# tests the final balance of the account after interest
# this unittest would be identical to the one used by math package
import unittest
import Building_Formulas


class TestFormulas(unittest.TestCase):
    def test_calc_final(self):
        Building_Formulas.calc_final()
        self.assertEqual(Building_Formulas.get_final(), 1104.6221254112045)


if __name__ == '__main__':
    unittest.main()