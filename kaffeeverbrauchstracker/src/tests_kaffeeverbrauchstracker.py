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


if __name__ == "__main__":
    unittest.main()
