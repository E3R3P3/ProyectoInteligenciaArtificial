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

    print('''
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░╔══╗░╔╗░░░░░░░╔╗░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░║╔╗║░║║░░░░░░░║║░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░║╚╝╚╗║║░░░╔══╗║║╔╗╔╗╔╗╔══╗░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░║╔═╗║║║░╔╗║╔╗║║╚╝╝║║║║║══╣░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░║╚═╝║║╚═╝║║╚╝║║╔╗╗║╚╝║╠══║░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░╚═══╝╚═══╝╚══╝╚╝╚╝╚══╝╚══╝░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ''')
    initialized_players = False

    print('''\n\tComo jugar.

                Aqui Escribir las reglas del juego.
          
          ''')

    if initialized_players == False:
        name_player_1 = input('\n\tNombre del primer jugador:>')
        color_player_1 = 'rojo'

        name_player_2 = input('\n\tNombre del segundo jugador:>')
        color_player_2 = 'azul'
        print("\033c", end="")
        player_1 = Player(1, name_player_1, color_player_1 )
        player_2 = Player(2, name_player_2, color_player_2 )
        listaJugadores=[player_1,player_2]

                
        #initialized_players = True
        
bucle=True
while bucle:
    #validamos si  en la lista de jugadores al menos 1 no se ha rendido
    se_puede_continuar=True if hay_jugadores(listaJugadores) < len(listaJugadores) else False

    if initialized_players == False:
        the_board.print_map()
        initialized_players = True

    #aqui entra al if solo si el resultado es True
    if se_puede_continuar:
        for player in listaJugadores:
            if player.canPlay: #De la lista de usuarios solo le dar'a el turno al usuario que no se haya rendido
                player.pick_piece(player,the_board)
    else:
        bucle=False

print("\033c", end="")
        
print(f'\nPuntos de {player_1.name} puntos = {player_1.point}')
print(f'\nPuntos de {player_2.name} puntos = {player_2.point}')     
if player_1.point > player_2.point:
      print(f'\n {player_1.name} GANO!!')
elif player_2.point > player_1.point:
      print(f'\n {player_2.name} GANO!!')
  
print('''
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░╔═══╗░░░░░░░░░░░░╔═══╗░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░║╔═╗║░░░░░░░░░░░░║╔═╗║░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░║║░╚╝╔══╗╔╗╔╗╔══╗║║░║║╔╗╔╗╔══╗╔═╗░░░░░░░░░░░░░
        ░░░░░░░░░░░░║║╔═╗║╔╗║║╚╝║║║═╣║║░║║║╚╝║║║═╣║╔╝░░░░░░░░░░░░░
        ░░░░░░░░░░░░║╚╩═║║╔╗║║║║║║║═╣║╚═╝║╚╗╔╝║║═╣║║░░░░░░░░░░░░░░
        ░░░░░░░░░░░░╚═══╝╚╝╚╝╚╩╩╝╚══╝╚═══╝░╚╝░╚══╝╚╝░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
''')

    

