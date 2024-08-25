import unittest
import rt_with_exceptions
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf8',
                    format='%(asctime)s | %(levelname)s: %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    try:
        def test_walk(self):
            test_runner = rt_with_exceptions.Runner(['hello'], -5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
    except ValueError as err:
        logging.warning("Неверная скорость для Runner", exc_info=True)

    try:
        def test_run(self):
            test_runner = rt_with_exceptions.Runner(['hello'])
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
    except TypeError as err:
        logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        test_runner1 = rt_with_exceptions.Runner('Patrick')
        test_runner2 = rt_with_exceptions.Runner('Frank')
        for i in range(10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


if __name__ == '__main__':
    unittest.main()
