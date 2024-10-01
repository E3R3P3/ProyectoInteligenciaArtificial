#from piece import Piece
class Board:
    # Constructor de la clase que recibe el alto y ancho del trablero
    def __init__(self, width, high):
        self.width = width
        self.high = high
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

    def place_piece(self, piece, positionInX, positionInY):
        # Este metodo coloca una pieza en el tablero en la posicion x,y
        print(f"Intentando colocar la pieza en {positionInX}, {positionInY}")  # Debug (prueba)
        for i in range(len(piece.shape)):  # Recorre las filas de la pieza.
            for j in range(len(piece.shape[i])):  # Recorre las columnas de cada fila de la pieza.
                if piece.shape[i][j] != ' ':  # Solo coloca si hay un símbolo en la forma.
                    if 0 <= positionInX + i < self.high and 0 <= positionInY + j < self.width:  #  Verifica que la posicion de la pieza esté dentro de los límites.
                        print(f"Colocando parte de la pieza en {positionInX + i}, {positionInY + j}")  # Debug (prueba)
                        self.map[positionInX + i][
                            positionInY + j] = piece.symbol  # Coloca el simbolo de la pieza en el mapa.
                    else:
                        print("Pieza fuera de los límites")
                        return

   
