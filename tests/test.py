from thad_roberts_model import *

ThadRobertsModel().verify()

import unittest
        
class TestMeasuremente(unittest.TestCase):
    
    
    def test_measurements_equality(self):
        self.assertEqual(Measurement("4.100", "0.04", "1000") == Measurement("4180", "70"), True)
        self.assertEqual(Measurement("4180", "70") == Measurement("4.100", "0.04", "1000"), True)
        self.assertEqual(Measurement("4180", "30") == Measurement("4.100", "0.04", "1000"), False)
        self.assertEqual(Measurement("4180", "30") != Measurement("4.100", "0.04", "1000"), True)
    
    def test_arithmetics(self):
        self.assertEqual(v("2")*Measurement("4.10", "0.04"), Measurement("8.20", "0.08"))
        self.assertEqual(Measurement("4.0", "0.04")*Measurement("4.0", "0.04"), Measurement("16.0", "0.08"))
        self.assertEqual(Measurement("4.0", "0.04")/Measurement("4.0", "0.04"), Measurement("1.0", "0.08"))
        self.assertEqual(Measurement("4.10", "0.04") + Measurement("4.10", "0.04"), Measurement("8.20", "0.08"))
        self.assertEqual(Measurement("4.10", "0.04") - Measurement("4.25", "0.04"), Measurement("-0.15", "0.08"))
        self.assertEqual(-Measurement("4.10", "0.04"), Measurement("-4.10", "0.04"))
        self.assertEqual(+Measurement("4.10", "0.04"), Measurement("4.10", "0.04"))
        self.assertEqual(Measurement("4.0", "0.04")**v("2"), Measurement("16", "0.08"))


