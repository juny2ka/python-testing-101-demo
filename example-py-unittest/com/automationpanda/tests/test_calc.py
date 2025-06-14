import sys

from com.automationpanda.example.calc import Calculator



# NUMBER_1 = 20.0
# NUMBER_2 = 2.0
# FAILURE = 'incorrect value'


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0.0, FAILURE)

    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 12.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 8.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -8.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_multiply(self):
        value = self.calc.multiply(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 20.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5.0, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)

    def test_max_greater(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_max_less(self):
        value = self.calc.maximum(NUMBER_2, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_max_equal(self):
        value = self.calc.maximum(NUMBER_1, NUMBER_1)
        self.assertEqual(value, NUMBER_1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_greater(self):
        value = self.calc.minimum(NUMBER_1, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_less(self):
        value = self.calc.minimum(NUMBER_2, NUMBER_1)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_min_equal(self):
        value = self.calc.minimum(NUMBER_2, NUMBER_2)
        self.assertEqual(value, NUMBER_2, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
