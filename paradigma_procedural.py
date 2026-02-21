## PARADIGMA PROCEDURAL

def registrar_entrada(lista, placa):
    # Agrega un vehiculo a la lista
    lista.append(placa)

def registrar_salida(lista, placa):
    # elimina vehiculo si existe
    if placa in lista:
        lista.remove(placa)

vehiculos = []

registrar_entrada(vehiculos, 'NZB16E')
registrar_entrada(vehiculos, 'BBBB23B')

print('vehiculos:', vehiculos)

registrar_salida(vehiculos, 'NZB16E')

print('Despues salida:', vehiculos)