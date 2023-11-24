def read_file(path):
    jugadores = []
    with open(path, 'r') as file:
        for linea in file:
            jug_x_periodista = linea.strip().split(',')
    
            jugadores.append(jug_x_periodista)
    
    return jugadores