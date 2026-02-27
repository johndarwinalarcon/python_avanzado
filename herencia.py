# EJERCICIO 2 - HERENCIA
## una clase hereda de otra

# HERENCIA

class Vehiculo:

    def __init__(self, placa):
        self.placa = placa

    def info(self):
        print('Placa:', self.placa)


class Moto(Vehiculo):

    def __init__(self, placa, casco):
        super().__init__(placa) # Hereda placa
        self.casco = casco

    def info_moto(self):
        print('Placa:', self.placa, 'Casco:', self.casco)


m = Moto('NZB16E', True)
m.info()
m.info_moto()