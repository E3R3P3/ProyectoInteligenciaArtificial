from piece import Piece
from board import Board


# Regla de Blokus: Cada jugador debe empezar con 21 piezas
class Player:

    # Método constructor de la clase Player con sus atributos
    def __init__(self, player_id, name, color, player_type="Human"):
        self.player_id = player_id
        self.name = name
        self.color = color
        self.canPlay = True
        self.firstMove = True
        self.point = 0  # Contenemos los puntos aqui
        self.pieces = Piece.generate_random_pieces(color)
        self.type = player_type

    # Muestra las piezas del jugador horizontalmente, alineadas
    def show_player_pieces(self):
        # Determina la altura máxima de las piezas
        max_height = max(len(piece.shape) for piece in self.pieces)
        # Determina el ancho máximo de las piezas
        max_width = max(max(len(row) for row in piece.shape) for piece in self.pieces)
        # Para cada fila hasta la altura máxima
        for i in range(len(self.pieces)):
            print(f'[{i + 1}]', end='        ')
        print()
        for i in range(max_height):
            for piece in self.pieces:
                if i < len(piece.shape):
                    # Si la fila existe en la pieza, imprime la fila alineada con el ancho máximo
                    print(' '.join(piece.shape[i]).ljust(max_width * 2), end=' ')
                else:
                    # Si la pieza es más pequeña, imprime espacios vacíos para mantener el formato
                    print(' ' * (max_width * 2), end=' ')
            print()  # Nueva línea después de imprimir todas las piezas en esa fila

    #  Permite al jugador seleccionar una pieza. Retorna dicha pieza.
    def select_piece(self):
        print(f"\n {self.name}, estas son tus piezas disponibles (numeradas de izquierda a derecha, del 1 al 21):\n")
        self.show_player_pieces()

        while True:
            selection = input("Escribe el número de la pieza que deseas utilizar:> ")
            if selection.isdigit() and 1 <= int(selection) <= len(self.pieces):
                selection = int(selection) - 1
                self.pieces[selection].show_piece()
                return self.pieces[selection]
            print("\n\tIngresa un número válido. Intenta nuevamente.")

    def delete_ia_piece(self, piece):
        self.pieces.remove(piece)

    #  Permite al jugador colocar su pieza en el board.
    #  Lógica de colocación REAL
    def make_move(self, piece, board):
        while True:
            pos_x = input("Ingresa el número de fila:> ")
            pos_y = input("Ingresa el número de columna:> ")

            if pos_x.isdigit() and pos_y.isdigit():

                pos_x, pos_y = int(pos_x), int(pos_y)

                if 0 <= pos_x < board.high and 0 <= pos_y < board.width:

                    if board.can_place_piece(self.firstMove, piece, pos_x, pos_y):

                        board.place_piece(self.firstMove, piece, pos_x, pos_y)
                        self.firstMove = False
                        self.pieces.remove(piece)  # Remueve la pieza después de colocarla
                        self.point += piece.value

                        print(f"Pieza colocada en la posición ({pos_x}, {pos_y}). Tablero actualizado.")

                        return True
                    else:
                        print("En tu primera jugada, debes colocar la pieza en una esquina.")
                        
            print("Posición no válida. Intenta nuevamente.")

    #  Combina selección y colocación de la pieza para separar responsabilidades
    def pick_piece(self, board):
        print(f"\nTurno de: [{self.name}], de tipo: {self.type}")

        # Bucle hasta que el usuario ingrese una opción válida
        while True:
            select = input(f"\nElija la opción que desea realizar:\n[1] Elegir pieza\n[2] Rendirme\n:> ")

            if select == "2":  # Si elige rendirse
                self.canPlay = False
                return False

            if select == "1":  # Si elige colocar una pieza
                selected_piece = self.select_piece()  # Elige la pieza
                if self.make_move(selected_piece, board):  # Intenta colocarla en el tablero
                    print(f"Pieza colocada exitosamente. + {selected_piece.value} puntos sumados.")
                    return True
                else:
                    print("No se pudo colocar la pieza. Intenta nuevamente.")

            # Mensaje de error si elige una opción inválida
            print("Opción no válida. Por favor, elige [1] o [2].")




