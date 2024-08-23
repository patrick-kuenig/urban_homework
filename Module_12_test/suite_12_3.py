import unittest
import tests_12_3

runner_test_suite = unittest.TestSuite()
runner_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=tests_12_3.RunnerTest))
runner_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_test_suite)
