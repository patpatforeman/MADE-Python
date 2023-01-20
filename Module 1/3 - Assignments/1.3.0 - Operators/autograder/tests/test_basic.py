import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
import student_submission as pp


class TestOperatorPP(unittest.TestCase):

    @weight(2)
    @number("1.1")
    def testfrst_num(self):
        self.assertIsNotNone(pp.first_number, "Did you change first_number's value?")
        self.assertAlmostEqual(pp.first_number, 64)

    @weight(2)
    @number("1.2")
    def testscnd_num(self):
        self.assertIsNotNone(pp.second_number, "Did you change second_number's value?")
        self.assertAlmostEqual(pp.second_number, 6.4)

    @weight(2)
    @number("1.3")
    def testthrd_num(self):
        self.assertIsNotNone(pp.third_number, "Did you change third_number's value?")
        self.assertAlmostEqual(pp.third_number, 68.4)

    @weight(2)
    @number("1.3")
    def testfrth_num(self):
        self.assertIsNotNone(pp.fourth_number, "Did you change fourth_number's value?")
        self.assertAlmostEqual(pp.fourth_number, 66.4)

    @weight(2)
    @number("1.4")
    def testsqwr_num1(self):
        self.assertIsNotNone(pp.squared_number_one, "Did you change squared_number_one's value?")
        self.assertAlmostEqual(pp.squared_number_one, 64)

    @weight(2)
    @number("1.5")
    def testsqwr_num2(self):
        self.assertIsNotNone(pp.squared_number_two, "Did you change squared_number_two's value?")
        self.assertAlmostEqual(pp.squared_number_two, 64.0)


if __name__ == '__main__':
    unittest.main()
