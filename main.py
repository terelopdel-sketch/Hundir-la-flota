# ============================================================
# MAIN - Hundir la Flota
# ============================================================
import numpy as np

from clases import *
from funciones import (pedir_coordenadas, mostrar_tableros, imprimir_resultado, bienvenida, coordenadas_maquina)
from funciones import (pedir_coordenadas, mostrar_tableros, imprimir_resultado, mensaje_bienvenida, coordenadas_maquina)
from variables import *


def main():
    bienvenida()

    # ---- Inicialización (solo una vez) ----
    tablero_jugador = Tablero(id_jugador="jugador", barcos=BARCOS)
    tablero_maquina = Tablero(id_jugador="maquina", barcos=BARCOS)

    tablero_jugador.colocar_barcos()
    tablero_maquina.colocar_barcos()

    print("¡Los barcos han sido colocados! ¡Que empiece la batalla!\n")

    disparos_jugador = set()   # Coordenadas ya disparadas por el jugador
    disparos_maquina = set()   # Coordenadas ya disparadas por la máquina

    # ---- Bucle principal del juego ----
    while True:

        # ---- TURNO DEL JUGADOR ----
        mostrar_tableros(tablero_jugador, tablero_maquina)

        turno_jugador = True
        while turno_jugador:
            print(f"\n  Tus vidas: {tablero_jugador.vidas} | Vidas rival: {tablero_maquina.vidas}")
            fila, col = pedir_coordenadas(disparos_jugador)
            disparos_jugador.add((fila, col))

            resultado = tablero_maquina.recibir_disparo(fila, col)

            if resultado == "impacto":
                print(f" ¡IMPACTO en ({fila}, {col})!")
                if tablero_maquina.todos_barcos_hundidos():
                    imprimir_resultado("jugador")
                    return  # Fin del juego
                else:
                    print("¡ Vuelve a dispara !")
                print(f" ¡IMPACTO en ({fila}, {col})! Vuelves a disparar.")
                if tablero_maquina.todos_barcos_hundidos():
                    imprimir_resultado("jugador")
                    return  # Fin del juego
            else:
                print(f" Agua en ({fila}, {col}). Turno de la máquina.")
                turno_jugador = False  # Pasa el turno a la máquina

        # ---- TURNO DE LA MÁQUINA ----
        turno_maquina = True
        while turno_maquina:
            fila, col = coordenadas_maquina(disparos_maquina)
            fila, col = turno_maquina(disparos_maquina)
            disparos_maquina.add((fila, col))

            resultado = tablero_jugador.recibir_disparo(fila, col)

            if resultado == "impacto":
                print(f"\n Máquina impacta en ({fila}, {col}). Sigue disparando...")
                if tablero_jugador.todos_barcos_hundidos():
                    imprimir_resultado("maquina")
                    return  # Fin del juego
            else:
                print(f"  La máquina falla en ({fila}, {col}). ¡Tu turno!")
                turno_maquina = False  # Pasa el turno al jugador


if __name__ == "__main__":
    main()
