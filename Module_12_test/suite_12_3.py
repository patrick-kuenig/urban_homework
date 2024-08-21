import unittest
import tests_12_1_new
import tests_12_2


runner_test_suite = unittest.TestSuite()
runner_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=tests_12_1_new.RunnerTest))
runner_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_test_suite)
