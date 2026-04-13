class Tablero:
    import numpy as np
    import random
    from constantes import DIMENSION, AGUA, IMPACTO,FALLO, ORIENTACIONES, BARCO
    """
    Representa el tablero de juego de un jugador o de la máquina.
    """

    def __init__(self, id_jugador: str, barcos : dict):
        self.player_id = player_id
        self.barcos = barcos #diccionario de barcos
        self.size = DIMENSION
        self.tablero = np.full((self.size, self.size), AGUA)
        self.seguimiento = np.full((self.size, self.size), AGUA)

    def colocar_barcos(self):
        """
        Coloca todos los barcos definidos en BARCOS.
        """
        for eslora in barcos.values():
            self._colocar_barco_individual(eslora)

    def _colocar_barco_individual(self):
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
            return IMPACTO

        elif self.tablero[x][y] == AGUA:
            self.tablero[x][y] = FALLO
            return FALLO


    
    def mostrar_tablero(self, ocultar_barcos=False):
        """
        Muestra el tablero propio.
        """
        print(f"\nTablero de {self.id_jugador}")

        for fila in self.tablero:
            fila_mostrar = []
            for celda in fila:
                if ocultar_barcos and celda == BARCO:
                    fila_mostrar.append(AGUA)
                else:
                    fila_mostrar.append(celda)
            print(" ".join(fila_mostrar))

    def mostrar_seguimiento(self):
        """
        Muestra el tablero de disparos realizados al rival.
        """
        print(f"\nSeguimiento de {self.id_jugador}")

        for fila in self.seguimiento:
            print(" ".join(fila))

    def todos_barcos_hundidos(self) -> bool:
        """
        Comprueba si ya no quedan barcos.
        """
        return not (BARCO in self.tablero)

        asfa