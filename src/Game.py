from board import Board
from player import Player
import copy
from MinimaxSolver import MinimaxSolver

class Game:
    def __init__(self):
        self.round = True
        self.round_status = ''
        self.initialized_players = False
        self.listaJugadores = []
        # Para rastrear el turno actual del jugador, 0 para el primer jugador, 1 para el segundo
        self.current_turn = 0
        self.the_board = Board(16, 16)

        self.initialize_players()
        self.play_game()

    #  Configura los jugadores al comienzo del juego
    def initialize_players(self):
        print("\033c", end="")  # Esto limpia la consola
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
        self.initialized_players = True

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
        while self.has_players(): #  Mientras existan jugadores, el juego continúa
            if not self.initialized_players:
                self.the_board.print_map()
            self.initialized_players = True

            jugada_valida = False  # Variable de control
            player = self.current_player()  # Obtiene el jugador actual

            if player.canPlay:
                # Si el jugador es una IA, se crea un objeto llamado solver de tipo MinimaxSolver para este jugador
                if player.type == "IA":
                    print(f"\nEl jugador IA llamado {player.name}, está calculando su jugada...")
                    solver = MinimaxSolver(player.name)
                    # El jugador IA, usa Minimax para encontrar su mejor movimiento
                    best_move = solver.solve(self)
                    # Si encuentra un movimiento válido, coloca la pieza en el tablero
                    if best_move:
                        piece, position = best_move  # El mejor movimiento devuelve la pieza y la posición
                        self.the_board.place_piece(player.firstMove, piece, position[0], position[1])
                        player.firstMove = False  # Después del primer movimiento, esto será False
                # Si el jugador es humano, juega manualmente con el método definido para elegir y colocar su pieza
                else:
                    jugada_valida = player.pick_piece(self.the_board)
                    if jugada_valida:
                        player.firstMove = False
            # Cambia al siguiente jugador
            self.next_turn()
        # Muestra puntajes
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
        current_player = self.current_player()  # Obtén el jugador actual

        # Recorre todas las piezas disponibles del jugador actual
        for piece in current_player.pieces:
            for x in range(self.the_board.high):
                for y in range(self.the_board.width):
                    # Crea copias profundas del tablero y el jugador para mantener el estado inmutable
                    new_board = copy.deepcopy(self.the_board)
                    new_player = copy.deepcopy(current_player)

                    # Intenta colocar la pieza en la posición (x, y)
                    if new_board.can_place_piece(new_player.firstMove, piece, x, y):
                        new_board.place_piece(new_player.firstMove, piece, x, y)
                        new_player.firstMove = False  # Marca el primer movimiento como ya completado

                        # Crea un nuevo estado del juego y lo agrega a la lista de posibles estados
                        new_game_state = copy.deepcopy(self)
                        new_game_state.the_board = new_board
                        new_game_state.listaJugadores[self.current_turn] = new_player
                        possible_states.append(new_game_state)

        return possible_states

    #  Verifica si el juego ha terminado:
    #  Si ya no hay más movimientos posibles o si todos los jugadores se han rendido o ya no tienen piezas
    def is_terminal(self):
        # Verifica si todos los jugadores se rindieron o no pueden jugar más
        all_players_done = all(not player.canPlay for player in self.listaJugadores)
        if all_players_done:
            return True
        # Verifica si el tablero está completamente lleno
        for row in self.the_board.map:
            if '.' in row:  #  Si aún hay espacios vacíos, el tablero no está lleno
                return False

        # Si no se puede jugar más, retorna True
        return True

# Ejecuta el juego
if __name__ == "__main__": #  Solo se ejecuta cuando se corre el archivo
    game = Game()  # Instancia que ejecuta el constructor
    game.play_game()  #  Método que inicia el juego
