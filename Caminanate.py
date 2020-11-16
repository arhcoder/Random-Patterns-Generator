import random

class Caminante:
    def __init__(self, nombre, x, y):
        self.nombre = nombre
        self.x = x
        self.y = y

    def caminar(self, x, y, avance_x, avance_y):
        x = self.x
        y = self.y
        x += avance_x
        y += avance_y
        self.x = avance_x
        self.y = avance_y

# Camina en cualquier dirección #
class Caminante_Borracho(Caminante):

    def movimiento_xy(self):
        avance_xy = [0, 0]

        # Controlador sirve porque sólo un se va a mover en un eje (En x o en y)
        controlador = random.choice([0, 1])
        avance_xy[controlador] = 0
        
        if controlador == 0:
            avance_xy[1] == random.choice([-1, 1])
        else:
            avance_xy[0] == random.choice([-1, 1])

        return avance_xy     
            

# Camina sólo en cruz #
class Caminante_Cuadrado(Caminante):

    def movimiento_x(self):
        avance_x = random.choice([0, -1, 1])
        return avance_x

    def movimiento_y(self):
        avance_y = random.choice([0, -1, 1])
        return avance_y

# Camina en diagonal #
class Caminante_Diagonal(Caminante):

    def movimiento_x(self):
        avance_x = random.choice([-1, 1])
        return avance_x

    def movimiento_y(self):
        avance_y = random.choice([-1, 1])
        return avance_y