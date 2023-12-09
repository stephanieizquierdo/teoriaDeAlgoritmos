from args import parse_args
from pulp import *
from reader import read_file
    

def programacion_lineal_jugadores_variables_continuas(jugadores):
    jugadores_segun_preferencias = jugadores
    todos_los_jugadores = set()
    for preferencia in jugadores_segun_preferencias:
        for jugador in preferencia:
            todos_los_jugadores.add(jugador)

    problema = LpProblem("jugadores_optimos", LpMinimize)
    jugadores_vars = {jugador: LpVariable(f"x{jugador}", 0, 1, LpContinuous) for jugador in todos_los_jugadores}
    problema += lpSum(jugadores_vars[jugador] for jugador in todos_los_jugadores)
    for preferencia in jugadores_segun_preferencias:
        problema += lpSum(jugadores_vars[jugador] * (jugador in preferencia) for jugador in todos_los_jugadores) >= 1
    problema.solve(PULP_CBC_CMD(msg=0))

    b = max([len(x) for x in jugadores])

    # print(f"b={b}; 1/b={1/b}")

    jugadores_values = {jug: pulp.value(jug_var) for jug, jug_var in jugadores_vars.items()}
    jugadores_filtrados = dict(filter(lambda pair: pair[1] >= 1/b, jugadores_values.items())) 

    jugadores_lp = list(jugadores_filtrados.keys())
    
    return jugadores_lp

if __name__ == '__main__':
    args = parse_args()
    jugadores = read_file(args.filename)
    
    solucion = programacion_lineal_jugadores_variables_continuas(jugadores)

    print(f"Jugadores minimos {len(solucion)}: {solucion}")
    
