from args import parse_args
from pulp import *
import math

def read_file(path):
    jugadores = []
    with open(path, 'r') as file:
        for linea in file:
            jug_x_periodista = linea.strip().split(',')
    
            jugadores.append(jug_x_periodista)
    
    return jugadores


def solve_hitting_set_real(preferences):
    # Create a linear programming problem
    prob = LpProblem("Hittingem", LpMinimize)

    # Create real variables for each player
    x = LpVariable.dicts("x", preferences, lowBound=0)

    # Objective function: minimize the number of players in the hitting set
    prob += lpSum(x[player] for player in preferences)

    # Constraints for each player
    for player in preferences:
        prob += x[player] <= 1 # A player can only be in the hitting set once
        prob += lpSum(x[pref] for pref in preferences[player]) >= 1 # Each player must have at least one preferred opponent in the hitting set

    # Solve the linear programming problem
    status = prob.solve()

    # Compute the largest set size among the different sets (preferences of the press)
    b = max(len(preferences[player]) for player in preferences)

    # Compute the objective value rounded to the nearest integer
    obj_rounded = math.floor(value(prob.objective) + 0.5)

    # Return the objective value rounded and the optimal hitting set rounded
    return obj_rounded, [player for player in preferences if pulp.value(x[player]) >= 1/b]


if __name__ == '__main__':
    args = parse_args()
    jugadores_segun_preferencias = read_file(args.filename)
    todos_los_jugadores = set()
    for preferencia in jugadores_segun_preferencias:
        for jugador in preferencia:
            todos_los_jugadores.add(jugador)
    
    ret = solve_hitting_set_real(jugadores_segun_preferencias)
    
    print(ret)
