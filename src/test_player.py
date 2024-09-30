from board import Board
from player import Player

# ARCHIVO HECHO ÚNICAMENTE PARA PROBAR LAS ACCIONES DE UN JUGADOR

# Crea el tablero de juego
the_board = Board(16, 16)

# Crea un jugador
player_amelia = Player(1, "Amelia", "Blue")
player_rafael = Player(2, "Rafael", "rojo")
listaJugadores=[player_amelia,player_rafael]
# Muestra el tablero vacío inicialmente para referencia
print()
print("Welcome to BLOKUS! \n")
the_board.print_map()

# Prueba la selección de una p ieza y la colocación en el tablero
for player in listaJugadores:
    while player.canPlay:
        player.pick_piece(the_board)
        

print("termino' el game")

# Le muestra al jugador cúantas y cuales piezas le quedan (OPCIONAL)
# print(f"{jugador_amelia.name}, te quedan estas [{len(jugador_amelia.pieces)}] piezas: ")
# print(jugador_amelia.show_pieces_jugador())

