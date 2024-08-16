import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = runner.Runner('Patrick')
        for i in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        test_runner = runner.Runner('Patrick')
        for i in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner1 = runner.Runner('Patrick')
        test_runner2 = runner.Runner('Frank')
        for i in range(10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


if __name__ == '__main__':
    unittest.main()
# Ran 3 tests in 0.058s
#
# OK
