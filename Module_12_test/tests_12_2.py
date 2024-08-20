import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
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

    def test_tournament1(self):
        tournament = runner_and_tournament.Tournament(90, runner1, runner3)
        local_result = {}
        local_result.update(tournament.start())
        last = local_result[max(local_result.keys())]
        self.assertTrue(last == "Ник")
        all_results.append(local_result)

    def test_tournament2(self):
        tournament = runner_and_tournament.Tournament(90, runner2, runner3)
        local_result = {}
        local_result.update(tournament.start())
        last = local_result[max(local_result.keys())]
        self.assertTrue(last == "Ник")
        all_results.append(local_result)

    def test_tournament3(self):
        tournament = runner_and_tournament.Tournament(90, runner1, runner2, runner3)
        local_result = {}
        local_result.update(tournament.start())
        last = local_result[max(local_result.keys())]
        self.assertTrue(last == "Ник")
        all_results.append(local_result)


if __name__ == "__main__":
    unittest.main()