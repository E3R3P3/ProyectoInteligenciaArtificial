# from piece import Piece
class Board:
    # Constructor de la clase que recibe el alto y ancho del trablero
    def __init__(self, width, high):
        self.width = width
        self.high = high
        self.possible = True
        # Aqui creamos la matriz del mapa con las dimensiones pasadas y los llenamos con "." para que se pueda ver el mapa
        self.map = [['.' for _ in range(width)] for _ in range(high)]

    def print_map(self):
        # Numera y crea las columnas
        header = "   " + "  ".join([f"{i + 0:2}" for i in range(self.width)])
        print(header)

        # Numera y crea las filas
        for idx in range(self.high):
            row = f"{idx + 0:2}  " + "   ".join(self.map[idx])
            print(row)

    # def choca_con_misma_pieza(positionX,positionY,i,j,shape):

    # Metodo para validar que no se superpongan las piezas, equinas y 1era jugada
    def can_place_piece(self, playerFirstMove, piece, positionX, positionY):
        """ Verifica si la pieza se puede colocar en la posición dada sin colisionar con otras piezas """
        anyInCorner = 0  # Variable para validar si hay algún valor en las esquinas

        # Recorremos la forma de la pieza para verificar posición
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if piece.shape[i][j] != ' ':  # Solo verifica si es parte de la pieza

                    # Verifica si la posición está dentro de los límites del tablero
                    if 0 <= positionX + i < self.high and 0 <= positionY + j < self.width:
                        # Verificar colisiones con otras piezas
                        if self.map[positionX + i][positionY + j] != '.':
                            return False  # La posición ya está ocupada

                        # Verificaciones de posiciones adyacentes (izquierda, derecha, arriba, abajo)
                        if positionY + j - 1 >= 0 and self.map[positionX + i][positionY + j - 1] == piece.symbol:
                            return False  # Hay una pieza del mismo jugador a la izquierda
                        if positionY + j + 1 < self.width and self.map[positionX + i][
                            positionY + j + 1] == piece.symbol:
                            return False  # Hay una pieza del mismo jugador a la derecha
                        if positionX + i - 1 >= 0 and self.map[positionX + i - 1][positionY + j] == piece.symbol:
                            return False  # Hay una pieza del mismo jugador arriba
                        if positionX + i + 1 < self.high and self.map[positionX + i + 1][positionY + j] == piece.symbol:
                            return False  # Hay una pieza del mismo jugador abajo

                        # Validación de esquinas adyacentes si no es la primera jugada
                        if not playerFirstMove:
                            if positionX + i - 1 >= 0 and positionY + j - 1 >= 0 and \
                                    self.map[positionX + i - 1][positionY + j - 1] == piece.symbol:
                                anyInCorner += 1
                            if positionX + i - 1 >= 0 and positionY + j + 1 < self.width and \
                                    self.map[positionX + i - 1][positionY + j + 1] == piece.symbol:
                                anyInCorner += 1
                            if positionX + i + 1 < self.high and positionY + j - 1 >= 0 and \
                                    self.map[positionX + i + 1][positionY + j - 1] == piece.symbol:
                                anyInCorner += 1
                            if positionX + i + 1 < self.high and positionY + j + 1 < self.width and \
                                    self.map[positionX + i + 1][positionY + j + 1] == piece.symbol:
                                anyInCorner += 1
                    else:
                        return False  # Está fuera de los límites del tablero

        # Si no es la primera jugada, la pieza debe tocar una esquina
        if not playerFirstMove and anyInCorner == 0:
            return False  # No hay ninguna esquina tocando

        return True

    #  Muestra la pieza colocada en el tablero y retorna una copia del tablero actual, si es posible
    def place_piece(self, playerFirstMove, piece, positionInX, positionInY):
        # Este metodo coloca una pieza en el tablero en la posicion x,y
        if self.can_place_piece(playerFirstMove, piece, positionInX, positionInY):
            for i in range(len(piece.shape)):  # Recorremos las filas de la pieza.
                for j in range(len(piece.shape[i])):  # Recorremos las columnas de cada fila de la pieza.
                    if piece.shape[i][j] != ' ':  # Solo colocamos si validamos que hay un espacio en blanco en la forma.
                        self.map[positionInX + i][positionInY + j] = piece.symbol
            # print(f"Pieza {piece.symbol} colocada en el tablero.")
            return True
        else:
            print("Error: No puedes colocar la pieza, está colisionando con otra o está fuera de los límites.")
            return False

    #  Evalúa el estado del juego desde la perspectiva de un jugador, para guiar la toma de decisiones de la IA.
    def heuristic(self, player):
        score = player.point
        remaining_pieces_penalty = -len(player.pieces) * 5

        # Obtén el símbolo único de las piezas del jugador actual
        player_symbol = player.pieces[0].symbol  # Cada pieza tiene un símbolo diferente basado en el jugador

        # Más piezas en el tablero, mejor para la IA
        coverage_bonus = sum(row.count(player_symbol) for row in self.map) * 10

        #  Penalización por piezas grandes (piezas con un valor mayor a 3)
        big_piece_penalty = sum(piece.value for piece in player.pieces if piece.value > 3) * -2

        # Suma de todos los factores
        score += remaining_pieces_penalty + coverage_bonus + big_piece_penalty
        return score
