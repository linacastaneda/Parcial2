"""Parser LL(1) simple para expresiones aritmeticas.

Este modulo incluye la tokenizacion, la tabla LL(1) y el
analizador sintactico predictivo basado en pila.
"""

import time
import tracemalloc

def tokenizar(expresion: str):
    """Convierte una expresion en una lista de tokens reconocibles."""
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
            tokens.append('num')
            i = j
        elif c == '+': tokens.append('+'); i += 1
        elif c == '*': tokens.append('*'); i += 1
        elif c == '(': tokens.append('('); i += 1
        elif c == ')': tokens.append(')'); i += 1
        else:
            raise ValueError(f"Token desconocido: {c}")
    tokens.append('$')
    return tokens

# Tabla LL(1): tabla[NoTerminal][terminal] = produccion (lista de simbolos)
TABLA = {
    'E' : {
        'num': ['T', "E'"],
        '('  : ['T', "E'"],
    },
    "E'": {
        '+'  : ['+', 'T', "E'"],
        ')'  : [],   # epsilon
        '$'  : [],   # epsilon
    },
    'T' : {
        'num': ['F', "T'"],
        '('  : ['F', "T'"],
    },
    "T'": {
        '+'  : [],   # epsilon
        '*'  : ['*', 'F', "T'"],
        ')'  : [],   # epsilon
        '$'  : [],   # epsilon
    },
    'F' : {
        'num': ['num'],
        '('  : ['(', 'E', ')'],
    },
}

NO_TERMINALES = {'E', "E'", 'T', "T'", 'F'}

def ll1(expresion: str):
    """Analiza la expresion usando una tabla LL(1) y una pila de analisis."""
    tokens = tokenizar(expresion)
    pila = ['$', 'E']
    idx = 0

    while pila:
        tope = pila[-1]
        actual = tokens[idx]

        if tope == '$' and actual == '$':
            # Analisis correcto si la pila y los tokens han terminado juntos
            return True
        elif tope == actual:          # terminal coincide
            pila.pop()
            idx += 1
        elif tope in NO_TERMINALES:
            prod = TABLA.get(tope, {}).get(actual)
            if prod is None:
                # No hay produccion valida para el no terminal y token actual
                return False
            pila.pop()
            for simbolo in reversed(prod):
                pila.append(simbolo)
        else:
            # Tope de pila no terminal ni igual a token actual
            return False

    return False

def parsear_ll1(expresion: str):
    """Evalua la expresion y devuelve validez, tiempo y memoria usada."""
    tracemalloc.start()
    t0 = time.perf_counter()

    resultado = ll1(expresion)

    t1 = time.perf_counter()
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        'valido'   : resultado,
        'tiempo_ms': (t1 - t0) * 1000,
        'memoria_kb': pico / 1024,
    } 