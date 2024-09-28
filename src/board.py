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

    def place_piece(self, piece, positionInX, positionInY):# Este metodo coloca una pieza en el tablero en la posicion x,y

        for i in range(len(piece.shape)):# Recorremos las filas de la pieza.

            for j in range(len(piece.shape[i])): # Recorremos las columnas de cada fila de la pieza.

                if piece.shape[i][j] != '': # Solo colocamos si validamos que hay un espacio en blanco en la forma.

                    if 0 <= positionInX + i < self.high and 0 <= positionInY + j < self.width: # Verificamos que la posicion de la pieza a dentro de los limites.

                        self.map[positionInX + i][positionInY + j] = piece.symbol # Colocamos el simbolo de la pieza en el mapa.

                    else:

                        print("Pieza fuera de los limites")

                        return