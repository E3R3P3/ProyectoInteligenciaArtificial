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
    def place_player_piece(self,selected_piece, board):
        # selected_piece = self.pick_piece(player,board)
        pos_x = int(input(f"Ingresa el num. de fila: "))
        pos_y = int(input(f"Ingrese el num. de columna: "))

        # Coloca la pieza en el tablero usando el método place_piece de Board
        board.place_piece(selected_piece, pos_x, pos_y)

        print('------------ probando rotacion ------------')
        # selected_piece.rotar()
        # selected_piece.
        board.place_piece(selected_piece, pos_x, pos_y)

        # # Elimina la pieza que el jugador utilizó, de su lista de piezas disponibles
        self.pieces.remove(selected_piece)

        # Muestra el tablero con la pieza colocada
        board.print_map()
    

#  Cada vez que se instancia un jugador, este viene ya con su lista de 21 piezas
# amelia = Player(1, "Amelia", "Blue")

# amelia.show_pieces_jugador()
