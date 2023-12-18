from reader import read_file
from tp3 import backtracking_jugadores
from tp3LinealContinua import programacion_lineal_jugadores_variables_continuas
from tp3LinealEntera import programacion_lineal_jugadores
from tp3greedy import greedy_jugadores

ALL_ALGORITHMS = [
    (greedy_jugadores, 'Greedy'),
    # (backtracking_jugadores, 'Backtracking'),
    (programacion_lineal_jugadores, 'Programación Lineal Entera'),
    (programacion_lineal_jugadores_variables_continuas, 'Programación Lineal con Variables Continuas'),
]


if __name__ == '__main__':
    files = [
        '5.txt',
        '7.txt',
        '10_pocos.txt',
        '10_todos.txt',
        '10_varios.txt',
        '15.txt',
        '20.txt',
        '50.txt',
        '75.txt',
        '100.txt',
        '200.txt',
        ]

    for f in files:
        jugadores = read_file(f"samples/{f}")

        print(f"{f}:\n")

        for algoritmo, name in ALL_ALGORITHMS:
            print(f"Algoritmo {name}")
            solucion = algoritmo(jugadores)
            if not solucion: continue
            print(f"Jugadores mínimos {len(solucion)}: {solucion}\n")
        
        print("\n================================")
