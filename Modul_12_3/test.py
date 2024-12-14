import unittest
import modul_12_3

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_3.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(modul_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)