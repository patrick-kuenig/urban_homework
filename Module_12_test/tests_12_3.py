import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        test_runner = runner.Runner('Patrick')
        for i in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        test_runner = runner.Runner('Patrick')
        for i in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        test_runner1 = runner.Runner('Patrick')
        test_runner2 = runner.Runner('Frank')
        for i in range(10):
            test_runner1.walk()
            test_runner2.run()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        global all_results
        all_results = []

    def setUp(self):
        global runner1
        global runner2
        global runner3
        runner1 = runner_and_tournament.Runner("Усейн", 10)
        runner2 = runner_and_tournament.Runner("Андрей", 9)
        runner3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(self):
        for dict_ in all_results:
            print(dict_)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament1(self):
        tournament = runner_and_tournament.Tournament(90, runner1, runner3)
        local_result = {}
        local_result.update(tournament.start())
        last = local_result[max(local_result.keys())]
        self.assertTrue(last == "Ник")
        all_results.append(local_result)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament2(self):
        tournament = runner_and_tournament.Tournament(90, runner2, runner3)
        local_result = {}
        local_result.update(tournament.start())
        last = local_result[max(local_result.keys())]
        self.assertTrue(last == "Ник")
        all_results.append(local_result)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_tournament3(self):
        tournament = runner_and_tournament.Tournament(90, runner1, runner2, runner3)
        local_result = {}
        local_result.update(tournament.start())
        last = local_result[max(local_result.keys())]
        self.assertTrue(last == "Ник")
        all_results.append(local_result)


if __name__ == "__main__":
    unittest.main()
