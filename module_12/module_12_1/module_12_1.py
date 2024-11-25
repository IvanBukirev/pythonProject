import unittest
from module_12.module_12_1.runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('Ivan')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('runner')
        runner2= Runner('runner2')
        for _ in range(10):
            runner.run()
            runner2.walk()
        self.assertNotEqual(runner.distance, runner2.distance)



if __name__ == '__main__':
    unittest.main()
