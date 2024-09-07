import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        self.assertEqual(runner.p1.distance, 50)
    def test_run(self):
        self.assertEqual(runner.p2.distance, 100)
    def test_challenge(self):
            self.assertNotEqual(runner.p2.distance, runner.p1.distance)
if __name__ == "__main__":
    unittest.main()