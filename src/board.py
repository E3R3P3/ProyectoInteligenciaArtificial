#from piece import Piece
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
    def can_place_piece(self,playerFirstMove, piece, positionInX, positionInY):
        anyInConer = 0 #variable para validar si hay algun valor en las esquinas
        """ Verifica si la pieza se puede colocar en la posición dada sin colisionar con otras piezas """
        for i in range(len(piece.shape)):  # Recorremos las filas de la pieza.
            for j in range(len(piece.shape[i])):  # Recorremos las columnas de cada fila de la pieza.
                if piece.shape[i][j] != ' ':  # Solo verificamos si no es un espacio vacío en la forma.
                    # Verificamos si la posición de la pieza está dentro de los límites del tablero.
                    if 0 <= positionInX + i < self.high and 0 <= positionInY + j < self.width:
                        # Si la posición ya está ocupada por una pieza diferente de "." (espacio vacío en el tablero)
                        if self.map[positionInX + i][positionInY + j] != '.':
                            return False  # No se puede colocar la pieza porque colisionaría
                        
                        # Verificamos las posiciones adyacentes para evitar piezas similares
                        # # Izquierda
                        if self.map[positionInX + i][positionInY + j - 1] == piece.symbol:
                            return False
                        # # Derecha
                        if self.map[positionInX + i][positionInY + j + 1] == piece.symbol:
                            return False
                        # # Arriba
                        if self.map[positionInX + i - 1][positionInY + j] == piece.symbol:
                            return False
                        # # Abajo
                        if self.map[positionInX + i + 1][positionInY + j] == piece.symbol:
                            return False
                        
                        #valores para saber si es el primer turno
                        #print(f"Es primera jugada?: {playerFirstMove}")
                        if playerFirstMove == False:
                            # Validar Esquina Superior Izquierda
                            '''print("Entrada al validar las esquinas")
                            print("pieza del usuario" + piece.symbol)
                            print(self.map[positionInX + i - 1][positionInY + j - 1])'''
                            if self.map[positionInX + i - 1][positionInY + j - 1] == piece.symbol:
                                #print('Esquina Superior Izquierda')
                                anyInConer+=1
                            if self.map[positionInX + i - 1][positionInY + j + 1] == piece.symbol:
                                #print('Esquina Superior derecha')
                                anyInConer+=1
                            if self.map[positionInX + i + 1][positionInY + j - 1] == piece.symbol:
                                #print('Esquina inferior izquierda')
                                anyInConer+=1
                            if self.map[positionInX + i + 1][positionInY + j + 1] == piece.symbol:
                                #print('Esquina inferior derecha')
                                anyInConer+=1

                    else:
                        return False  # Está fuera de los límites del tablero
        if playerFirstMove == False:
            if anyInConer == 0:
                anyInConer=0
                return False 
            else:
                return True
        else:
            return True

    def place_piece(self,playerFirstMove, piece, positionInX, positionInY): # Este metodo coloca una pieza en el tablero en la posicion x,y
        if self.can_place_piece(playerFirstMove,piece,positionInX,positionInY):
            for i in range(len(piece.shape)): # Recorremos las filas de la pieza.

                for j in range(len(piece.shape[i])):  # Recorremos las columnas de cada fila de la pieza.

                    if piece.shape[i][j] != ' ':  # Solo colocamos si validamos que hay un espacio en blanco en la forma.

                        if 0 <= positionInX + i < self.high and 0 <= positionInY + j < self.width: # Verificamos que la posicion de la pieza a dentro de los limites.
                            # if ferst_play == 1: 
                            #     self.ferst_play_1 = False
                            # elif ferst_play == 2:
                            #     self.ferst_play_2 = False
                            self.map[positionInX + i][positionInY + j] = piece.symbol # Colocamos el simbolo de la pieza en el mapa.
                            self.possible = True
                        else:

                            print("Pieza fuera de los limites")
                            self.possible = False
                            return
            print("Pieza colocada exitosamente.")
            return True #Retornamos este valor para saber si se pudo posicionar
        else:
            self.possible = False
            print("Error: No puedes colocar la pieza, está colisionando con otra o está fuera de los límites.")

