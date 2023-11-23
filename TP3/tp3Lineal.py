from args import parse_args
import pulp

def read_file(path):
    jugadores = []
    with open(path, 'r') as file:
        for linea in file:
            jug_x_periodista = linea.strip().split(',')
    
            jugadores.append(jug_x_periodista)
    
    return jugadores



def jugadores_optimos_programacion_lineal(jugadores_segun_preferencias, todos_los_jugadores):
    problema = pulp.LpProblem("jugadores_seleccionados", pulp.LpMinimize)
    variables_jugadores= []
    
    for jugador in jugadores:
        variables_jugadores.append(pulp.LpVariable(jugador, cat="Binary"))


    problema.solve()
    
if __name__ == '__main__':
    args = parse_args()
    jugadores_segun_preferencias = read_file(args.filename)
    todos_los_jugadores = [set(preferencia) for preferencia in jugadores_segun_preferencias]
    jugadores_optimos_programacion_lineal
    