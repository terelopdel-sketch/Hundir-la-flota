
Class Tablero:

# Define el nombre del jugador, tamaño del tablero, el tablero del jugador1 y jugador 2

def __init__(self, player_id: str):
    self.player_id = player_id
    self.size = DIMENSION
    self.board = np.full((self.size, self.size), AGUA)
    self.tracking = np.full((self.size, self.size), AGUA)

# Coloca barcos de forma aleatoria en el tablero del jugador

def crea_barco_aleatorio(tablero, eslora, num_intentos=100):
    indice_max_filas = tablero.shape[0] - 1
    indice_max_columnas = tablero.shape[1] - 1
    contador = 0

    while contador <= num_intentos:
        contador += 1

        barco = []

        # Punto inicial
        fila = random.randint(0, indice_max_filas)
        columna = random.randint(0, indice_max_columnas)

        pieza_original = (fila, columna)
        print("Pieza original:", pieza_original)

        barco.append(pieza_original)

        # Orientación
        orientacion = random.choice(ORIENTACIONES)
        print("Con orientación", orientacion)

        # Construir barco
        for i in range(eslora - 1):

            if orientacion == "N":
                fila -= 1
            elif orientacion == "S":
                fila += 1
            elif orientacion == "O":
                columna -= 1
            elif orientacion == "E":
                columna += 1

            pieza = (fila, columna)
            barco.append(pieza)

        # Intentar colocarlo
        tablero_temp = colocar_barco_plus(tablero, barco)

        if isinstance(tablero_temp, np.ndarray):
            print("Barco colocado, número de intentos:", contador)
            return tablero_temp

        print("Intentando colocar otro barco...")

    return tablero  # si falla tras muchos intentos

# Realizar disparo

def realizar_disparo(tablero, coordenada):
    if tablero[coordenada] == BARCO:
        tablero[coordenada] = IMPACTO
        print("¡Tocado!")
    elif tablero[coordenada] == AGUA:
        tablero[coordenada] = FALLO
        print("Agua.")
    elif tablero[coordenada] == IMPACTO or tablero[coordenada] == FALLO:
        print("Ya has disparado aquí.")

# Mostrar tablero del jugador 

def display 
