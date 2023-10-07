from TP1.args import parse_args
import numpy as np

def read_sample(filename):
  return np.loadtxt(
    filename,
    usecols=(0, 1), delimiter=',',
    dtype={'names': ('S_i', 'A_i'),
                     'formats': ('i4', 'i4')},
    skiprows=1,
)


def scaloni_greedy_sort(times):
  return sorted(times, key=lambda x: x[1], reverse=True)


def scaloni_greedy_best_time(times):
  s_time = 0
  a_time = 0
  max_time = 0
  for scaloni, ayudante in times:
    s_time += scaloni
    new_a_time = s_time + ayudante
    max_time = max(a_time, new_a_time)
    a_time = new_a_time

  return max_time


def scaloni_greedy(times):
  times_sorted = scaloni_greedy_sort(times)

  return scaloni_greedy_best_time(times_sorted)


if __name__ == '__main__':
  args = parse_args()
  sample = read_sample(args.filename)

  print(scaloni_greedy(sample))