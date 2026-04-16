import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from graphviz import Digraph

from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser


class ErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"Línea {line}:{column} -> {msg}")


def imprimir_arbol_bonito(tree, parser, indent=0):
    """Imprime el árbol sintáctico con indentación."""
    if tree is None:
        return

    if hasattr(tree, "getRuleIndex"):
        nombre = parser.ruleNames[tree.getRuleIndex()]
    else:
        nombre = tree.getText()

    print("  " * indent + str(nombre))

    for i in range(tree.getChildCount()):
        hijo = tree.getChild(i)
        imprimir_arbol_bonito(hijo, parser, indent + 1)


def dibujar_arbol(tree, parser, nombre_archivo="arbol_sintactico"):
    """Genera una imagen PNG del árbol sintáctico usando Graphviz."""
    dot = Digraph(comment="Árbol sintáctico")
    contador = [0]

    def recorrer(nodo, padre=None):
        node_id = str(contador[0])
        contador[0] += 1

        if hasattr(nodo, "getRuleIndex"):
            label = parser.ruleNames[nodo.getRuleIndex()]
        else:
            label = nodo.getText()

        dot.node(node_id, label)

        if padre is not None:
            dot.edge(padre, node_id)

        for i in range(nodo.getChildCount()):
            recorrer(nodo.getChild(i), node_id)

    recorrer(tree)
    dot.render(nombre_archivo, format="png", view=True)
    print(f"  Imagen generada: {nombre_archivo}.png")


def parsear(texto: str, mostrar_arbol=False, dibujar=False, nombre_imagen="arbol_sintactico"):
    input_stream = InputStream(texto)
    lexer = gramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)

    parser.removeErrorListeners()
    error_listener = ErrorCollector()
    parser.addErrorListener(error_listener)

    tree = parser.programa()

    if error_listener.errores:
        print("  INVÁLIDO")
        for e in error_listener.errores:
            print(f"     {e}")
    else:
        print("  VÁLIDO")

        if mostrar_arbol:
            print("  Árbol sintáctico:")
            imprimir_arbol_bonito(tree, parser)

        if dibujar:
            dibujar_arbol(tree, parser, nombre_imagen)


pruebas = [
    ('CREATE usuarios { nombre: "Lina", edad: 20, activo: true }', True),
    ('CREATE log {}', True),
    ('READ usuarios', True),
    ('READ usuarios WHERE edad > 18', True),
    ('READ usuarios WHERE edad > 18 AND activo = true', True),
    ('READ usuarios WHERE NOT activo = false', True),
    ('READ usuarios WHERE edad > 18 AND ciudad = "Bogota" OR activo = true', True),
    ('UPDATE usuarios SET ciudad = "Medellin" WHERE nombre = "Lina"', True),
    ('UPDATE usuarios SET activo = false', True),
    ('DELETE usuarios WHERE edad < 18', True),
    ('CREATE usuarios nombre: "Lina"', False),
    ('READ WHERE edad > 18', False),
    ('UPDATE usuarios edad = 21', False),
    ('READ usuarios WHERE AND edad > 18', False),
]

print("=" * 60)
print("PRUEBAS DEL PARSER")
print("=" * 60)

for i, (entrada, esperado) in enumerate(pruebas, 1):
    print(f"\nPrueba {i}: {entrada}")

    # Mostrar árbol bonito solo en algunas pruebas válidas
    if i in [1, 5, 8]:
        parsear(entrada, mostrar_arbol=True, dibujar=False)
    else:
        parsear(entrada, mostrar_arbol=False, dibujar=False)

print("\n" + "=" * 60)

# Ejemplo extra: generar imagen con Graphviz para una prueba representativa
print("\nGenerando imagen del árbol para una prueba representativa...\n")
parsear(
    'READ usuarios WHERE edad > 18 AND activo = true',
    mostrar_arbol=True,
    dibujar=True,
    nombre_imagen="arbol_read_where"
)