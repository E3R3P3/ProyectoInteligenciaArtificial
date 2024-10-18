import random

class Piece:
    def __init__(self, shape, symbol, piece_id, color, value, orientation,
                 coordinates=None):  # Aqui agrega mas propiedades para las piezas
        """
        Inicializa los atributos de la pieza.

        :param forma: Matriz 2D que representa la disposición de los bloques.
        :param piece_id: Identificador de la pieza.
        :param color: Color de la pieza.
        :param valor: Valor de la pieza.
        :param orientation: Orientación de la pieza.
        :param coordinates: Ubicación en el tablero, puede ser None.
        """
        self.shape = shape  # Utilizamos este parametro como una lista para darle la forma a la pieza
        self.symbol = symbol
        self.piece_id = piece_id
        self.color = color  # Este parametro es para definir la froma pero lo utilizare depues para dale el color
        self.value = value
        self.orientation = orientation
        self.coordinates = coordinates

    def rotate(self):
        """Rota la pieza 90 grados en sentido horario."""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.orientation = (self.orientation + 90) % 360  # Actualiza la orientación

    def reflect(self, horizontal=True):
        """Refleja la pieza horizontal o verticalmente.

        :param horizontal: Si es True, refleja horizontalmente; de lo contrario, refleja verticalmente.
        """
        if horizontal:
            self.shape = [row[::-1] for row in self.shape]  # reflect horizontalmente
        else:
            self.shape.reverse()  # reflect verticalmente

    def show_piece(self):
        """Imprime la pieza en la consola."""
        for fila in self.shape:
            print(' '.join(fila))
        print(f"ID: {self.piece_id}, Color: {self.color}, value: {self.value}, Orientación: {self.orientation}°")

    def available_pieces_for_positions(self,playerFirstMove, board):
        """
        Genera una lista de piezas que se pueden colocar en al menos una de las posiciones disponibles.
        """
        
        # Obtener todas las posiciones disponibles en el tablero para el símbolo del jugador
        available_positions = board.get_available_positions(self.symbol)
        valid_pieces = []  # Lista para almacenar las piezas que pueden ser colocadas

        # Probar si la pieza se puede colocar en alguna de las posiciones disponibles
        for pos in available_positions:
            # Si la pieza se puede colocar en la posición actual, agregarla a la lista de piezas válidas
            if board.can_place_piece(playerFirstMove, self, pos[0], pos[1]):
                valid_pieces.append(self.piece_id)
                break  # Salir del bucle si la pieza ya es válida para una posición
        print(valid_pieces) 
        return valid_pieces

    
    # Método para generar 21 piezas aleatorias. Devuelve una lista de objetos tipo Piece
    @classmethod
    
    def generate_random_pieces(cls, color):
        pieceValues=[1,2,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5]
        possible_shapes = [
            [['#']],  # 1
            [['#', '#']],  # 2
            [['#', '#'], [' ', '#']],  # 3
            [['#', '#', '#']],  # 3
            [['#', '#', '#', '#']],  # Barra
            [[' ', ' ', '#'], ['#', '#', '#']],  # Barra
            [['#', '#', ' '], [' ', '#', '#']],  # 4
            [['#', '#'], ['#', '#']],  # 4
            [['#', '#', '#'], [' ', '#', ' ']],  # T
            [[' ', '#', '#'], ['#', '#', ' '], [' ', '#', ' ']],  # F
            [['#', '#', '#', '#', '#']],  # Barra 5x1
            [['#', '#', '#', '#'], [' ', ' ', ' ', '#']],  # L grande 4x2
            [[' ', ' ', '#'], [' ', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],  # N
            [['#', '#'], ['#', '#'], ['#', ' ']],  # P
            [['#', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],  # T 3x3
            [['#', ' ', ' '], ['#', '#', '#'], [' ', ' ', '#']],  # U
            [[' ', ' ', '#'], [' ', ' ', '#'], ['#', '#', '#']],  # V
            [[' ', ' ', '#'], [' ', '#', '#'], ['#', '#', ' ']],  # w
            [['#', ' ', ' '], ['#', '#', '#'], [' ', '#', ' ']],  # Cruz 3x3
            [[' ', '#'], ['#', '#'], [' ', '#'], [' ', '#']],  # Z y
            [['#', '#'], [' ', '#'], ['#', '#']],  # Z 3x4
        ]
        pieces = []

        symbols = {'rojo' : '#' ,
                   'azul' : '@' ,
                   'amarillo' : 'T' ,
                   'verde' : 'L' ,
                   }
        
        # Llenará la lista anterior con 21 piezas
        for i in range(21):
            shape = possible_shapes[i]
            symbol = symbols[color]
            value = pieceValues[i]
            orientation = 0

            # Creación de una pieza
            piece = cls(shape, symbol, i + 1, color, value, orientation)

            # Agregando la pieza creada a la lista de piezas random
            pieces.append(piece)

        # Devuelve la lista con las 21 piezas
        return pieces

    
# Ejemplo de creación de un objeto Piece
# piece = Piece(
#     shape=[['#', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],
#     piece_id=1,
#     color='rojo',
#     value=10,
#     symbol="T",
#     orientation=0
# )
