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

    # Metodo para validar que no se superpongan las piezas
    def can_place_piece(self, playerFirstMove, piece, positionX, positionY):
        """ Verifica si la pieza se puede colocar en la posición dada sin colisionar con otras piezas """
        anyInCorner = 0  # Variable para validar si hay algún valor en las esquinas
        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if piece.shape[i][j] != '.':  # Solo verifica si es parte de la pieza
                    # Verifica si la posición está dentro de los límites del tablero
                    if 0 <= positionX + i < self.high and 0 <= positionY + j < self.width:
                        # Si la posición ya está ocupada, no se puede colocar la pieza
                        if self.map[positionX + i][positionY + j] != '.':
                            return False  # No se puede colocar la pieza porque colisionaría

                        # Verificaciones de posiciones adyacentes (asegura que estén dentro de los límites)
                        # Izquierda
                        if positionY + j - 1 >= 0 and self.map[positionX + i][positionY + j - 1] == piece.symbol:
                            return False
                        # Derecha
                        if positionY + j + 1 < self.width and self.map[positionX + i][positionY + j + 1] == piece.symbol:
                            return False
                        # Arriba
                        if positionX + i - 1 >= 0 and self.map[positionX + i - 1][positionY + j] == piece.symbol:
                            return False
                        # Abajo
                        if positionX + i + 1 < self.high and self.map[positionX + i + 1][positionY + j] == piece.symbol:
                            return False

                        # Validación de esquinas
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
        if not playerFirstMove and anyInCorner == 0:
            return False  # No hay ninguna esquina tocando
        return True

    #  Muestra la pieza colocada en el tablero y retorna una copia del tablero actual, si es posible
    def place_piece(self, playerFirstMove, piece, positionInX, positionInY):
        # Este metodo coloca una pieza en el tablero en la posicion x,y
        if self.can_place_piece(playerFirstMove, piece, positionInX, positionInY):
            for i in range(len(piece.shape)):  # Recorremos las filas de la pieza.
                for j in range(len(piece.shape[i])):  # Recorremos las columnas de cada fila de la pieza.
                    if piece.shape[i][j] != '.':  # Solo colocamos si validamos que hay un espacio en blanco en la forma.
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
    score += remaining_pieces_penalty
    return score

