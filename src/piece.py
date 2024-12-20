import random


class Piece:
    def __init__(self, shape, symbol, piece_id, color, value, orientation, coordinates=None):  # Aqui agrega mas propiedades para las piezas
        self.shape = shape  # Utilizamos este parametro como una lista para darle la forma a la pieza
        self.symbol = symbol
        self.piece_id = piece_id
        self.color = color  # Este parametro es para definir la froma pero lo utilizare depues para dale el color
        self.value = value
        self.orientation = orientation
        self.coordinates = coordinates

    # Rota la pieza 90 grados en sentido horario: para uso futuro
    # def rotate(self):
    #     self.shape = [list(row) for row in zip(*self.shape[::-1])]
    #     # Actualiza la orientación
    #     self.orientation = (self.orientation + 90) % 360

    # Refleja la pieza pieza horizontal o verticalmente: para uso futuro
    # def reflect(self, horizontal=True):
    #     # Si es True, refleja horizontalmente; de lo contrario, refleja verticalmente.
    #     if horizontal:
    #         self.shape = [row[::-1] for row in self.shape]  # reflect horizontalmente
    #     else:
    #         self.shape.reverse()  # reflect verticalmente

    #Imprime la pieza en la consola.
    def show_piece(self):

        for fila in self.shape:

            print(' '.join(fila))

        #print(f"ID: {self.piece_id}, Color: {self.color}, value: {self.value}, Orientación: {self.orientation}°")

    # Método para generar 21 piezas aleatorias. Devuelve una lista de objetos tipo Piece
    @classmethod
    def generate_random_pieces(cls, color):

        pieceValues = [1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

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
            [[' ', '#'], ['#', '#'], ['#', ' '], ['#', ' ']],  # N
            [['#', '#'], ['#', '#'], ['#', ' ']],  # P
            [['#', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],  # T 3x3
            [['#', ' ', ' '], ['#', '#', '#'], [' ', ' ', '#']],  # U
            [[' ', ' ', '#'], [' ', ' ', '#'], ['#', '#', '#']],  # L al revés
            [[' ', ' ', '#'], [' ', '#', '#'], ['#', '#', ' ']],  # w
            [['#', ' ', ' '], ['#', '#', '#'], [' ', '#', ' ']],  # Cruz 3x3
            [[' ', '#'], ['#', '#'], [' ', '#'], [' ', '#']],  # Z y
            [['#', '#'], [' ', '#'], ['#', '#']],  # Z 3x4
        ]

        pieces = []

        symbols = {'Rojo': '#', 'Azul': '@', 'Amarillo': '$', 'Verde': 'Ñ'}

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
