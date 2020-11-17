from Patrones import Rook_Pattern, Bishop_Pattern, Queen_Pattern
from bokeh.plotting import figure, output_file, show

# Alejandro Ramos: @arhcoder #

def generar_patter(Chess_Piece, movimientos):

    pieza = Chess_Piece(0, 0)
    positions = [(0, 0)]
    paso = 1

    while paso <= movimientos:

        x = pieza.x
        y = pieza.y
        avance_xy = pieza.movimiento_xy()
        nueva_x = x + avance_xy[0]
        nueva_y = y + avance_xy[1]

        if avance_xy[0] == 0 and avance_xy[1] == 0:
            pass
        else:
            pieza.dibujar(x, y, nueva_x, nueva_y)
            positions.append((nueva_x, nueva_y))
            eje_x.append(nueva_x)
            eje_y.append(nueva_y)
            paso += 1

    return positions

if __name__ == "__main__":
    
    print("\n\n| GENERADOR DE PARONES ALEATORIOS |\n\n")
    movimientos = int(input("Cantidad de lineas en cada patrón: "))

    Graphic_Rook_Pattern = figure()
    Graphic_Bishop_Pattern = figure()
    Graphic_Queen_Pattern = figure()

    eje_x = [0]
    eje_y = [0]

    print("\nPatrón de Torre:\n", generar_patter(Rook_Pattern, movimientos))
    output_file("Patrón-de-Torre.html")
    Graphic_Rook_Pattern.line(eje_x, eje_y, line_width=2)
    show(Graphic_Rook_Pattern)

    eje_x = [0]
    eje_y = [0]

    print("\nPatrón de Alfil:\n", generar_patter(Bishop_Pattern, movimientos))
    output_file("Patrón-de-Alfil.html")
    Graphic_Bishop_Pattern.line(eje_x, eje_y, line_width=2)
    show(Graphic_Bishop_Pattern)

    eje_x = [0]
    eje_y = [0]

    print("\nPatrón de Reina:\n", generar_patter(Queen_Pattern, movimientos))
    output_file("Patrón-de-Reina.html")
    Graphic_Queen_Pattern.line(eje_x, eje_y, line_width=2)
    show(Graphic_Queen_Pattern)