from piece import Piece
from board import Board

# Regla de Blokus: Cada jugador debe empezar con 21 piezas
class Player:

    # Método constructor de la clase Player con sus atributos
    def __init__(self, player_id, name, color):
        self.player_id = player_id
        self.name = name
        self.color = color
        self.pieces = Piece.generar_piezas_random(color)

    # Muestra las piezas del jugador horizontalmente, alineadas
    def mostrar_piezas_jugador(self):
        max_altura = max(len(pieza.shape) for pieza in self.pieces)

        # Para cada fila de cada pieza
        for i in range(max_altura):
            for pieza in self.pieces:
                if i < len(pieza.shape):
                    print(' '.join(map(str, pieza.shape[i])), end='    ')  # Imprimime cada fila
                else:
                    # Si la pieza no tiene más filas, imprime espacios vacíos para mantener el espacio
                    print(' ' * len(' '.join(map(str, pieza.shape[0]))), end='    ')
            print()  # Salto de línea después de cada fila de todas las piezas

    # Permite al jugador seleccionar una de sus piezas
    def seleccionar_pieza(self):
        print(f"[{self.name}], estas son tus piezas disponibles (numeradas de izquierda a derecha, del 1 al 21): \n")

        self.mostrar_piezas_jugador()

        # Elegir una pieza por número (se le resta 1 para usar como índice)
        seleccion = int(input("Escribe aquí el número de la pieza que deseas utilizar: ")) - 1
        return self.pieces[seleccion]

    # Permite al jugador colocar la pieza seleccionada en el tablero
    def colocar_pieza(self, tablero):
        pieza_seleccionada = self.seleccionar_pieza()
        pos_x = int(input(f"Ingresa el num. de fila: "))
        pos_y = int(input(f"Ingrese el num. de columna: "))

        # Coloca la pieza en el tablero usando el método place_piece de Board
        tablero.place_piece(pieza_seleccionada, pos_x, pos_y)

        # Elimina la pieza que el jugador utilizó, de su lista de piezas disponibles
        self.pieces.remove(pieza_seleccionada)

        # Muestra el tablero con la pieza colocada
        tablero.print_map()

#  Cada vez que se instancia un jugador, este viene ya con su lista de 21 piezas
amelia = Player(1, "Amelia", "Blue")

# amelia.mostrar_piezas_jugador()
