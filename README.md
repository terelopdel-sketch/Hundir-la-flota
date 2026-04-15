# Hundir la flota
Challenger hundir la flota: Raquel, Ali, Tere, Ares.

---

## Descripción

El objetivo del programa es simular un juego de Hundir la Flota, donde el objetivo es hundir todos los barcos del rival antes de que él hunda los tuyos.

Cada jugador tiene sus barcos dispuestos en un tablero y un registro de los movimientos realizados en otro.

---

## Estructura

```bash
.
├── variables.py     # Constantes del juego (dimensión, barcos, símbolos)
├── clases.py        # Clase Tablero (lógica principal del juego)
├── funciones.py     # Funciones auxiliares (input, turnos, impresión)
├── main.py          # Ejecución del juego
```

---

## Ejecución

### 1. Clonar repositorio

```bash
git clone https://github.com/terelopdel-sketch/Hundir-la-flota.git
cd Hundir-la-flota
```

---

### 2. Ejecutar el programa

```bash
python main.py
```

---

## Funcionamiento

1. Los tableros se generan automáticamente.
2. Los barcos se colocan de forma aleatoria.
3. El jugador introduce coordenadas (fila y columna).
4. El sistema responde:

   * Impacto si hay barco.
   * Agua si no lo hay.
5. La máquina realiza disparos aleatorios.
6. El juego termina cuando todos los barcos de un jugador han sido destruidos.

---

## Simbología

| Símbolo | Significado                       |
| ------- | --------------------------------- |
| " "     | Agua (casilla vacía sin disparar) |
| "O"     | Barco                             |
| "X"     | Impacto (barco alcanzado)         |
| "-"     | Fallo (disparo al agua)           |

---

## Configuración del juego

En el archivo variables.py se definen los parámetros principales del juego:

* Dimensión del tablero:

```python
DIMENSION = 10
```

* Tipos de barcos:

```python
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
```

---

## Componentes principales

### Clase Tablero (clases.py)

Se encarga de:

* Crear el tablero de juego.
* Colocar los barcos de forma aleatoria.
* Gestionar los disparos recibidos.
* Mostrar el estado del tablero.
* Comprobar si todos los barcos han sido hundidos.

---

### Funciones auxiliares (funciones.py)

* Solicitud de coordenadas al usuario.
* Generación de turnos del oponente.
* Visualización de los tableros.
* Resultado del juego.

---

## Fin del juego

El juego finaliza cuando uno de los jugadores ha perdido todos sus barcos. En ese momento se muestra un mensaje indicando el ganador.

---

## Posibles mejoras

* Implementar una inteligencia artificial más avanzada.
* Interfaz gráfica.
* Modo multijugador.
* Mejorar la validación de entradas.

---

## Notas

Este proyecto ha sido desarrollado con fines educativos para practicar programación en Python, uso de clases, funciones y trabajo en equipo con Git y GitHub.
