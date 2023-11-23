from args import parse_args
import pulp

def read_file(path):
    jugadores = []
    with open(path, 'r') as file:
        for linea in file:
            jug_x_periodista = linea.strip().split(',')
    
            jugadores.append(jug_x_periodista)
    
    return jugadores

def jugadores_optimos_programacion_lineal(jugadores):
    problema = pulp.LpProblem("jugadores_seleccionados", pulp.LpMinimize)
    problema.solve()
    
if __name__ == '__main__':
    args = parse_args()
    jugadores = read_file(args.filename)
    