# Poliformismo
# Mismo metodo, distinto comportamiento

# Polimorfismo

class Carro:
    def pagar(self):
        print('Tarifa carro 3000')

class Moto:
    def pagar(self):
        print('Tarifa moto 1500')

def cobrar(vehiculo):
    vehiculo.pagar() # no importa el tipo 


c = Carro()
m = Moto()

cobrar(c)
cobrar(m)