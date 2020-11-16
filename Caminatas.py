from Caminanate import Caminante_Borracho, Caminante_Cuadrado, Caminante_Diagonal

def caminata(nombre, tipo_de_caminanate, pasos):
    caminante = tipo_de_caminanate(nombre, 0, 0)
    positions = [(0, 0)]
    i = 1

    while i <= pasos:
        x = caminante.x
        y = caminante.y
        avance_xy = caminante.movimiento_xy()
        nueva_x = x + avance_xy[0]
        nueva_y = y + avance_xy[1]

        if avance_xy[0] == 0 and avance_xy[1] == 0:
            pass
        else:
            caminante.caminar(x, y, nueva_x, nueva_y)
            positions.append((nueva_x, nueva_y))
            i += 1
    return positions

if __name__ == "__main__":
    pasos = 100
    print("\nBorracho:\n", caminata("Sergio", Caminante_Borracho, pasos))
    print("\nCuadrado:\n", caminata("Rogelio", Caminante_Cuadrado, pasos))
    print("\nDiagonal:\n", caminata("Jesús", Caminante_Diagonal, pasos))