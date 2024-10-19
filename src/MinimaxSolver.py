import time
import copy

""" 
    OBJETIVOS:
    - Explorar posibles movimientos
    - Evaluar el estado del tablero usando la función heuristic(), de la clase board
    - Encontrar la mejor jugada de la AI en cada turno
"""


class MinimaxSolver:

    def __init__(self, player_name):
        self.player_name = player_name
        self.time_start = None
        self.max_time = None

    #  Inicia la búsqueda Minimax con podado alfa-beta para encontrar el mejor movimiento posible.
    def solve(self, game, max_time=2):
        self.time_start = time.time()
        self.max_time = max_time
        best_move = None
        best_score = float('-inf')

        # Limita la profundidad para evitar bucles infinitos
        max_depth = 4

        for depth in range(1, max_depth + 1):  # Limita la búsqueda a una profundidad máxima de 4
            try:
                move, score = self._maximize(game, float('-inf'), float('inf'), depth)
                if score > best_score:
                    best_move = move
                    best_score = score
            except TimeoutError:
                break

        return best_move

    # Busca maximizar el puntaje de la IA explorando todos los posibles movimientos. Con alfa-beta para optimizar la búsqueda.
    def _maximize(self, game, alpha, beta, depth):
        # Verifica si el tiempo límite se ha agotado
        if time.time() - self.time_start > self.max_time:
            raise TimeoutError("Tiempo agotado para Minimax")

        # Si llega a la profundidad máxima o el juego termina, retorna la heurística del estado actual
        if depth == 0 or game.is_terminal():
            # Aquí llamamos a la heurística desde el tablero
            return None, game.the_board.heuristic(game.current_player())

        max_score = float('-inf')
        best_move = None

        for move, new_state in game.children():
            _, score = self._minimize(new_state, alpha, beta, depth - 1)
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break
        return best_move, max_score

    # Busca el mejor movimiento para el oponente (el jugador que intenta minimizar el puntaje de la IA).
    def _minimize(self, game, alpha, beta, depth):
        if time.time() - self.time_start > self.max_time:
            raise TimeoutError("Tiempo agotado para Minimax")

        if depth == 0 or game.is_terminal():
            # Aquí llamamos a la heurística desde el tablero
            return None, game.the_board.heuristic(game.current_player())

        # Peor puntaje posible para el oponente IA
        # En minimize(), simulamos el turno del oponente que intenta minimizar el puntaje.
        # Por eso inicializamos min_score en más infinito (float('inf')),
        # para asegurarnos de que cualquier puntaje encontrado será menor.
        min_score = float('inf')
        best_move = None

        for move, new_state in game.children():
            _, score = self._maximize(new_state, alpha, beta, depth - 1)
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, min_score)
            if alpha >= beta:
                break
        return best_move, min_score
