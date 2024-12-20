import time
from datetime import datetime
import copy

class MinimaxSolver:

    def __init__(self, player_name):
        self.player_name = player_name
        self.time_start = None
        self.max_time = None
        self.max_depth = 0

    #  Inicia la búsqueda Minimax con podado alfa-beta para encontrar el mejor movimiento posible.
    def solve(self, game):

        self.time_start = time.time()  # devuelve un float: está expresado en segundos
        #self.max_time = max_time
        best_move = None
        best_score = float('-inf')

        # Limita la profundidad para evitar bucles infinitos
        _max_depth = 500 # se redujo de 4 a 3

        for depth in range(1, _max_depth + 1):  # Limita la búsqueda a una profundidad máxima de 4
            try:

                move, score = self._maximize(game, float('-inf'), float('inf'), depth)

                if score > best_score:

                    best_move = move
                    best_score = score

            except TimeoutError:

                print(f"Tiempo agotado mientras se analizaban jugadas a {depth} turnos a futuro. No se pudo continuar más allá por límite de tiempo.")
                
                break

        return best_move

    # Busca maximizar el puntaje de la IA explorando todos los posibles movimientos. Con alfa-beta para optimizar la búsqueda.
    def _maximize(self, game, alpha, beta, depth):

        contador_llamadas = 0  # Contador de llamadas

        # Verifica si el tiempo límite se ha agotado
        if time.time() - self.time_start > self.max_time:
            
            raise TimeoutError("Tiempo agotado para Minimax")

        # Si llega a la profundidad máxima o el juego termina, retorna la heurística del estado actual
        if depth == 0 or game.is_terminal():

            # Aquí llamamos a la heurística desde el tablero
            return None, game.the_board.heuristic(game.current_player())

        max_score = float('-inf')
        best_move = None
        max_local_depth = 0

        # Podado alpha - beta
        for move, new_state in sorted(game.children(),
                                      key=lambda state: game.the_board.heuristic(state[1].current_player()),
                                      reverse=True):  # Ordenamos los estados
            
            contador_llamadas += 1  # Incrementa el contador de llamadas

           
            _, score = self._minimize(new_state, alpha, beta, depth - 1) # Llamada recursiva a _minimize

            if score > max_score:

                max_score = score
                best_move = move

            alpha = max(alpha, max_score) #Evaluamos si max_score es mayor que alpha para en el caso reasignale su valor

            if depth >= max_local_depth: #Saeteamos el valor de la profundidad máxima para imprimirlo en el reporte

                max_local_depth = depth

                if max_local_depth >= self.max_depth:

                    self.max_depth = max_local_depth


            #print(f'Profundidad de #{self.max_depth}')

            if alpha >= beta: #Hacemos el podado

                print(f"Poda alfa-beta realizada en depth {depth}, Alpha: {alpha}, Beta: {beta}")

                break

        #print(f"Llamadas a _maximize: {contador_llamadas} en depth {depth}")
        return best_move, max_score

    # Busca el mejor movimiento para el oponente (el jugador que intenta minimizar el puntaje de la IA).
    def _minimize(self, game, alpha, beta, depth):

        contador_llamadas = 0  # Contador de llamadas

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

            contador_llamadas += 1  # Incrementa el contador de llamadas

            _, score = self._maximize(new_state, alpha, beta, depth - 1)

            if score < min_score:

                min_score = score
                best_move = move

            beta = min(beta, min_score) #Evaluamos si min_score es menor que beta para en el caso reasignale su valor

            if alpha >= beta:

                break
        
        return best_move, min_score
