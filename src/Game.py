from board import Board
from player import Player
round = True
round_status = ''
initialized_players = False
listaJugadores=[]

the_board = Board(16, 16)


def hay_jugadores(lista_jugadores):
    cantidad_jugadores_rendidos=0 #variable contador
    for player in lista_jugadores: #acceder a cada elemento de la lista
        if player.canPlay==False: #Si su propiedad de poder jugar es falsa significa que se rindio'
            cantidad_jugadores_rendidos+=1
    return cantidad_jugadores_rendidos


if initialized_players == False:

    print("\033c", end="")

    print('𝔅𝔩𝔬𝔨𝔲𝔰')
    initialized_players = False

    print('\nRonda iniciada.')

    if initialized_players == False:
        name_player_1 = input('\nNombre del primer jugador:>')
        color_player_1 = input('\nColor del primer jugador:>')

        name_player_2 = input('\nNombre del segundo jugador:>')
        color_player_2 = input('\nColor del segundo jugador:>')
        player_1 = Player(1, name_player_1, color_player_2 )
        player_2 = Player(2, name_player_2, color_player_2 )
        listaJugadores=[player_1,player_2]

                
        initialized_players = True
        
bucle=True
while bucle:
    #   validamos si  en la lista de jugadores al menos 1 no se ha rendido
    se_puede_continuar=True if hay_jugadores(listaJugadores) < len(listaJugadores) else False

    #   aqui entra al if solo si el resultado es True
    if se_puede_continuar:
        for player in listaJugadores:
            if player.canPlay: #    De la lista de usuarios solo le dara el turno al usuario que no se haya rendido
                player.pick_piece(player, the_board)
    else:
        bucle=False

print("termino' el game")

    

