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

        self.time_start = time.time()  # Guarda el momento en que se empezó a buscar la jugada
        self.max_time = max_time  # Guarda el tiempo máximo permitido para la búsqueda Minimax, configurado para 2 segs
        best_move = None  # Almacenará el mejor movimiento que se encuentre durante la búsqueda
        best_score = float('-inf')  # Inicializa con el puntaje más bajo posible

        # Búsqueda iterativa en profundidad, hasta 100 que es un valor arbitrario
        for depth in range(1, 100):
            try:
                move, score = self._maximize(game, float('-inf'), float('inf'), depth)
                if score > best_score:
                    best_move = move
                    best_score = score
            except TimeoutError:
                break  # Termina si se acaban los 2 segs

        return best_move

    # Busca maximizar el puntaje de la IA explorando todos los posibles movimientos. Con alfa-beta para optimizar la búsqueda.
    def _maximize(self, game, alpha, beta, depth):
        # Verifica si el tiempo límite se ha acabado
        if time.time() - self.time_start > self.max_time:
            raise TimeoutError("Tiempo agotado para Minimax")

        # Si se llega a la profundidad máxima o el juego termina, se retorna la heurística del estado actual
        if depth == 0 or game.is_terminal():
            return None, game.evaluate_heuristic(self.player_name)

        # En maximize(), estamos buscando el puntaje más alto posible para la IA.
        # Por eso inicializamos max_score en menos infinito (float('-inf')),
        # para asegurarnos de que cualquier puntaje encontrado será mayor.
        max_score = float('-inf')
        best_move = None

        # Genera todos los posibles movimientos del jugador actual
        for move, new_state in game.children(self.player_name):
            # Se llama a minimize() para evaluar el estado después del movimiento del oponente, con una profundidad menos
            _, score = self._minimize(new_state, alpha, beta, depth - 1)
            if score > max_score:  # Si el puntaje encontrado es mejor que el puntaje actual, lo actualizamos
                max_score = score
                best_move = move

            # Poda alfa-beta: Técnica de la IA para evitar movimientos inútiles
            alpha = max(alpha, max_score)  # Se actualiza con el mejor puntaje encontrado hasta ahora por la IA
            if alpha >= beta:  # Si la IA encuentra un puntaje tan bueno, dejará de buscar más movimientos
                break  # Aquí se detiene la búsqueda en la rama actual

        # Devuelve el mejor movimiento encontrado y su puntaje
        return best_move, max_score

    # Busca el mejor movimiento para el oponente (el jugador que intenta minimizar el puntaje de la IA).
    def _minimize(self, game, alpha, beta, depth):
        if time.time() - self.time_start > self.max_time:
            raise TimeoutError("Tiempo agotado para Minimax")

        if depth == 0 or game.is_terminal():
            return None, game.evaluate_heuristic(self.player_name)

        # Peor puntaje posible para el oponente IA
        # En minimize(), simulamos el turno del oponente que intenta minimizar el puntaje.
        # Por eso inicializamos min_score en más infinito (float('inf')),
        # para asegurarnos de que cualquier puntaje encontrado será menor.
        min_score = float('inf')
        best_move = None

        # Genera todos los posibles movimientos del oponente
        for move, new_state in game.children(game.get_opponent_name(self.player_name)):
            # Llama a maximize() para evaluar lo que haría la IA en respuesta al oponente con una profundidad menos
            _, score = self._maximize(new_state, alpha, beta, depth - 1)
            if score < min_score:
                min_score = score
                best_move = move

            # Poda alfa-beta
            beta = min(beta, min_score)
            if alpha >= beta:
                break

        # Devuelve el mejor movimiento del oponente y su puntaje
        return best_move, min_score
