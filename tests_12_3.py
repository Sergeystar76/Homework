import unittest
import runner
import runner_and_tournament as rt

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        p1 = runner.Runner('Sergey')
        for i in range(10):
            p1.walk()
        self.assertEqual(p1.distance, 50)

    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        p2 = runner.Runner('Max')
        for i in range(10):
            p2.run()
        self.assertEqual(p2.distance, 100)

    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        p3 = runner.Runner('Anna')
        p4 = runner.Runner('Olya')
        for i in range(10):
            p3.run()
            p4.walk()

        self.assertNotEqual(p3.distance, p4.distance)
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.r1 = rt.Runner('Усэйн', 10)
        self.r2 = rt.Runner('Андрей', 9)
        self.r3 = rt.Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print({key: str(runner) for key, runner in result.items()})

    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def test_run_Nick_Usain(self):
        run1 = rt.Tournament(90, self.r1, self.r3)
        result1 = run1.start()
        last_place = list(result1.values())
        self.assertTrue(last_place[-1] == 'Ник')
        self.all_results['test_run_Nick_Usain'] = result1

    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def test_run_Andrey_Nick(self):
        run2 = rt.Tournament(90, self.r2, self.r3)
        result2 = run2.start()
        last_place = list(result2.values())
        self.assertTrue(last_place[-1] == 'Ник')
        self.all_results['test_run_Andrey_Nick'] = result2

    @unittest.skipIf( is_frozen,'Тесты в этом кейсе заморожены')
    def test_run_Usain_Andrey_Nick(self):
        run3 = rt.Tournament(90, self.r1, self.r2, self.r3)
        result3 = run3.start()
        last_place = list(result3.values())
        self.assertTrue(last_place[-1] == 'Ник')
        self.all_results['test_run_Usain_Andrey_Nick'] = result3
