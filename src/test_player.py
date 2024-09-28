from board import Board
from player import Player

# ARCHIVO HECHO ÚNICAMENTE PARA PROBAR LAS ACCIONES DE UN JUGADOR

# Crea el tablero de juego
tablero = Board(16, 16)

# Crea un jugador
jugador_amelia = Player(1, "Amelia", "Blue")

# Muestra el tablero vacío inicialmente para referencia
print()
print("Welcome to BLOKUS! \n")
tablero.print_map()

# Prueba la selección de una pieza y la colocación en el tablero
print()
jugador_amelia.colocar_pieza(tablero)

# Le muestra al jugador cúantas y cuales piezas le quedan (OPCIONAL)
# print(f"{jugador_amelia.name}, te quedan estas [{len(jugador_amelia.pieces)}] piezas: ")
# print(jugador_amelia.mostrar_piezas_jugador())

