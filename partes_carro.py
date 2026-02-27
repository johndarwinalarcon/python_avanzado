class Carro: #creando la clase o modelo

    #Construtor o iniciador
    def __init__(self, marca, color): # Constructor 
        self.marca = marca ## atributo donde cada carro tiene su propia marca
        self.color = color ## atributo donde cada uno tiene su color
        self.velocidad = 0 ## asignamos valor
        self.encendido = False ## asignamos valor

    # Metodo
    def encender(self):
        self.encendido = True
        print('El carro esta encendido')

    # Metodo
    def apagar(self):
        self.encendido = False
        print('El carro esta apagado')

    # Metodo
    def acelerar(self):
        self.velicidad += 10
        print('El carro acelera. velocidad: ', self.velocidad)

    # Metodo
    def frenar(self):
        self.velocidad -=10
        if self.velocidad < 0:
            self.velocidad = 0
        print('El carro frena, velocidad', self.velocidad)

## Instanciar un objecto
carro1 = Carro('Toyota','Blanca') ## Intancia o instanciar un objecto
carro2 = Carro('Mazda','Rojo') ## Instancia

## Acciones
carro1.encender()
carro1.acelerar()
carro1.acelerar()
carro1.frenar()
carro1.frenar()
carro1.apagar()

print('-------------------------------')

carro2.acelerar()