# Proyecto - Análisis Sintáctico y Parsers

## 1. Introducción

Este proyecto tiene como objetivo diseñar e implementar diferentes técnicas de análisis sintáctico, incluyendo el uso de ANTLR, parsers LL(1), el algoritmo CYK y un parser descendente recursivo.

Se desarrollan cinco puntos principales que abarcan desde el diseño de gramáticas hasta la comparación de algoritmos de parsing.

---

## 2. Punto 1: Diseño de la gramática NoSQL

Se diseñó una gramática para un lenguaje tipo NoSQL orientado a documentos, que soporta operaciones CRUD:

- CREATE
- READ
- UPDATE
- DELETE

El modelo se basa en documentos compuestos por pares campo-valor, similares a estructuras JSON.

La gramática permite:

- documentos vacíos y anidados
- condiciones con operadores lógicos
- asignaciones y consultas

Se identificó ambigüedad en las condiciones, la cual se resuelve en la implementación mediante precedencia de operadores.

---

## 3. Punto 2: Implementación en ANTLR v4

La gramática fue implementada en ANTLR v4 (`gramatica.g4`), generando:

- Lexer
- Parser
- Listener

Se desarrolló un script en Python para probar el parser.

### Resultados

- Se validaron correctamente sentencias válidas
- Se detectaron errores sintácticos en sentencias inválidas
- Se generaron árboles sintácticos

Además, se visualizó el árbol usando Graphviz.

---

## 4. Punto 3: Ambigüedad en if-then-else

Se analizó la ambigüedad del problema clásico del `dangling else`.

Se demostró que la gramática original es ambigua mediante:

- una cadena problemática
- dos árboles de derivación distintos

Se propuso una gramática corregida separando:

- proposiciones emparejadas
- proposiciones no emparejadas

---

## 5. Punto 4: Parser CYK vs LL(1)

Se implementaron dos parsers:

- CYK (programación dinámica)
- LL(1) (predictivo)

### LL(1)

Se utilizó la gramática:

E → T E'  
E' → + T E' | ε  
T → F T'  
T' → * F T' | ε  
F → ( E ) | num  

Se calcularon:

- FIRST
- FOLLOW
- tabla de predicción LL(1)

El parser utiliza una pila y una tabla para analizar la entrada.

### CYK

Se implementó usando Forma Normal de Chomsky y programación dinámica.

### Comparación

- CYK: O(n³), más general
- LL(1): O(n), más eficiente

Se midieron:

- tiempo
- memoria

---

## 6. Punto 5: Parser descendente recursivo

Se implementó un parser manual con:

- analizador léxico
- funciones recursivas
- algoritmo de emparejamiento (`match`)

El parser reconoce:

- asignaciones
- expresiones
- condicionales
- estructuras anidadas

Se probaron casos válidos e inválidos, detectando errores sintácticos correctamente.

