import numpy as np
import random
from variables import DIMENSION, AGUA, IMPACTO,FALLO, ORIENTACIONES, BARCO, BARCOS


class Tablero:
    
    """
    Representa el tablero de juego de un jugador o de la máquina.
    """

    def __init__(self, id_jugador: str, barcos : dict):
        self.id_jugador = id_jugador
        self.barcos = barcos #diccionario de barcos
        self.size = DIMENSION
        self.tablero = np.full((self.size, self.size), AGUA)
        self.seguimiento = np.full((self.size, self.size), AGUA)
        self.vidas = sum(self.barcos.values())  # Total de casillas ocupadas por barcos

    def colocar_barcos(self):
        """
        Coloca todos los barcos definidos en BARCOS.
        """
        for eslora in self.barcos.values():
            self._colocar_barco_individual(eslora)

    def _colocar_barco_individual(self, eslora):
        """
        Coloca un barco individual de forma aleatoria.
        """
        while True:
            barco = []

            fila = random.randint(0, self.size - 1)
            columna = random.randint(0, self.size - 1)

            barco.append((fila, columna))

            orientacion = random.choice(ORIENTACIONES)

            for _ in range(eslora - 1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "O":
                    columna -= 1
                elif orientacion == "E":
                    columna += 1

                barco.append((fila, columna))

            valido = True
            for x, y in barco:
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    valido = False
                    break
                if self.tablero[x][y] == BARCO:
                    valido = False
                    break

            if not valido:
                continue

            for x, y in barco:
                self.tablero[x][y] = BARCO

            break

    def recibir_disparo(self, x: int, y: int) -> bool:
        """
        Procesa un disparo recibido.
        """

        if self.tablero[x][y] == BARCO:
            self.tablero[x][y] = IMPACTO
            self.seguimiento[x][y] = IMPACTO
            self.vidas -= 1
            return "impacto"
        elif self.tablero[x][y] == IMPACTO or self.tablero[x][y] == FALLO:
            return "repetido"

        elif self.tablero[x][y] == AGUA:
            self.tablero[x][y] = FALLO
            self.seguimiento[x][y] = FALLO
            return "fallo"


    
    def imprimir_tablero(self, mostrar_barcos=True):
        """
        Imprime el tablero por pantalla con cabecera de columnas.

        Args:
            mostrar_barcos: si False, oculta los barcos (útil para ver el tablero rival)
        """
        print("    " + "  ".join(str(i) for i in range(DIMENSION)))
        print("   " + "---" * DIMENSION)
        for i, fila in enumerate(self.tablero):
            fila_visual = []
            for celda in fila:
                if not mostrar_barcos and celda == BARCO:
                    fila_visual.append(AGUA)
                else:
                    fila_visual.append(celda)
            print(f"{i:2} | " + "  ".join(fila_visual))

    def mostrar_seguimiento(self):
        """Imprime solo los disparos realizados sobre este tablero (sin revelar barcos)."""
        print("    " + "  ".join(str(i) for i in range(DIMENSION)))
        print("   " + "---" * DIMENSION)
        for i, fila in enumerate(self.seguimiento):
            print(f"{i:2} | " + "  ".join(fila))

    def todos_barcos_hundidos(self) -> bool:
        """
        Comprueba si ya no quedan barcos.
        """
        return (self.vidas <= 0)

        