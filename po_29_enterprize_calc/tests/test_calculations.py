from unittest import TestCase
from po_29_enterprize_calc.buslog.calculations import Calculations


class TestCalculations(TestCase):

    def setUp(self) -> None:
        self.calculations = Calculations("../../data/calcs.csv")

    def test_plus(self):
        result = self.calculations.plus(3, 4)
        self.assertEqual(7, result)

    def test_minus(self):
        result = self.calculations.minus(4, 3)
        self.assertEqual(1, result)
