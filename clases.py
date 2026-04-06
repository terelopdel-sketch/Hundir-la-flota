
Class Tablero:

# Define el nombre del jugador, tamaño del tablero, el tablero del jugador1 y jugador 2

def __init__(self, player_id: str):
    self.player_id = player_id
    self.size = BOARD_SIZE
    self.board = np.full((self.size, self.size), EMPTY)
    self.tracking = np.full((self.size, self.size), EMPTY)

# Coloca barcos de forma aleatoria en el tablero del jugador



