import unittest
from time_calculator import TimeCalculator

class TestTimeCalculator(unittest.TestCase):
    def test_to_seconds(self):
        calc = TimeCalculator(hours=1, minutes=1, seconds=1)
        self.assertEqual(calc.to_seconds(), 3661)

    def test_to_minutes(self):
        calc = TimeCalculator(hours=1, minutes=0, seconds=0)
        self.assertEqual(calc.to_minutes(), 60)

    def test_to_hours(self):
        calc = TimeCalculator(hours=2, minutes=0, seconds=0)
        self.assertEqual(calc.to_hours(), 2)

if __name__ == '__main__':
    unittest.main()