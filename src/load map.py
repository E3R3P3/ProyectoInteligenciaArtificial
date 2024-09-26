from piece import Piece
from board import Board

NewMap = Board(16,16)#Creamos un objeto de la clase Board con las dimenciones 16x16

# Creamos algunas piezas para probar
# Entre cada corchete del arreglo son las filas y colocamos 1 donde queremos un fragmento de ficha
piece_L = Piece([[1, 0], [1, 0], [1, 1]], '#')# En el simbolo se puede colocar lo que sea que quiereas usar como ficha
piece_T = Piece([[1, 1, 1], [0, 1, 0], [0, 1, 0]], '@')
piece_O = Piece([[1, 1], [1, 1]], 'O')

print("Mapa creado.\n")
NewMap.print_map()
print("\n\n")
print("Mapa actualizado con la letra\n\n")
NewMap.place_piece(piece_T,1,6)
NewMap.place_piece(piece_L,6,8)
NewMap.place_piece(piece_T,8,2)
#imprimimos nuevamente el mapa para ver la letra
NewMap.print_map()