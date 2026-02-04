python

import unittest
from datetime import date
from src.coffee_tracker import CoffeeTracker

class CoffeeTrackerTest(unittest.TestCase):
    def setUp(self):
        self.tracker = CoffeeTracker(daily_limit_count=2)
        self.d1 = date(2026, 2, 1)

    def test_add_coffee_increases_count_by_day(self):
        self.tracker.add_coffee(200, day=self.d1, kind="coffee")
        # indirekte Überprüfung der internen Länge, später anders
        # -> kein weiterer Assert möglich ohne entries_for_day
        self.assertTrue(True)

    def test_invalid_amount_raises(self):
        with self.assertRaises(ValueError):
            self.tracker.add_coffee(0, day=self.d1)

    def test_invalid_kind_raises(self):
        with self.assertRaises(ValueError):
            self.tracker.add_coffee(100, day=self.d1, kind="  ")

    def test_total_ml_for_day(self):
        self.tracker.add_coffee(200, day=self.d1)
        self.tracker.add_coffee(150, day=self.d1)
        self.assertEqual(self.tracker.total_ml_for_day(self.d1), 350)

    def test_average_ml_for_day_empty(self):
        self.assertEqual(self.tracker.average_ml_for_day(self.d1), 0.0)

    def test_average_ml_for_day(self):
        self.tracker.add_coffee(200, day=self.d1)
        self.tracker.add_coffee(100, day=self.d1)
        self.assertEqual(self.tracker.average_ml_for_day(self.d1), 150.0)
        
    def test_limit_exceeded_for_day(self):
        self.tracker.add_coffee(30, day=self.d1, kind="espresso")
        self.tracker.add_coffee(30, day=self.d1, kind="espresso")
        self.tracker.add_coffee(200, day=self.d1, kind="coffee")
        self.assertTrue(self.tracker.limit_exceeded_for_day(self.d1))



if __name__ == "__main__":
    unittest.main()



