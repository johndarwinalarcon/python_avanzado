##PARADIGMA DECLARATIVO
# Decimos que queremos, no como

# PARADIGMA DECLARATIVO usando compresion de listas

vehiculos = ['NZB16E','BBB222','CCC333']

# Queremos solo placas que empiezan por B
filtrado = [v for v in vehiculos if v.startswith('B')] # esta funcion hace el filtrado por nosotros, no le decimos como hacerlo, solo que queremos

print('Filtrados:', filtrado)