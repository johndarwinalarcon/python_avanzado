# ejemplo de vida real

# piensa en el boton "pagar" en tu parqueadero

# cliente carro --> paga 3000

# cliente moto --> paga 1500

# cliente camion --> paga 6000

# el boton se llama igual: pagar
# pero hace cosas diferentes.

## Creamos clases diferentes

class Carro:
    def pagar(self):
        # Este metodo es para carros
        print('Carro paga 3000')

class Moto:
    def pagar(self):
        # Este metodo es para motos
        print('Moto paga 1500')

class Camion:
    def pagar(self):
        # Este metodo es para camiones
        print('Camion paga 6000')


# Metodo o funcion que usa cualquier objecto
def cobrar(vehiculo):
    # No sabemos si es carro, moto o camion
    # Solo sabemos que tiene pagar()
    vehiculo.pagar()


# Creamos objetos
c = Carro()
m = Moto()
cam = Camion()

# Usamos la misma funcion o metodo
cobrar(c)
cobrar(m)
cobrar(cam)



### -------------------------------------
### Ejemplo poliformismo en Animales
### -------------------------------------

def sonidos(animal):
    animal.sonido
    

class Perro:
    def sonido(self):
        print('Wua Wua Wua')

class Gato:
    def sonido(self):
        print('Mia Mia Mia')

class Vaca:
    def sonido(self):
        print('Muu Muu Muu')

a = Perro()
b = Gato()
c = Vaca()

sonidos(a)
sonidos(b)
sonidos(c)