
import re


class Token:
    """Representa un token de la entrada lexica."""

    def __init__(self, tipo, valor):
        """Inicializa un token con su tipo y su valor literal."""
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"Token({self.tipo}, {self.valor})"


def tokenizar(cadena):
    """Convierte una cadena de entrada en una lista de tokens.

    Se reconocen palabras reservadas, identificadores, numeros, operadores,
    paréntesis, llaves y punto y coma. Los espacios en blanco se omiten.
    """
    especificacion = [
        ("IF", r"\bif\b"),
        ("ELSE", r"\belse\b"),
        ("NUM", r"\b\d+\b"),
        ("ID", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
        ("EQ", r"=="),
        ("NE", r"!="),
        ("LE", r"<="),
        ("GE", r">="),
        ("LT", r"<"),
        ("GT", r">"),
        ("ASSIGN", r"="),
        ("PLUS", r"\+"),
        ("MINUS", r"-"),
        ("TIMES", r"\*"),
        ("DIV", r"/"),
        ("LPAREN", r"\("),
        ("RPAREN", r"\)"),
        ("LBRACE", r"\{"),
        ("RBRACE", r"\}"),
        ("SEMI", r";"),
        ("SKIP", r"[ \t\n]+"),
        ("MISMATCH", r"."),
    ]

    patron = "|".join(f"(?P<{nombre}>{regex})" for nombre, regex in especificacion)
    tokens = []

    for mo in re.finditer(patron, cadena):
        tipo = mo.lastgroup
        valor = mo.group()

        if tipo == "SKIP":
            continue
        if tipo == "MISMATCH":
            raise SyntaxError(f"Símbolo inesperado: {valor}")

        tokens.append(Token(tipo, valor))

    tokens.append(Token("EOF", "$"))
    return tokens


class Parser:
    """Parser recursivo descendente para sentencias simples y condicionales."""

    def __init__(self, tokens):
        """Inicializa el parser con la lista de tokens ya tokenizados."""
        self.tokens = tokens
        self.pos = 0
        self.actual = self.tokens[self.pos]

    def avanzar(self):
        """Avanza al siguiente token de la lista."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.actual = self.tokens[self.pos]

    def match(self, tipo_esperado):
        """Verifica que el token actual sea del tipo esperado y avanza.

        Si el token no coincide, lanza un error de sintaxis.
        """
        if self.actual.tipo == tipo_esperado:
            self.avanzar()
        else:
            raise SyntaxError(
                f"Se esperaba {tipo_esperado}, pero se encontró {self.actual.tipo} ('{self.actual.valor}')"
            )

    def parse(self):
        """Inicia el analisis sintactico a partir del simbolo inicial del lenguaje."""
        self.programa()
        self.match("EOF")
        return True

    def programa(self):
        """Analiza el programa completo como una lista de sentencias."""
        self.lista_sentencias()

    def lista_sentencias(self):
        """Analiza una secuencia de sentencias hasta que no haya mas tokens validos."""
        while self.actual.tipo in ("ID", "IF"):
            self.sentencia()

    def sentencia(self):
        """Analiza una sentencia de asignacion o un condicional."""
        if self.actual.tipo == "ID":
            self.asignacion()
        elif self.actual.tipo == "IF":
            self.condicional()
        else:
            raise SyntaxError(f"Sentencia no válida cerca de '{self.actual.valor}'")

    def asignacion(self):
        """Analiza una instruccion de asignacion con expresion y punto y coma."""
        self.match("ID")
        self.match("ASSIGN")
        self.expr()
        self.match("SEMI")

    def condicional(self):
        """Analiza una estructura condicional if con bloque opcional else."""
        self.match("IF")
        self.match("LPAREN")
        self.condicion()
        self.match("RPAREN")
        self.match("LBRACE")
        self.lista_sentencias()
        self.match("RBRACE")

        if self.actual.tipo == "ELSE":
            self.match("ELSE")
            self.match("LBRACE")
            self.lista_sentencias()
            self.match("RBRACE")

    def condicion(self):
        """Analiza una condicion compuesta por valor, operador relacional y valor."""
        if self.actual.tipo not in ("ID", "NUM"):
            raise SyntaxError(f"Condición inválida cerca de '{self.actual.valor}'")

        self.valor()
        self.op_rel()
        self.valor()

    def op_rel(self):
        """Analiza el operador relacional en una condicion."""
        if self.actual.tipo in ("EQ", "NE", "LT", "GT", "LE", "GE"):
            self.avanzar()
        else:
            raise SyntaxError(f"Operador relacional inválido cerca de '{self.actual.valor}'")

    def expr(self):
        """Analiza una expresion aritmetica con suma y resta."""
        self.termino()
        self.expr_p()

    def expr_p(self):
        """Analiza continuaciones de expresiones con operadores + o -."""
        while self.actual.tipo in ("PLUS", "MINUS"):
            self.avanzar()
            self.termino()

    def termino(self):
        """Analiza un termino aritmetico con multiplicacion o division."""
        self.factor()
        self.termino_p()

    def termino_p(self):
        """Analiza continuaciones de terminos con operadores * o /."""
        while self.actual.tipo in ("TIMES", "DIV"):
            self.avanzar()
            self.factor()

    def factor(self):
        """Analiza un factor que puede ser id, numero o subexpresion entre paréntesis."""
        if self.actual.tipo == "ID":
            self.match("ID")
        elif self.actual.tipo == "NUM":
            self.match("NUM")
        elif self.actual.tipo == "LPAREN":
            self.match("LPAREN")
            self.expr()
            self.match("RPAREN")
        else:
            raise SyntaxError(f"Factor inválido cerca de '{self.actual.valor}'")

    def valor(self):
        """Analiza un valor usado en una condicion, id o numero."""
        if self.actual.tipo == "ID":
            self.match("ID")
        elif self.actual.tipo == "NUM":
            self.match("NUM")
        else:
            raise SyntaxError(f"Valor inválido cerca de '{self.actual.valor}'")


def probar(cadena):
    """Ejecuta la tokenizacion y el parseo de una cadena de prueba."""
    print("=" * 60)
    print("Entrada:")
    print(cadena)
    try:
        tokens = tokenizar(cadena)
        parser = Parser(tokens)
        parser.parse()
        print("Resultado: VÁLIDA")
    except Exception as e:
        print("Resultado: INVÁLIDA")
        print(f"Error: {e}")


if __name__ == "__main__":
    pruebas = [
        "x = 5;",
        "y = x + 3;",
        "if (x > 2) { y = 4; }",
        "if (x > 2) { y = 4; } else { y = 7; }",
        "if (x > 2) { y = 4; if (y < 10) { z = 1; } }",
        "x 5;",
        "if x > 2 { y = 4; }",
        "if (x > 2) y = 4;",
        "if (x > 2) { y = 4 }",
    ]

    for p in pruebas:
        probar(p)