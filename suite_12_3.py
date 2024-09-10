import unittest
import tests_12_3 as rt

run_TS = unittest.TestSuite()
run_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(rt.TournamentTest))
run_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(rt.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_TS)