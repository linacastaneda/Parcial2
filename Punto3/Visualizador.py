from graphviz import Digraph

# -------------------------------------------------------
# Árbol 1: else se asocia con el if interno
# if e1 then (if e2 then otras else otras)
# -------------------------------------------------------

def arbol_if_interno():
    dot = Digraph(comment="Else con if interno")

    dot.node('A', 'if')
    dot.node('B', 'cond: e1')
    dot.node('C', 'then')

    dot.node('D', 'if-else')
    dot.node('E', 'cond: e2')
    dot.node('F', 'then')
    dot.node('G', 'otras')
    dot.node('H', 'else')
    dot.node('I', 'otras')

    dot.edges([
        ('A','B'), ('A','C'), ('C','D'),
        ('D','E'), ('D','F'), ('F','G'),
        ('D','H'), ('H','I')
    ])

    return dot

# -------------------------------------------------------
# Árbol 2: else se asocia con el if externo
# (if e1 then if e2 then otras) else otras
# -------------------------------------------------------

def arbol_if_externo():
    dot = Digraph(comment="Else con if externo")

    dot.node('A', 'if-else')
    dot.node('B', 'cond: e1')
    dot.node('C', 'then')

    dot.node('D', 'if')
    dot.node('E', 'cond: e2')
    dot.node('F', 'then')
    dot.node('G', 'otras')

    dot.node('H', 'else')
    dot.node('I', 'otras')

    dot.edges([
        ('A','B'), ('A','C'), ('A','H'),
        ('C','D'),
        ('D','E'), ('D','F'), ('F','G'),
        ('H','I')
    ])

    return dot

# -------------------------------------------------------
# Generar imágenes
# -------------------------------------------------------

arbol_if_interno().render('arbol_if_interno', format='png', view=True)
arbol_if_externo().render('arbol_if_externo', format='png', view=True)