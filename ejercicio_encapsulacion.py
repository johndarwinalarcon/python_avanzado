#EJERCICIO 1 - ENCAPSULACION
# Proteger datos dentro de una clase

# ENCAPSULACION

class Cliente:

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo # Privado con __

    def ver_saldo(self):
        # Metodo para ver saldo
        print('Saldo:', self.__saldo)

    def pagar(self, valor):
        # Modificar saldo de forma segura
        if valor <= self.__saldo:
            print('Pago realizado')
        else:
            print('Saldo insuficiente')

c = Cliente('Darwin', 1000)

c.ver_saldo()
c.pagar(10000)
c.ver_saldo

# c.__saldo x ERROR porque es privado