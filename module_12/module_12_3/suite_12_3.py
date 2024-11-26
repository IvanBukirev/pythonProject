import unittest
from module_12.module_12_1 import module_12_1
from module_12.module_12_2 import tests_12_2
import tests_12_3

testST = unittest.TestSuite()
# testST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
# testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))



run = unittest.TextTestRunner(verbosity=2)
run.run(testST)
