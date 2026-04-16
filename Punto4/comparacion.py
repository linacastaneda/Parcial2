from cyk_parser import parsear_cyk
from ll1_parser import parsear_ll1

pruebas = [
    # (expresion, es_valida, descripcion)
    ("2 + 3",                        True,  "Suma simple"),
    ("2 + 3 * 4",                    True,  "Suma y multiplicación"),
    ("(2 + 3) * 4",                  True,  "Con paréntesis"),
    ("2 + 3 * 4 + 5 * 6",            True,  "Expresión mediana"),
    ("((2 + 3) * (4 + 5))",          True,  "Paréntesis anidados"),
    ("2 + 3 * 4 + 5 * 6 + 7 * 8 + 9", True, "Expresión larga"),
    ("2 +",                          False, "Inválida: operador colgante"),
    ("* 3",                          False, "Inválida: empieza con *"),
    ("(2 + 3",                       False, "Inválida: paréntesis sin cerrar"),
]

print(f"\n{'='*75}")
print(f"{'Expresión':<35} {'Válida':^7} {'CYK(ms)':^10} {'LL1(ms)':^10} "
      f"{'CYK(KB)':^9} {'LL1(KB)':^9}")
print(f"{'='*75}")

for expr, esperado, desc in pruebas:
    r_cyk = parsear_cyk(expr)
    r_ll1 = parsear_ll1(expr)

    valido = "si" if r_cyk['valido'] == esperado else "❌"
    print(f"{desc:<35} {valido:^7} "
          f"{r_cyk['tiempo_ms']:^10.4f} {r_ll1['tiempo_ms']:^10.4f} "
          f"{r_cyk['memoria_kb']:^9.2f} {r_ll1['memoria_kb']:^9.2f}")

print(f"{'='*75}")