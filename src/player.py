from piece import Piece
from board import Board

# Regla de Blokus: Cada jugador debe empezar con 21 piezas
class Player:

    # Método constructor de la clase Player con sus atributos
    def __init__(self, player_id, name, color):
        self.player_id = player_id
        self.name = name
        self.color = color
        self.canPlay = True
        self.pieces = Piece.generate_random_pieces(color)
        self.first_move = True

        # Muestra las piezas del jugador horizontalmente, alineadas
    def show_player_pieces(self):
        # Determina la altura máxima de las piezas
        max_height = max(len(piece.shape) for piece in self.pieces)
        
        # Determina el ancho máximo de las piezas
        max_width = max(max(len(row) for row in piece.shape) for piece in self.pieces)
        
        # Para cada fila hasta la altura máxima
        for i in range(max_height):
            for piece in self.pieces:
                if i < len(piece.shape):
                    # Si la fila existe en la pieza, imprime la fila alineada con el ancho máximo
                    print(' '.join(piece.shape[i]).ljust(max_width * 2), end=' ')
                else:
                    # Si la pieza es más pequeña, imprime espacios vacíos para mantener el formato
                    print(' ' * (max_width * 2), end=' ')
            print()  # Nueva línea después de imprimir todas las piezas en esa fila
            
    # Permite al jugador seleccionar una de sus piezas
    def pick_piece(self,player, board):
        
        print()
        print(f"Turno de: [{self.name}]\n")
        opcionDeJuego=int(input("""
        Eliga la opcion que desea realizar:
        [1] Elegir pieza
        [2] Rendirme
        """))

        if opcionDeJuego ==1:
            print(f"Estas son tus piezas disponibles (numeradas de izquierda a derecha, del 1 al 21): \n")

            self.show_player_pieces()
            # player.pick_piece(board)
            # player.place_player_piece(board)

            # Elegir una pieza por número (se le resta 1 para usar como índice)
            selection = int(input("Escribe aquí el número de la pieza que deseas utilizar: ")) - 1
            selected_piece=self.pieces[selection]
            self.place_player_piece(selected_piece,board)
        else:
            player.canPlay=False
        
        

    # Permite al jugador colocar la pieza seleccionada en el tablero
    def place_player_piece(self, selected_piece, board):
        pos_x = int(input(f"Ingresa el num. de fila: "))
        pos_y = int(input(f"Ingrese el num. de columna: "))

        if self.first_move:
            # Si es el primer movimiento, la pieza puede colocarse en cualquier lugar
            board.place_piece(selected_piece, pos_x, pos_y)
            self.first_move = False  # Actualizamos el estado
        else:
            # Si no es el primer movimiento, valida que toque una esquina
            if self.is_valid_corner(board, selected_piece, pos_x, pos_y):
                board.place_piece(selected_piece, pos_x, pos_y)
            else:
                print("¡La pieza debe tocar otra pieza solo por las esquinas!")

        # Elimina la pieza que el jugador utilizó de su lista de piezas disponibles
        self.pieces.remove(selected_piece)

        # Muestra el tablero con la pieza colocada
        board.print_map()

    # Valida si la pieza toca una esquina de otra pieza
    def is_valid_corner(self, board, piece, pos_x, pos_y):
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Direcciones de las esquinas

        for i in range(len(piece.shape)):
            for j in range(len(piece.shape[i])):
                if piece.shape[i][j] != ' ':  # Solo verifica las celdas de la pieza que no estan vacias
                    for dir_x, dir_y in directions:
                        check_x = pos_x + i + dir_x
                        check_y = pos_y + j + dir_y
                        # Verifica si estamos dentro de los límites del tablero
                        if 0 <= check_x < board.high and 0 <= check_y < board.width:
                            # Si la celda en la esquina no esta vacia, marca que esta tocando otra pieza
                            if board.map[check_x][check_y] != '.':
                                return True

        return False

#  Cada vez que se instancia un jugador, este viene ya con su lista de 21 piezas
# amelia = Player(1, "Amelia", "Blue")

# amelia.show_pieces_jugador()
