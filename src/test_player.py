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

#metodo que retorna un numero 
def hay_jugadores(lista_jugadores):
    cantidad_jugadores_rendidos=0 #variable contador
    for player in lista_jugadores: #acceder a cada elemento de la lista
        if player.canPlay==False: #Si su propiedad de poder jugar es falsa significa que se rindio'
            cantidad_jugadores_rendidos+=1
    return cantidad_jugadores_rendidos

bucle=True
while bucle:
    #validamos si  en la lista de jugadores al menos 1 no se ha rendido
    se_puede_continuar=True if hay_jugadores(listaJugadores) < len(listaJugadores) else False

    #aqui entra al if solo si el resultado es True
    if se_puede_continuar:
        for player in listaJugadores:
            if player.canPlay: #De la lista de usuarios solo le dar'a el turno al usuario que no se haya rendido
                player.pick_piece(player,the_board)
    else:
        bucle=False

#mensaje provisional para validar si se puede jugar
print("termino' el game")

# Le muestra al jugador cúantas y cuales piezas le quedan (OPCIONAL)
# print(f"{jugador_amelia.name}, te quedan estas [{len(jugador_amelia.pieces)}] piezas: ")
# print(jugador_amelia.show_pieces_jugador())

