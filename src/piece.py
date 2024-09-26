class Piece:
    def __init__(self, shape,symbol, id_pieza, color, valor, orientacion, coordenada=None): #Aqui agrega mas propiedades para las piezas
        """
        Inicializa los atributos de la pieza.

        :param forma: Matriz 2D que representa la disposición de los bloques.
        :param id_pieza: Identificador de la pieza.
        :param color: Color de la pieza.
        :param valor: Valor de la pieza.
        :param orientacion: Orientación de la pieza.
        :param coordenada: Ubicación en el tablero, puede ser None.
        """
        self.shape = shape #Utilizamos este parametro como una lista para darle la forma a la pieza 
        self.symbol = symbol
        self.id_pieza = id_pieza
        self.color = color #Este parametro es para definir la froma pero lo utilizare depues para dale el color
        self.valor = valor
        self.orientacion = orientacion
        self.coordenada = coordenada

    def rotar(self):
        """Rota la pieza 90 grados en sentido horario."""
        self.forma = [list(row) for row in zip(*self.forma[::-1])]
        self.orientacion = (self.orientacion + 90) % 360  # Actualiza la orientación

    def reflejar(self, horizontal=True):
        """Refleja la pieza horizontal o verticalmente.

        :param horizontal: Si es True, refleja horizontalmente; de lo contrario, refleja verticalmente.
        """
        if horizontal:
            self.forma = [row[::-1] for row in self.forma]  # Reflejar horizontalmente
        else:
            self.forma.reverse()  # Reflejar verticalmente

    def mostrar_pieza(self):
        """Imprime la pieza en la consola."""
        for fila in self.forma:
            print(' '.join(fila))
        print(f"ID: {self.id_pieza}, Color: {self.color}, Valor: {self.valor}, Orientación: {self.orientacion}°")

# Ejemplo de uso
piece = Piece(
    forma=[['#', '#', '#'], [' ', '#', ' '], [' ', '#', ' ']],
    id_pieza=1,
    color='rojo',
    valor=10,
    orientacion=0
)

print("Pieza original:")
piece.mostrar_pieza()

piece.rotar()
print("\nPieza después de rotar:")
piece.mostrar_pieza()

piece.reflejar(horizontal=True)
print("\nPieza después de reflejar horizontalmente:")
piece.mostrar_pieza()