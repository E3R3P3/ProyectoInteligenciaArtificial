import random

class Piece:
    def __init__(self, shape, symbol, id_pieza, color, valor, orientacion,
                 coordenada=None):  # Aqui agrega mas propiedades para las piezas
        """
        Inicializa los atributos de la pieza.

        :param forma: Matriz 2D que representa la disposición de los bloques.
        :param id_pieza: Identificador de la pieza.
        :param color: Color de la pieza.
        :param valor: Valor de la pieza.
        :param orientacion: Orientación de la pieza.
        :param coordenada: Ubicación en el tablero, puede ser None.
        """
        self.shape = shape  # Utilizamos este parametro como una lista para darle la forma a la pieza
        self.symbol = symbol
        self.id_pieza = id_pieza
        self.color = color  # Este parametro es para definir la froma pero lo utilizare depues para dale el color
        self.valor = valor
        self.orientacion = orientacion
        self.coordenada = coordenada

    def rotar(self):
        """Rota la pieza 90 grados en sentido horario."""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.orientacion = (self.orientacion + 90) % 360  # Actualiza la orientación

    def reflejar(self, horizontal=True):
        """Refleja la pieza horizontal o verticalmente.

        :param horizontal: Si es True, refleja horizontalmente; de lo contrario, refleja verticalmente.
        """
        if horizontal:
            self.shape = [row[::-1] for row in self.shape]  # Reflejar horizontalmente
        else:
            self.shape.reverse()  # Reflejar verticalmente

    def mostrar_pieza(self):
        """Imprime la pieza en la consola."""
        for fila in self.shape:
            print(' '.join(fila))
        print(f"ID: {self.id_pieza}, Color: {self.color}, Valor: {self.valor}, Orientación: {self.orientacion}°")

    # Método para generar 21 piezas aleatorias. Devuelve una lista de objetos tipo Piece
    @classmethod
    def generate_random_pieces(cls, color):
        possible_shapes = [
            [['#', '#'], ['#', '#']],  # Cuadrado 2 x 2
            [['#', '#', '#'], [' ', '#', ' ']],  # T
            [['#', ' '], ['#', ' '], ['#', '#']],  # L
            [['#', '#', '#', '#']],  # Barra
            [['#', '#'], [' ', '#'], [' ', '#']],  # S
            [['#']]  # Cuadrado 1x1
        ]
        pieces = []

        # Llenará la lista anterior con 21 piezas
        for i in range(21):
            shape = possible_shapes[i % len(possible_shapes)]
            symbol = random.choice(['#', 'L', 'T', '@'])
            valor = random.randint(1, 10)
            orientacion = 0

            # Creación de una pieza
            piece = cls(shape, symbol, i + 1, color, valor, orientacion)

            # Agregando la pieza creada a la lista de piezas random
            pieces.append(piece)

        # Devuelve la lista con las 21 piezas
        return pieces


# Ejemplo de creación de un objeto Piece
piece = Piece(
    shape=[['#', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],
    id_pieza=1,
    color='rojo',
    valor=10,
    symbol="T",
    orientacion=0
)

# Para probar los métodos de la clase Piece
# print("Pieza original:")
# piece.mostrar_pieza()
#
# piece.rotar()
# print("\nPieza después de rotar:")
# piece.mostrar_pieza()
#
# piece.reflejar(horizontal=True)
# print("\nPieza después de reflejar horizontalmente:")

# piece.mostrar_pieza()
# py piece.py para ejecutar
