from board import Board
from player import Player
round = True
round_status = ''
initialized_players = False
name_player_1 = ''
name_player_2 = ''
color_player_1 = ''
color_player_2 = ''


the_board = Board(16, 16)



while round == True:

    if initialized_players == False:

        print("\033c", end="")

        print('𝔅𝔩𝔬𝔨𝔲𝔰')

        print('\n\n𝓟𝓵𝓪𝔂 : 1')

        print('\n\𝓔𝔁𝓲𝓽 : 2')

        round_status = input('\n:>')
        initialized_players = False


    if round_status == '1':

        
        print('\nRonda iniciada.')

        if initialized_players == False:
            name_player_1 = input('\nNombre del primer jugador:>')
            color_player_1 = input('\nColor del primer jugador:>')

            name_player_2 = input('\nNombre del segundo jugador:>')
            color_player_2 = input('\nColor del segundo jugador:>')
            player_1 = Player(1, name_player_1, color_player_2 )
            player_2 = Player(2, name_player_2, color_player_2 )
            initialized_players = True

        player_1.place_player_piece(the_board)
        player_2.place_player_piece(the_board)
        

    elif round_status == '2':

        print("\033c", end="")

        round = False
