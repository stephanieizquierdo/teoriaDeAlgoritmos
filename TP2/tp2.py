from args import parse_args
import numpy as np

ENTRENO = 'Entreno'
DESCANSO = 'Descanso'

def read_file(path):
  file = open(path, mode = 'r', encoding = 'utf-8-sig')
  leido = file.read().splitlines()

  cant_dias = leido[0]

  e_i=[]
  s_i=[]

  rango_cant_dias = range(int(cant_dias))
  for dia in rango_cant_dias:
    e_i.append(int(leido[dia+ 1]))
    s_i.append(int(leido[int(cant_dias)+dia+1]))
  
  file.close()

  return e_i, s_i, cant_dias


def scaloni_ganancia(e_i, s_i):
  cant_dias = len(e_i)
  matriz = np.zeros((cant_dias, cant_dias), dtype=int)
    
  for columna in range(len(matriz[0])):
    for fila in range(len(matriz)):
      if fila == 0:
        if columna==0 or columna==1:
          matriz[fila][columna] = min(s_i[fila], e_i[columna])
        else:
          matriz[fila][columna] = min(s_i[fila], e_i[columna]) + max(matriz[:, columna-2])
      elif fila > columna: continue
      else:
          matriz[fila][columna] = min(s_i[fila], e_i[columna]) + matriz[fila-1, columna-1]
  return matriz

def scaloni_get_max_ganancia(opt):
  return max(opt[:, -1])


def scaloni_plan(opt):
  cant_dias = opt.shape[1]
  idx_fila, idx_col = (np.argmax(opt[:, -1]), cant_dias - 1)
  plan = [ENTRENO]

  while len(plan) != cant_dias:
    if idx_fila != 0:
      idx_fila -= 1
      idx_col -= 1
      plan.append(ENTRENO)
    else:
      idx_fila = np.argmax(opt[:, idx_col-1]) # check if idx_col == 0
      idx_col -= 1
      plan.append(DESCANSO)

  return plan[::-1]


if __name__ == '__main__':
  args = parse_args()
  e_i, s_i, _ = read_file(args.filename)

  ganancia = scaloni_ganancia(e_i, s_i)
  plan = scaloni_plan(ganancia)
  
  print(f"Ganancia máxima: {scaloni_get_max_ganancia(ganancia)}")
  print(f"Plan de entrenamiento: {plan}")