# PARADIGMA ORIENTADO A OBJETOS (POO)
## Modelados el mundo real

# PARADIGMA POO

class Vehiculo:
    # Constructor
    def __init__(self, placa):
        self.placa = placa # Guardamos placa

    def mostrar(self):
        # Metodo para mostrar placa
        print('Placa:', self.placa)

# Crear objeto
v1 = Vehiculo('NZB16E')
v1.mostrar()
#Caracteristica: objetos y clases