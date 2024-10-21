from board import Board
from player import Player
import copy
from MinimaxSolver import MinimaxSolver

class Game:
    def __init__(self):
        self.initialized_players = False
        self.listaJugadores = []
        # Para rastrear el turno actual del jugador, 0 para el primer jugador, 1 para el segundo
        self.all_players_done = 0
        self.current_turn = 0
        self.the_board = Board(16, 16)
        if not self.initialized_players:
            self.initialize_players()  # Solo inicializamos si no está inicializado
            self.initialized_players = True  # Marcamos como inicializados
        self.play_game()
        self.display_final_scores()

        #  Configura los jugadores al comienzo del juego

    def initialize_players(self):
        if self.initialized_players:
            return
        print("\033c", end="")
        while True:
            
            print('''
                            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                            ░░░░░░░░░░░░░░░░░░░-- BLOKUS --░░░░░░░░░░░░░░░░░░░░░░░
                            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                [1]: 2 jugadores   [2]: 4 jugadores
                    ''')

            option = input('\n\t:>')

            if self.debug_option(option):
                break
            else:
                continue
        
        option = int(option)

        if option == 1:
            option = 0

            name_player_1 = self.validate_name('Jugador_1')
            color_player_1 = 'Rojo'

            while True:
                print("\033c", end="")
                print(f'Jugador: {name_player_1}')
                type = input('''
                    Tipo de jugador. 
                    [1]: IA [2]: Humano
                :>''')

                if self.debug_option(type):
                    break

            type = int(type)

            if type == 1:
                player_1_type = 'IA'
            elif type == 2:
                player_1_type = 'Human'

            name_player_2 = self.validate_name('Jugador_2')
            color_player_2 = 'Azul'

            while True:
                print("\033c", end="")
                print(f'Jugador: {name_player_2}')
                type = input('''
                    Tipo de jugador. 
                    [1]: IA [2]: Humano
                :>''')

                if self.debug_option(type):
                    break

            type = int(type)

            if type == 1:
                player_2_type = 'IA'
            elif type == 2:
                player_2_type = 'Human'

            print("\033c", end="")

            player_1 = Player(1, name_player_1, color_player_1, player_type=player_1_type)
            player_2 = Player(2, name_player_2, color_player_2, player_type=player_2_type)

            self.listaJugadores = [player_1, player_2]

        if option == 2:
            option = 0

            name_player_1 = self.validate_name('Jugador_1')
            color_player_1 = 'Rojo'

            while True:
                print("\033c", end="")
                print(f'Jugador: {name_player_1}')
                type = input('''
                    Tipo de jugador. 
                    [1]: IA [2]: Humano
                :>''')

                if self.debug_option(type):
                    break

            type = int(type)

            if type == 1:
                player_1_type = 'IA'
            elif type == 2:
                player_1_type = 'Human'

            name_player_2 = self.validate_name('Jugador_2')
            color_player_2 = 'Amarillo'

            while True:
                print("\033c", end="")
                print(f'Jugador: {name_player_2}')
                type = input('''
                    Tipo de jugador. 
                    [1]: IA [2]: Humano
                :>''')

                if self.debug_option(type):
                    break

            type = int(type)

            if type == 1:
                player_2_type = 'IA'
            elif type == 2:
                player_2_type = 'Human'

            name_player_3 = self.validate_name('Jugador_3')
            color_player_3 = 'Azul'

            while True:
                print("\033c", end="")
                print(f'Jugador: {name_player_3}')
                type = input('''
                    Tipo de jugador. 
                    [1]: IA [2]: Humano
                :>''')

                if self.debug_option(type):
                    break

            type = int(type)

            if type == 1:
                player_3_type = 'IA'
            elif type == 2:
                player_3_type = 'Human'

            name_player_4 = self.validate_name('Jugador_4')
            color_player_4 = 'Verde'

            while True:
                print("\033c", end="")
                print(f'Jugador: {name_player_4}')
                type = input('''
                    Tipo de jugador. 
                    [1]: IA [2]: Humano
                :>''')

                if self.debug_option(type):
                    break

            type = int(type)

            if type == 1:
                player_4_type = 'IA'
            elif type == 2:
                player_4_type = 'Human'

            print("\033c", end="")
            print(f'Name: {name_player_1} type: {player_1_type}\nName: {name_player_2} type: {player_2_type}\nName: {name_player_3} type: {player_3_type}\nName: {name_player_4} type: {player_4_type}')
            input()

            player_1 = Player(1, name_player_1, color_player_1, player_type=player_1_type)
            player_2 = Player(2, name_player_2, color_player_2, player_type=player_2_type)
            player_3 = Player(3, name_player_3, color_player_3, player_type=player_3_type)
            player_4 = Player(4, name_player_4, color_player_4, player_type=player_4_type)

            self.listaJugadores = [player_1, player_2, player_3, player_4]

        self.initialized_players = True
    
    def debug_option(sef, option):

        if not option.isdigit():
                print("\033c", end="")
                print('\n\tSolo numeros, no letras. Intenta nuevamente.')
                return False
        option = int(option)
        if option < 1 or option > 2:
            print("\033c", end="")
            print('\n\tSolo numeros, de las opciones. Intenta nuevamente.')
            return False 
        else:
            return True

    
    def validate_name(self, text):
        while True:  # Bucle se ejecutará hasta que se ingresen nombres válidos
            name = input(f"\n\tNombre del {text}:>").strip()  # Elimina espacios
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

    # Verifica si al menos un jugador puede continuar jugando
    def has_players(self):
        #  Verifica cuales jugadores de la lista, tienen la propiedad "canPlay = True"
        return any(player.canPlay for player in self.listaJugadores)

    # Retorna el jugador del turno actual
    def current_player(self):
        return self.listaJugadores[self.current_turn]

    # Avanza al siguiente jugador que puede jugar, ignorando a los rendidos
    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.listaJugadores)
        while not self.listaJugadores[self.current_turn].canPlay:
            self.current_turn = (self.current_turn + 1) % len(self.listaJugadores)

    #  Bucle principal del juego
    def play_game(self):
        if self.all_players_done < 2:
            print("\033c", end="")
            self.the_board.print_map()

        while self.has_players():

            player = self.current_player()

            if player.canPlay:

                #print(f'AAA{self.current_turn}')
                # Si es IA

                if player.type == "IA":

                    print(f"\nEl jugador IA llamado {player.name}, está calculando su jugada...")
                    solver = MinimaxSolver(player.name)
                    best_move = solver.solve(self)

                    if best_move:

                        piece, position = best_move

                        if self.the_board.place_piece(player.firstMove, piece, position[0], position[1]):
                            player.point += piece.value # le sumamos los puntos a la IA
                            player.delete_ia_piece(piece) # Borramos la piesa colocada
                            player.firstMove = False
                            #print(f"\nPieza {piece.symbol} colocada por {player.name} en la posición {position}. + {piece.value} puntos sumados.")
                            self.the_board.print_map()
                            self.next_turn()

                        else:

                            print(f"Error: {player.name} no pudo colocar la pieza.")
                            player.canPlay = False

                    else:

                        print(f"{player.name} no tiene movimientos válidos.")
                        
                        self.all_players_done = self.all_players_done+1
                        #print(f'Valor de self.all_players_done = {self.all_players_done}')

                        player.canPlay = False

                # Si es Humano
                else:

                    jugada_valida = player.pick_piece(self.the_board)

                    if jugada_valida:

                        player.firstMove = False
                        self.the_board.print_map()
                        self.next_turn()
                    else:
                        player.canPlay = False  
            else:

                #print(f"{player.name} no puede jugar.")
                self.all_players_done = self.all_players_done+1
                #print(f'Valor de self.all_players_done = {self.all_players_done}')

                self.next_turn()
        #self.display_final_scores()  

    #  Muestra los puntajes finales de los jugadores y anuncia al ganador.
    def display_final_scores(self):
        print("\033", end="")

        for player in self.listaJugadores:
            # Si el jugador tiene piezas, obtener el símbolo de la primera pieza
            player_symbol = player.pieces[0].symbol if player.pieces else "N/A"
            print(f'Jugador: {player.name}, Tipo: {player.type}, Puntos: {player.point}, Símbolo de pieza: {player_symbol}')

        
        winner = max(self.listaJugadores, key=lambda x: x.point)
        print(f'\n {winner.name} HA GANADO!')
        print('''
            ░░░░░░░░░░░░░░░░░░  FELICIDADES  ░░░░░░░░░░░░░░░░░░░░░░
        ''')

    #   Genera todos los posibles estados de juego a partir de cada jugada válida.
    def children(self):
        possible_states = []
        current_player = self.current_player()

        if len(current_player.pieces) == 0:  # Si no quedan piezas, no genera estados
            return possible_states

        contador_estados = 0  # Contador para medir los estados generados

        for piece in current_player.pieces:
            for x in range(self.the_board.high):
                for y in range(self.the_board.width):
                    # Intenta colocar la pieza en todas las posiciones posibles del tablero
                    if self.the_board.can_place_piece(current_player.firstMove, piece, x, y):
                        new_board = Board(self.the_board.width, self.the_board.high)
                        new_board.map = [row[:] for row in self.the_board.map]

                        new_player = copy.deepcopy(current_player)
                        new_board.place_piece(new_player.firstMove, piece, x, y)
                        new_player.firstMove = False  # Marcamos que ya no es la primera jugada

                        # Crea el nuevo estado del juego
                        new_game_state = Game.__new__(Game)
                        new_game_state.the_board = new_board
                        new_game_state.listaJugadores = self.listaJugadores.copy()
                        new_game_state.listaJugadores[self.current_turn] = new_player
                        new_game_state.current_turn = (self.current_turn + 1) % len(self.listaJugadores)
                        move = (piece, (x, y))

                        # Agrega el nuevo estado a la lista de posibles estados
                        possible_states.append((move, new_game_state))

                        contador_estados += 1  # Incrementa el contador

        #print(f"Estados generados: {contador_estados}")
        return possible_states[:1000]  # Limitar la generación de estados a 100 si es necesario

    #  Verifica si el juego ha terminado:
    #  Si ya no hay más movimientos posibles o si todos los jugadores se han rendido o ya no tienen piezas
    def is_terminal(self):
        # Verifica si todos los jugadores ya no pueden jugar más (rendidos o sin piezas válidas)
        all_players_done = all(not player.canPlay or len(player.pieces) == 0 for player in self.listaJugadores)

        if all_players_done:
            return True  # Si todos los jugadores han terminado

        # Verifica si aún hay espacios vacíos en el tablero (esto evita el final antes de tiempo)
        for row in self.the_board.map:
            if '.' in row:
                return False

        return True


# Ejecuta el juego
if __name__ == "__main__": #  Solo se ejecuta cuando se corre el archivo
    game = Game()  # Instancia que ejecuta el constructor
    game.play_game()  #  Método que inicia el juego
