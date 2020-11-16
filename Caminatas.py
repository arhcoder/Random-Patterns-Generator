from Caminanate import Caminante_Borracho, Caminante_Cuadrado, Caminante_Diagonal
from bokeh.plotting import figure, output_file, show

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
            eje_x.append(nueva_x)
            eje_y.append(nueva_y)
            i += 1
    return positions

if __name__ == "__main__":
    pasos = 80000
    graphic_a = figure()
    graphic_b = figure()
    graphic_c = figure()

    eje_x = [0]
    eje_y = [0]
    print("\nBorracho:\n", caminata("Sergio", Caminante_Borracho, pasos))
    output_file("Caminante-Borracho.html")
    graphic_a.line(eje_x, eje_y, line_width = 2)
    show(graphic_a)

    eje_x = [0]
    eje_y = [0]
    print("\nCuadrado:\n", caminata("Rogelio", Caminante_Cuadrado, pasos))
    output_file("Caminante-Cuadrado.html")
    graphic_b.line(eje_x, eje_y, line_width = 2)
    show(graphic_b)

    eje_x = [0]
    eje_y = [0]
    print("\nDiagonal:\n", caminata("Jesús", Caminante_Diagonal, pasos))
    output_file("Caminante-Diagonal.html")
    graphic_c.line(eje_x, eje_y, line_width = 2)
    show(graphic_c)