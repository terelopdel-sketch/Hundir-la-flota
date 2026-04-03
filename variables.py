# Dimensión del tablero
DIMENSION = 10

# Barcos del juego: {nombre:eslora}
BARCOS = {
    "Barcaza 1": 1,
    "Barcaza 2": 1,
    "Barcaza 3": 1,
    "Barcaza 4": 1,
    "Fragata 1": 2,
    "Fragata 2": 2,
    "Fragata 3": 2,
    "Corbeta 1": 3,
    "Corbeta 2": 3,
    "Buque": 4
}

# Simbolos del tablero
AGUA = " "   # casilla vacia sin disparar
BARCO = "O"  # Barco sin impactar
IMPACTO = "X"  # Disparo que ha dado a un barco
FALLO = "-"  # Disparo que ha dado en agua

# Orientaciones posibles para colocar los barcos
ORIENTACIONES = ["N", "S", "E", "O"]
