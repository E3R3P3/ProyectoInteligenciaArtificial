from board import Board
from player import Player
import copy
from MinimaxSolver import MinimaxSolver

class Game:
    def __init__(self):
        self.initialized_players = False
        self.listaJugadores = []
        # Para rastrear el turno actual del jugador, 0 para el primer jugador, 1 para el segundo
        self.current_turn = 0
        self.the_board = Board(16, 16)
        if not self.initialized_players:
            self.initialize_players()  # Solo inicializamos si no está inicializado
            self.initialized_players = True  # Marcamos como inicializados
        self.play_game()

        #  Configura los jugadores al comienzo del juego

    def initialize_players(self):
        if self.initialized_players:
            return

        print("\033c", end="")  # Esto limpia la consola solo la primera vez
        print('''
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░░░░░░░░░░░░░░░-- BLOKUS --░░░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ''')

        name_player_1 = self.validate_name('Jugador_1')
        color_player_1 = 'Rojo'

        name_player_2 = self.validate_name('Jugador_2')
        color_player_2 = 'Azul'

        print("\033c", end="")
        player_1 = Player(1, name_player_1, color_player_1, player_type="Human")
        player_2 = Player(2, name_player_2, color_player_2, player_type="IA")

        self.listaJugadores = [player_1, player_2]
        self.initialized_players = True  # Asegura que ya fueron inicializados los jugadores

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
        self.the_board.print_map()
        while self.has_players():
            player = self.current_player()

            if self.is_terminal():
                print("\nEl juego ha terminado. No hay más movimientos posibles.")
                break

            if player.canPlay:
                if player.type == "IA":
                    print(f"\nEl jugador IA llamado {player.name}, está calculando su jugada...")
                    solver = MinimaxSolver(player.name)
                    best_move = solver.solve(self)
                    if best_move:
                        piece, position = best_move
                        if self.the_board.place_piece(player.firstMove, piece, position[0], position[1]):
                            player.firstMove = False
                            print(f"\nPieza {piece.symbol} colocada por {player.name} en la posición {position}.")
                        else:
                            print(f"Error: {player.name} no pudo colocar la pieza.")
                    else:
                        print(f"{player.name} no tiene movimientos válidos.")
                else:
                    jugada_valida = player.pick_piece(self.the_board)
                    if jugada_valida:
                        player.firstMove = False

                self.the_board.print_map()
                self.next_turn()
            else:
                print(f"{player.name} no puede jugar.")
                self.next_turn()
        self.display_final_scores()

    #  Muestra los puntajes finales de los jugadores y anuncia al ganador.
    def display_final_scores(self):
            print("\033", end="")
            for player in self.listaJugadores:
                print(f'\nPuntos de {player.name}: {player.point}')
            winner = max(self.listaJugadores, key=lambda x: x.point)
            print(f'\n {winner.name} HA GANADO!')
            print('''
                    ░░░░░░░░░░░░░░░░░░  FELICIDADES  ░░░░░░░░░░░░░░░░░░░░░░
            ''')

    #   Genera todos los posibles estados futuros del juego a partir de cada jugada posible del jugador actual.
    def children(self):
        possible_states = []
        current_player = self.current_player()

        if len(current_player.pieces) == 0:  # Si no quedan piezas, no genera estados
            return possible_states

        for piece in current_player.pieces:
            for x in range(self.the_board.high):
                for y in range(self.the_board.width):
                    if self.the_board.can_place_piece(current_player.firstMove, piece, x, y):
                        new_board = Board(self.the_board.width, self.the_board.high)
                        new_board.map = [row[:] for row in self.the_board.map]

                        new_player = copy.deepcopy(current_player)
                        new_board.place_piece(new_player.firstMove, piece, x, y)
                        new_player.firstMove = False

                        new_game_state = Game.__new__(Game)
                        new_game_state.the_board = new_board
                        new_game_state.listaJugadores = self.listaJugadores.copy()
                        new_game_state.listaJugadores[self.current_turn] = new_player
                        new_game_state.current_turn = (self.current_turn + 1) % len(self.listaJugadores)
                        new_board.print_map()
                        move = (piece, (x, y))
                        possible_states.append((move, new_game_state))

        return possible_states

    #  Verifica si el juego ha terminado:
    #  Si ya no hay más movimientos posibles o si todos los jugadores se han rendido o ya no tienen piezas
    def is_terminal(self):
        all_players_done = all(not player.canPlay or len(player.pieces) == 0 for player in self.listaJugadores)
        if all_players_done:
            return True

        for row in self.the_board.map:
            if '.' in row:  # Si aún hay espacios vacíos, el tablero no está lleno
                return False

        return True


# Ejecuta el juego
if __name__ == "__main__": #  Solo se ejecuta cuando se corre el archivo
    game = Game()  # Instancia que ejecuta el constructor
    game.play_game()  #  Método que inicia el juego
