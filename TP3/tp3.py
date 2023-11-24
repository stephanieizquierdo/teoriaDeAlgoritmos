from args import parse_args
from reader import read_file


def backtracking_jugadores_optimos(jugadores_matriz, periodista, solucion_optima, solucion_actual):
    if periodista == len(jugadores_matriz):
        if len(solucion_optima) == 0 or len(solucion_actual) <= len(solucion_optima):
            solucion_optima = solucion_actual.copy()
        return solucion_optima
    
    if len(solucion_optima) != 0 and len(solucion_actual) >= len(solucion_optima):
        return solucion_optima

    for jugador in jugadores_matriz[periodista]:
        jugadores_temporales = solucion_actual.copy()
        jugadores_temporales.add(jugador)

        solucion_optima = backtracking_jugadores_optimos(jugadores_matriz, periodista + 1, solucion_optima, jugadores_temporales)
    
    return solucion_optima

if __name__ == '__main__':
    args = parse_args()
    jugadores = read_file(args.filename)

    solucion = set()
    solucion = backtracking_jugadores_optimos(jugadores, 0, solucion, set())

    print(f"Jugadores minimos {len(solucion)}: {solucion}")