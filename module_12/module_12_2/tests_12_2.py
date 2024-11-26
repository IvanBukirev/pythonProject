import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 10)
        self.runner2 = rt.Runner('Андрей', 9)
        self.runner3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for tournament, results in cls.all_results.items():
            print(f' {{{', '.join([f'{place}: {name}' for place, name in results.items()])}}}')

    def test_turn1(self):
        turn_1 = rt.Tournament(90, self.runner1, self.runner3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    def test_turn2(self):
        turn_2 = rt.Tournament(90, self.runner2, self.runner3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_turn3(self):
        turn_3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    def test_turn4(self):
        turn_4 = rt.Tournament(6, self.runner1, self.runner2, self.runner3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn4'] = result


if __name__ == '__main__':
    unittest.main()
