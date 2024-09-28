from piece import Piece
from board import Board

#Creamos un objeto de la clase Board con las dimensiones 16 x 16
NewMap = Board(16,16)

# Creamos piezas para probar
# Entre cada corchete del arreglo son las filas y colocamos 1 donde queremos un fragmento de ficha
piece_O = Piece(
    shape=[['#', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],
    piece_id=1,
    color='rojo',
    value=10,
    symbol="T",
    orientation=0
)

# Imprime el board vacío
print("Mapa creado.\n")
NewMap.print_map()

# Refleja la pieza "piece_O" horizontalmente
piece_O.reflect(horizontal=True)

# Coloca la pieza ya reflejada con el método anterior, en el board
print("Mapa actualizado con la pieza.\n")

# Coloca la pieza ya reflejada con el método anterior, en el board
NewMap.place_piece(piece_O,2,1)

# Imprimimos nuevamente el board para ver pieza colocada en la posición indicada anteriormente "2,1"
NewMap.print_map()

