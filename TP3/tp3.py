from args import parse_args
from reader import read_file


def es_compatible(jugadores_matriz, solucion):
    for jugadores in jugadores_matriz:
        if not bool(set(jugadores) & solucion):
            return False
        # presente = False
        # for jugador in jugadores:
        #     if jugador in solucion:
        #         presente = True
        #         break
        # if not presente:
        #     return False
    return True

# Condiciones de corte
# - Llego al último periodista y tengo que descartar la solución porque no es optima
# - Llego a algun periodista y descarto la solución porque ya no es óptima
# - Llego a algún periodista y me quedo con la solución porque al fijarme si es valido, es mejor que la optima
# - Si ya probé con un jugador y no funcionó en la solución actual, descarto la rama actual (solucion actual)


def _backtracking_jugadores_optimos(jugadores_matriz, periodista, solucion_optima, solucion_actual,
                                    jugadores_sin_probar):
    if periodista == len(jugadores_matriz):
        if len(solucion_optima) == 0 or len(solucion_actual) < len(solucion_optima) and es_compatible(jugadores_matriz, solucion_actual):
            solucion_optima = solucion_actual.copy()
            #print(f"Actualizo Optimo al final row {periodista} {solucion_optima}")
            return solucion_optima
        else:
            #print(f"No actualizo Optimo al final row {periodista}")
            return solucion_optima
    
    if len(solucion_optima) != 0 and len(solucion_actual) >= len(solucion_optima):
        #print(f"Descarto solucion cuando row es {periodista}")
        return solucion_optima
    
    if len(solucion_actual) < len(solucion_optima) and es_compatible(jugadores_matriz, solucion_actual):
            solucion_optima = solucion_actual.copy()
            #print(f"Encuentro solucion antes del final en row {periodista} {solucion_optima}")
            return solucion_optima

    for jugador in jugadores_matriz[periodista]:
        # if jugador not in jugadores_sin_probar:
        #     continue

        jugadores_temporales = solucion_actual.copy()
        jugadores_temporales.add(jugador)

        solucion_optima = _backtracking_jugadores_optimos(jugadores_matriz, periodista + 1, solucion_optima, jugadores_temporales, jugadores_sin_probar)
        
        # jugadores_sin_probar.update(solucion_optima)

    
    return solucion_optima

def backtracking_jugadores(jugadores):

    todos_los_jugadores = set()
    sol_base = set()
    for preferencia in jugadores:
        # sol_base.add(preferencia[0])
        for jugador in preferencia:
            todos_los_jugadores.add(jugador)


    return _backtracking_jugadores_optimos(jugadores, 0, sol_base, set(), todos_los_jugadores)

if __name__ == '__main__':
    args = parse_args()
    jugadores = read_file(args.filename)
    #jugadores = read_file("TP3/samples/7.txt")

    solucion = backtracking_jugadores(jugadores)

    print(f"Jugadores minimos {len(solucion)}: {solucion}")