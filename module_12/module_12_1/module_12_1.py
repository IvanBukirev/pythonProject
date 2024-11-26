import unittest
from module_12.module_12_1 import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run_1= runner.Runner('runner')
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_2=runner.Runner('runner2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_3 = runner.Runner('runner3')
        run_4=runner.Runner('runner4')
        for _ in range(10):
            run_3.run()
            run_4.walk()
        self.assertNotEqual(run_3.distance, run_4.distance)



if __name__ == '__main__':
    unittest.main()
