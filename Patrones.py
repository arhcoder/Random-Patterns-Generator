import random

# Alejandro Ramos: @arhcoder #

class Chess_Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, x, y, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y
    

# Diuja sólo en cruz | Como una torre en ajedrez #
class Rook_Pattern(Chess_Piece):

    def movimiento_xy(self):
        avance_xy = []

        # Controlador sirve porque sólo un se va a mover en un eje (En x o en y) #
        # Se elige la coordenada que no va a cambiar (x o y):
        controlador = random.choice([0, 1])
        
        if controlador == 0:
            avance_xy.append(0)
            avance_xy.append(random.choice([-1, 1]))
        else:
            avance_xy.append(random.choice([-1, 1]))
            avance_xy.append(0)
        return avance_xy


# Diuja en diagonal | Como un alfil en ajedrez #
class Bishop_Pattern(Chess_Piece):

    def movimiento_xy(self):
        avance_xy = []
        avance_xy.append(random.choice([-1, 1]))
        avance_xy.append(random.choice([-1, 1]))
        return avance_xy


# Dibuja en cualquier dirección | Como una reina en ajedrez #
class Queen_Pattern(Chess_Piece):

    def movimiento_xy(self):
        avance_xy = []
        avance_xy.append(random.choice([0, -1, 1]))
        avance_xy.append(random.choice([0, -1, 1]))
        return avance_xy