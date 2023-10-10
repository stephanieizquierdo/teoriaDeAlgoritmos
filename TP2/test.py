import unittest
import re
from tp2 import scaloni_ganancia, scaloni_get_max_ganancia, scaloni_plan, read_file


class TestScaloni(unittest.TestCase):


    def setUp(self):
        self.expected = {}
        with open('samples/Resultados Esperados.txt', mode = 'r', encoding = 'utf-8') as file:
            leido = file.read().splitlines()

            for i in range(0, len(leido), 4):
                gain_matcher = re.search("Ganancia maxima: (.*)", leido[i+1])
                plan_matcher = re.search("Plan de entrenamiento: (.*)", leido[i+2])
                plan = plan_matcher.group(1).split(', ')
                self.expected[leido[i]] = {
                    'gain': int(gain_matcher.group(1)),
                    'plan': plan,
                }
        

    def test_3(self):
        exp = self.expected['3.txt']
        e_i, s_i, _ = read_file(f"samples/3.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_10(self):
        exp = self.expected['10.txt']
        e_i, s_i, _ = read_file(f"samples/10.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_10_bis(self):
        exp = self.expected['10_bis.txt']
        e_i, s_i, _ = read_file(f"samples/10_bis.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])
    
    def test_10_todo_entreno(self):
        exp = self.expected['10_todo_entreno.txt']
        e_i, s_i, _ = read_file(f"samples/10_todo_entreno.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_50(self):
        exp = self.expected['50.txt']
        e_i, s_i, _ = read_file(f"samples/50.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_50_bis(self):
        exp = self.expected['50_bis.txt']
        e_i, s_i, _ = read_file(f"samples/50_bis.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_100(self):
        exp = self.expected['100.txt']
        e_i, s_i, _ = read_file(f"samples/100.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_500(self):
        exp = self.expected['500.txt']
        e_i, s_i, _ = read_file(f"samples/500.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_1000(self):
        exp = self.expected['1000.txt']
        e_i, s_i, _ = read_file(f"samples/1000.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])

    def test_5000(self):
        exp = self.expected['5000.txt']
        e_i, s_i, _ = read_file(f"samples/5000.txt")
        ganancia = scaloni_ganancia(e_i, s_i)
        plan = scaloni_plan(ganancia)
        max_ganancia = scaloni_get_max_ganancia(ganancia)
        self.assertEqual(max_ganancia, exp['gain'])
        # self.assertListEqual(plan, exp['plan'])


if __name__ == '__main__':
    unittest.main()