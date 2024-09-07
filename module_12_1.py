import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        p1 = runner.Runner('Sergey')
        for i in range(10):
            p1.walk()
        self.assertEqual(p1.distance, 50)

    def test_run(self):
        p2 = runner.Runner('Max')
        for i in range(10):
            p2.run()
        self.assertEqual(p2.distance, 100)
    def test_challenge(self):
        p3 = runner.Runner('Anna')
        p4 = runner.Runner('Olya')
        for i in range(10):
            p3.run()
            p4.walk()

        self.assertNotEqual(p3.distance, p4.distance)
if __name__ == "__main__":
    unittest.main()