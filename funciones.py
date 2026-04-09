import numpy as np
from variables import *

def imprimir_tableros(tablero_propio, tablero_visible_enemigo, jugador):
    """Imprime los dos tableros en paralelo."""
    
    print(f"\n{'='*45}")
    print(f" JUGADOR: {jugador}")
    print(f"{'='*45}")
    print(" TU TABLERO        TABLERO ENEMIGO")
    
    # Cabecera con DIMENSION dinámica
    print("   " + " ".join(str(i) for i in range(DIMENSION)) +
          "     " + " ".join(str(i) for i in range(DIMENSION)))
    
    for i in range(DIMENSION):
        fila_propia = " ".join(tablero_propio[i])
        fila_enemigo = " ".join(tablero_visible_enemigo[i])
        print(f"{i:2} {fila_propia}     {fila_enemigo}")


def pedir_coordenadas(tablero_visible):
    """Pide fila y col válidas y no repetidas al usuario."""
    
    while True:
        try:
            fila = int(input(f"Introduce fila (0-{DIMENSION-1}): "))
            col = int(input(f"Introduce columna (0-{DIMENSION-1}): "))
            
            if not (0 <= fila < DIMENSION and 0 <= col < DIMENSION):
                print("Coordenadas fuera de rango.")
                continue

            # CAMBIO: usar FALLO en vez de AGUA_DISPARADA
            if tablero_visible[fila, col] in [IMPACTO, FALLO]:
                print("Ya disparaste ahí. Elige otra posición.")
                continue

            return fila, col

        except ValueError:
            print("Introduce números enteros.")


def turno_maquina(tablero_visible):
    """Genera coordenadas aleatorias evitando repetir."""
    
    while True:
        fila = np.random.randint(0, DIMENSION)
        col = np.random.randint(0, DIMENSION)

        # CAMBIO: usar FALLO
        if tablero_visible[fila, col] not in [IMPACTO, FALLO]:
            return fila, col


def mostrar_resultado_disparo(fila, col, impacto, jugador):
    """Imprime el resultado de un disparo."""
    
    coord = f"({fila}, {col})"
    
    if impacto:
        print(f"{jugador} disparó en {coord} -> ¡IMPACTO!")
    else:
        print(f"{jugador} disparó en {coord} -> Agua.")

