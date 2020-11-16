from Caminanate import Caminante_Borracho, Caminante_Cuadrado, Caminante_Diagonal

def caminata(nombre, tipo_de_caminanate, pasos):
    caminante = tipo_de_caminanate(nombre, 0, 0)
    positions = [(0, 0)]

    for _ in range(1, pasos + 1):
        x = caminante.x
        y = caminante.y
        nueva_x = x + caminante.movimiento_x()
        nueva_y = y + caminante.movimiento_y()
        caminante.caminar(x, y, nueva_x, nueva_y)
        positions.append((nueva_x, nueva_y))
    
    return positions

if __name__ == "__main__":
    print("\nBorracho:\n", caminata("Sergio", Caminante_Borracho, 20))
    print("\nCuadrado:\n", caminata("Rogelio", Caminante_Cuadrado, 20))
    print("\nDiagonal:\n", caminata("Jesús", Caminante_Diagonal, 20))