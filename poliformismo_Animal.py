### -------------------------------------
### Ejemplo poliformismo en Animales
### -------------------------------------

# Metodo - Funcion - polimorfismo
def sonidos(animal):
    animal.sonido() ## se llama el metodo de cada clase 
    
# Clases - Objectos
class Perro:
    def sonido(self):
        print('Wua Wua Wua')

class Gato:
    def sonido(self):
        print('Mia Mia Mia')

class Vaca:
    def sonido(self):
        print('Muu Muu Muu')

# instanciar objectos
a = Perro()
b = Gato()
c = Vaca()


sonidos(a)
sonidos(b)
sonidos(c)