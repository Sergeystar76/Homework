import logging
import unittest
import rt_with_exceptions as rt

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = rt.Runner('Sergey', -5)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            runner = rt.Runner(25)
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)



    def test_challenge(self):
        p3 = rt.Runner('Anna')
        p4 = rt.Runner('Olya')
        for i in range(10):
            p3.run()
            p4.walk()
        self.assertNotEqual(p3.distance, p4.distance)

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")



