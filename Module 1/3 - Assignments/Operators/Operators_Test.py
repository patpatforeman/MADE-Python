# unit test for week2_operator_pp
import unittest
import Operators as pp


class TestOperatorPP(unittest.TestCase):
    def testfrst_num(self):
        self.assertIsNotNone(pp.frst_num, "Did you change frst_num's value?")
        self.assertEqual(pp.frst_num, 64)

    def testscnd_num(self):
        self.assertIsNotNone(pp.scnd_num, "Did you change scnd_num's value?")
        self.assertEqual(pp.scnd_num, 6.4)

    def testthrd_num(self):
        self.assertIsNotNone(pp.thrd_num, "Did you change thrd_num's value?")
        self.assertEqual(pp.thrd_num, 68.4)

    def testfrth_num(self):
        self.assertIsNotNone(pp.frth_num, "Did you change frth_num's value?")
        self.assertEqual(pp.frth_num, 66.4)

    def testsqwr_num1(self):
        self.assertIsNotNone(pp.sqwr_num1, "Did you change sqwr_num1's value?")
        self.assertEqual(pp.sqwr_num1, 64)

    def testsqwr_num2(self):
        self.assertIsNotNone(pp.sqwr_num2, "Did you change sqwr_num2's value?")
        self.assertEqual(pp.sqwr_num2, 64.0)

    def testaccurate(self):
        self.assertIsNotNone(pp.accurate, "Did you change accurate's value?")
        self.assertEqual(pp.accurate, pp.sqwr_num2)


if __name__ == '__main__':
    unittest.main()
