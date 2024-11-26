import logging
import unittest
import rt_with_exceptions as rt


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s --- %(levelname)s --- %(message)s')



    def test_walk(self):
        try:
            run_1 = rt.Runner('runner',-5 )
            for _ in range(10):
                run_1.walk()
            self.assertEqual(run_1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'"Неверная скорость для Runner"', exc_info=True)


    def test_run(self):
        try:
            run_2 = rt.Runner(123)
            for _ in range(10):
                run_2.run()
            self.assertEqual(run_2.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',exc_info=True)


    def test_challenge(self):
        run_3 = rt.Runner('runner3')
        run_4 = rt.Runner('runner4')
        for _ in range(10):
            run_3.run()
            run_4.walk()
        self.assertNotEqual(run_3.distance, run_4.distance)


if __name__ == '__main__':
    unittest.main()
