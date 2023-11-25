from args import parse_args
from pulp import *
from reader import read_file


def programacion_lineal_jugadores(jugadores):
    jugadores_segun_preferencias = jugadores
    todos_los_jugadores = set()
    for preferencia in jugadores_segun_preferencias:
        for jugador in preferencia:
            todos_los_jugadores.add(jugador)

    problema = LpProblem("jugadores_optimos", LpMinimize)
    jugadores_vars = {jugador: LpVariable(f"x_{jugador}", 0, 1, LpBinary) for jugador in todos_los_jugadores}
    problema += lpSum(jugadores_vars[jugador] for jugador in todos_los_jugadores)
    for preferencia in jugadores_segun_preferencias:
        problema += lpSum(jugadores_vars[jugador] * (jugador in preferencia) for jugador in todos_los_jugadores) >= 1
    problema.solve()
    

if __name__ == '__main__':
    args = parse_args()
    jugadores = read_file(args.filename)
    
    programacion_lineal_jugadores(jugadores)
    
