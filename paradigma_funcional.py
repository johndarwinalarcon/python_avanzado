# Paradigma Funcional

## Usamos funciones puras (sin cambiar datos originales)

# Paradigma Funcional

def calcular_total(horas):
    # no cambia nada externo
    return horas * 2000

total = calcular_total(3)
print('Total a pagar: ', total)