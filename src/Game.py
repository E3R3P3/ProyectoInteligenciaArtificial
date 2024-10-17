from board import Board
from player import Player
round = True
round_status = ''
initialized_players = False
listaJugadores=[]

the_board = Board(16, 16)

def validate_name(text):
    while True:
        name = input(f"\n\tNombre del {text} jugador:>")
        
        # Verificar si es solo texto
        if not name.isalpha():
            print("\n\tEl nombre solo debe contener letras. Intenta nuevamente.")
            continue
        
        # Verificar la longitud del nombre (por ejemplo, entre 2 y 30 caracteres)
        if len(name) < 2 or len(name) > 30:
            print("\n\tEl nombre debe tener entre 2 y 30 caracteres. Intenta nuevamente.")
            continue
        
        # Si pasa ambas validaciones, salimos del bucle
        return name

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
        name_player_1 = validate_name('primer')
        color_player_1 = 'rojo'

        name_player_2 = validate_name('segundo')
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
        jugadaValida = False
        for player in listaJugadores:
            if player.canPlay: #De la lista de usuarios solo le dar'a el turno al usuario que no se haya rendido
                jugadaValida = player.pick_piece(the_board)
                #print("Es jugada valida: ?",jugadaValida)
                if(jugadaValida): #valida si jugadaValida es true
                    player.firstMove=False
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



    

