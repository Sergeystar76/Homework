import unittest

import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = rt.Runner('Усэйн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(runner) for key, runner in result.items()})

    def test_run_Nick_Usain(self):
        run1 = rt.Tournament(90, self.r1, self.r3)
        result1 = run1.start()
        last_place = list(result1.values())
        self.assertTrue(last_place[-1] == 'Ник')
        self.all_results['test_run_Nick_Usain'] = result1

    def test_run_Andrey_Nick(self):
        run2 = rt.Tournament(90, self.r2, self.r3)
        result2 = run2.start()
        last_place = list(result2.values())
        self.assertTrue(last_place[-1] == 'Ник')
        self.all_results['test_run_Andrey_Nick'] = result2

    def test_run_Usain_Andrey_Nick(self):
        run3 = rt.Tournament(90, self.r1, self.r2, self.r3)
        result3 = run3.start()
        last_place = list(result3.values())
        self.assertTrue(last_place[-1] == 'Ник')
        self.all_results['test_run_Usain_Andrey_Nick'] = result3
