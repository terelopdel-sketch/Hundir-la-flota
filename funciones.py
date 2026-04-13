import numpy as np
from variables import *


def mostrar_tableros(tablero_jugador, tablero_maquina):
    """Muestra el tablero del jugador completo y el de la máquina sin barcos."""
    print(f"\n{'='*30}")
    print("  TU TABLERO")
    print(f"{'='*30}")
    tablero_jugador.imprimir(mostrar_barco=True)

    print(f"\n{'='*30}")
    print("  TABLERO ENEMIGO")
    print(f"{'='*30}")
    tablero_maquina.imprimir()


def pedir_coordenadas(tablero_visible):
    """Pide fila y col válidas y no repetidas al usuario."""
    while True:
        try:
            fila = int(input(f"Introduce fila (0-{DIMENSION - 1}): "))
            col  = int(input(f"Introduce columna (0-{DIMENSION - 1}): "))
            if not (0 <= fila < DIMENSION and 0 <= col < DIMENSION):
                print(f"  Coordenadas fuera de rango (0-{DIMENSION - 1}).")
                continue
            if tablero_visible[fila, col] in [IMPACTO, FALLO]:
                print("  Ya disparaste ahi. Elige otra posicion.")
                continue
            return fila, col
        except ValueError:
            print("  Introduce numeros enteros.")


def turno_maquina(tablero_visible):
    """Genera coordenadas aleatorias validas para la maquina."""
    while True:
        fila = np.random.randint(0, DIMENSION)
        col  = np.random.randint(0, DIMENSION)
        if tablero_visible[fila, col] not in [IMPACTO, FALLO]:
            return fila, col


def imprimir_resultado(ganador):
    """Imprime el mensaje final segun quien haya ganado."""
    print(f"\n{'='*30}")
    if ganador == "jugador":
        print("  HAS GANADO! Hundiste todos los barcos enemigos.")
    else:
        print("  La maquina ha ganado. Todos tus barcos han sido hundidos.")
    print(f"{'='*30}")
    coord = f"({fila}, {col})"
    
    if impacto:
        print(f"{jugador} disparó en {coord} -> ¡IMPACTO!")
    else:
        print(f"{jugador} disparó en {coord} -> Agua.")

