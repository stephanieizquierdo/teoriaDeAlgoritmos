from args import parse_args
from reader import read_file


def greedy_jugadores(jugadores_matrix):
    jugadores = jugadores_matrix.copy()
    jugadores.sort(key=lambda x: len(x))

    solucion = set()

    for propuestas in jugadores:
        optimo_local = propuestas[0] # primer jugador que no está en el set
        for jugador in propuestas:
            if jugador in solucion:
                optimo_local = jugador
                break
        # print(f"Agregando a {optimo_local}")
        solucion.add(optimo_local)

    # print(f"Jugadores: {jugadores}")

    
    return solucion

if __name__ == '__main__':
    args = parse_args()
    jugadores = read_file(args.filename)

    solucion = greedy_jugadores(jugadores)

    print(f"Jugadores minimos {len(solucion)}: {solucion}")