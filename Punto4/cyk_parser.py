"""Parser CYK simple para lenguajes en forma normal de Chomsky.

Incluye definicion de la gramatica, tokenizacion y funcion principal
para evaluar si una expresion pertenece al lenguaje.
"""

import time
import tracemalloc

# ── Gramatica en FNC ─────────────────────────────────────────────
# Producciones binarias: A -> B C
BINARIAS = {
    ('E',  'PLUS', 'T')    : 'E',
    ('T',  'E',    'PLUS') : None,   # auxiliar
    ('T',  'TIMES','F')    : 'T',
    ('F',  'LPAREN','A3')  : 'F',
    ('A1', 'PLUS', 'T')    : 'A1',
    ('A2', 'TIMES','F')    : 'A2',
    ('A3', 'E',    'RPAREN'): 'A3',
}

# Producciones binarias limpias (lado derecho -> lado izquierdo)
PROD_BIN = [
    ('E',  'E',      'A1'),
    ('A1', 'PLUS',   'T'),
    ('T',  'T',      'A2'),
    ('A2', 'TIMES',  'F'),
    ('F',  'LPAREN', 'A3'),
    ('A3', 'E',      'RPAREN'),
]

# Producciones unitarias: A -> B
PROD_UNIT = [
    ('E', 'T'),
    ('T', 'F'),
]

def tokenizar(expresion: str):
    """Convierte la cadena en lista de tokens terminales."""
    tokens = []
    i = 0
    while i < len(expresion):
        c = expresion[i]
        if c.isspace():
            i += 1
            continue
        elif c.isdigit():
            j = i
            while j < len(expresion) and expresion[j].isdigit():
                j += 1
            tokens.append(('num', expresion[i:j]))
            i = j
        elif c == '+': tokens.append(('PLUS',   '+')); i += 1
        elif c == '*': tokens.append(('TIMES',  '*')); i += 1
        elif c == '(': tokens.append(('LPAREN', '(')); i += 1
        elif c == ')': tokens.append(('RPAREN', ')')); i += 1
        else:
            raise ValueError(f"Token desconocido: {c}")
    return tokens

def terminal_a_no_terminales(token_tipo):
    """Retorna que no terminales pueden generar este terminal."""
    mapa = {
        'num'   : ['F'],
        'PLUS'  : ['PLUS'],
        'TIMES' : ['TIMES'],
        'LPAREN': ['LPAREN'],
        'RPAREN': ['RPAREN'],
    }
    return mapa.get(token_tipo, [])

def cyk(expresion: str):
    """Aplica el algoritmo CYK para verificar la pertenencia a la gramatica."""
    tokens = tokenizar(expresion)
    n = len(tokens)
    if n == 0:
        return False

    # tabla[i][j] = conjunto de no terminales que generan tokens[i..j]
    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Paso 1: inicializar diagonal (longitud 1)
    for i, (tipo, _) in enumerate(tokens):
        for nt in terminal_a_no_terminales(tipo):
            tabla[i][i].add(nt)
        # Cerrar bajo producciones unitarias
        cambio = True
        while cambio:
            cambio = False
            for (A, B) in PROD_UNIT:
                if B in tabla[i][i] and A not in tabla[i][i]:
                    tabla[i][i].add(A)
                    cambio = True

    # Paso 2: subcadenas de longitud 2 a n
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for (A, B, C) in PROD_BIN:
                    if B in tabla[i][k] and C in tabla[k+1][j]:
                        tabla[i][j].add(A)
            # Cerrar bajo producciones unitarias
            cambio = True
            while cambio:
                cambio = False
                for (A, B) in PROD_UNIT:
                    if B in tabla[i][j] and A not in tabla[i][j]:
                        tabla[i][j].add(A)
                        cambio = True

    return 'E' in tabla[0][n-1]

def parsear_cyk(expresion: str):
    """Mide tiempo y memoria usados al ejecutar el parser CYK."""
    tracemalloc.start()
    t0 = time.perf_counter()

    resultado = cyk(expresion)

    t1 = time.perf_counter()
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        'valido'  : resultado,
        'tiempo_ms': (t1 - t0) * 1000,
        'memoria_kb': pico / 1024,
    }