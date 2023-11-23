from args import parse_args
from pulp import *

def read_file(path):
    jugadores = []
    with open(path, 'r') as file:
        for linea in file:
            jug_x_periodista = linea.strip().split(',')
    
            jugadores.append(jug_x_periodista)
    
    return jugadores

def jugadores_optimos_programacion_lineal(jugadores_segun_preferencias, todos_los_jugadores):
    problema = LpProblem("jugadores_optimos", LpMinimize)
    jugadores_vars = {jugador: LpVariable(f"x_{jugador}", 0, 1, LpBinary) for jugador in todos_los_jugadores}
    problema += lpSum(jugadores_vars[jugador] for jugador in todos_los_jugadores)
    for preferencia in jugadores_segun_preferencias:
        problema += lpSum(jugadores_vars[jugador] * (jugador in preferencia) for jugador in todos_los_jugadores) >= 1
    problema.solve()
    

if __name__ == '__main__':
    args = parse_args()
    jugadores_segun_preferencias = read_file(args.filename)
    todos_los_jugadores = set()
    for preferencia in jugadores_segun_preferencias:
        for jugador in preferencia:
            todos_los_jugadores.add(jugador)
    
    jugadores_optimos_programacion_lineal(jugadores_segun_preferencias, todos_los_jugadores)
    
