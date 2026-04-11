 @ -0,0 +1,166 @@


# ============================================================
# CLASES DEL JUEGO
# ============================================================

import numpy as np
import random
from variables import DIMENSION, AGUA, IMPACTO, FALLO, ORIENTACIONES, BARCO


class Tablero:
    """
    Representa el tablero de un jugador.

    Atributos:
        jugador_id  : nombre o identificador del jugador
        barcos      : dict con nombre y eslora de cada barco
        board       : array 10x10 con barcos e impactos (lo que ve el dueño)
        tracking    : array 10x10 solo con impactos (lo que ve el rival sobre este tablero)
        coordenadas_barcos : set con todas las coordenadas (fila, col) ocupadas por barcos
        vidas       : número total de casillas con barco (= sum de esloras)
    """
# Define el nombre del jugador, tamaño del tablero, el tablero del jugador1 y jugador 2

    def __init__(self, player_id: str, barcos: dict):
        self.player_id = player_id
        self.barcos = barcos # Se guarda el diccionario de barcos para colocarlo
        self.size = DIMENSION # Esto no sería necesario porque podemos utilizar la constante dimension
        self.board = np.full((self.size, self.size), AGUA) # tablero jugador
        self.tracking = np.full((self.size, self.size), AGUA) # tablero vista rival sin barcos
        self.coordenadas_barcos = set() # vamos a guardar las coordenadas de los barcos

# Coloca barcos de forma aleatoria en el tablero del jugador

    def crea_barco_aleatorio(self):
        indice_max_filas = DIMENSION - 1 # Aquí sería dimensión -1
        indice_max_columnas = DIMENSION - 1
        
        for nombre, eslora in self.barcos.items():
            colocado = False
            intentos = 0
        
            while not colocado:
                intentos += 1
                if intentos > 1000:
                    # Reiniciar si hay demasiados intentos (tablero muy fragmentado)
                    self.board = np.full((DIMENSION, DIMENSION), AGUA)
                    self.coordenadas_barcos = set()
                    intentos = 0

            celdas = []

        # Punto inicial
            fila = random.randint(0, indice_max_filas)
            col = random.randint(0, indice_max_columnas)

            

        # Orientación
            orientacion = random.choice(ORIENTACIONES)
            print("Con orientación", orientacion)

            celdas = self.calcular_celdas(fila, col, eslora, orientacion) # Aquí guardamos todas las celdas del barco

            if celdas and self.es_valido(celdas):
                for (f, c) in celdas:
                    self.board[f][c] = BARCO
                    self.coordenadas_barcos.add((f, c))
                colocado = True
    
    def calcular_celdas(self, fila, col, eslora, orientacion):
        """
        Devuelve la lista de celdas que ocuparía un barco dada su posición,
        eslora y orientación. Retorna None si se sale del tablero.
        """
        celdas= []
        celdas.append(fila, col) # aquí guardamos el punto inicial

        for i in range(eslora - 1):

                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                 fila += 1
                elif orientacion == "O":
                    columna -= 1
                elif orientacion == "E":
                    columna += 1

                if 0 <= fila < DIMENSION and 0 <= col < DIMENSION:
                    celdas.append((fila, col))
                else:
                    return None  # Se sale del tablero

    def es_valido(self, celdas):
        """Comprueba que ninguna celda esté ya ocupada por otro barco."""
        for (f, c) in celdas:
            if (f, c) in self.coordenadas_barcos:
                return False
        return True
        

# Realizar disparo

def recibir_disparo(self, fila, col):
        """
        Procesa un disparo recibido en (fila, col).

        Retorna:
            "impacto"  si había barco
            "fallo"    si era agua
            "repetido" si esa casilla ya fue disparada
        """
        celda = self.tablero[fila][col]

        if celda == IMPACTO or celda == FALLO:
            return "repetido"

        if celda == BARCO:
            self.board[fila][col] = IMPACTO
            self.tracking[fila][col] = IMPACTO
            self.coordenadas_barcos.discard((fila, col))
            self.vidas -= 1
            return "impacto"
        else:
            self.board[fila][col] = FALLO
            self.tracking[fila][col] = FALLO
            return "fallo"
        
 # ----------------------------------------------------------
    # ESTADO DEL JUEGO
    # ----------------------------------------------------------

    def sin_barcos(self):
        """Retorna True si el jugador no tiene barcos restantes."""
        return self.vidas <= 0       

# ----------------------------------------------------------
    # VISUALIZACIÓN
    # ----------------------------------------------------------

    def imprimir(self, mostrar_barcos=True):
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

    def imprimir_vista_rival(self):
        """Imprime solo los disparos realizados sobre este tablero (sin revelar barcos)."""
        print("    " + "  ".join(str(i) for i in range(DIMENSION)))
        print("   " + "---" * DIMENSION)
        for i, fila in enumerate(self.vista_rival):
            print(f"{i:2} | " + "  ".join(fila))