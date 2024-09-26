#from piece import Piece
class Board:
    # Constructor de la clase que recibe el alto y ancho del trablero
    def __init__(self,width,high):
        self.width = width
        self.high = high
        # Aqui creamos la matriz del mapa con las dimenciones pasadas y los llenamos con "-" para que se pueda ver el mapa
        self.map = [['-' for _ in range(width)] for _ in range(high)]

    def print_map(self):
        # Con un for recorremos la matriz para ver el mapa
        for row in self.map:
            # Le agregamos espacio entre colubnas para que se vea mejor
            print(' '.join(row))

    def place_piece(self,piece,positionInX,positionInY):# Este metodo coloca una pieza en el tablero en la posicion x,y

        for i in range(len(piece.shape)):# Recorremos las filas de la pieza.

            for j in range(len(piece.shape[i])): # Recorremos las columnas de cada fila de la pieza.

                if piece.shape[i][j] == 1: # Solo colocamos  validamos que hay un 1 en la forma.

                    if 0 <= positionInX + i < self.high and 0 <= positionInY + j < self.width: # Verificamos que la posicion de la pieza a dentro de los limites.

                        self.map[positionInX + i][positionInY + j] = piece.symbol # Colocamos el simbolo de la pieza en el mapa.

                    else:

                        print("Pieza fuera de los limites")

                        return