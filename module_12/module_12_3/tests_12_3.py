import unittest
from module_12.module_12_1 import runner
from module_12.module_12_2 import runner_and_tournament as rt

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1= runner.Runner('runner')
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_2=runner.Runner('runner2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_3 = runner.Runner('runner3')
        run_4=runner.Runner('runner4')
        for _ in range(10):
            run_3.run()
            run_4.walk()
        self.assertNotEqual(run_3.distance, run_4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tournament, results in cls.all_results.items():
            print(f' {{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = rt.Tournament(90, self.runner1, self.runner3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = rt.Tournament(90, self.runner2, self.runner3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn4(self):
        turn_4 = rt.Tournament(6, self.runner1, self.runner2, self.runner3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn4'] = result

if __name__ == '__main__':
    unittest.main()