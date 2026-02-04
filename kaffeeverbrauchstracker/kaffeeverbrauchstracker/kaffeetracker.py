python

from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Dict

@dataclass(frozen=True)
class CoffeeEntry:
    day: date
    amount_ml: int
    kind: str = "coffee"

class CoffeeTracker:
    def __init__(self, daily_limit_count: int = 5) -> None:
        if daily_limit_count < 1:
            raise ValueError("daily_limit_count muss >= 1 sein")
        self._daily_limit_count = daily_limit_count
        self._entries: List[CoffeeEntry] = []
        
    def add_coffee(self, amount_ml: int, day: Optional[date] = None, kind: str = "coffee") -> None:
        if amount_ml <= 0:
            raise ValueError("amount_ml muss > 0 sein")
        if not kind or not kind.strip():
            raise ValueError("kind darf nicht leer sein")
            
    def entries_for_day(self, day: date):
         return [e for e in self._entries if e.day == day]

    def coffee_count_for_day(self, day: Optional[date] = None) -> int:
        entry_day = day or date.today()
        return len(self.entries_for_day(entry_day))
        
    def total_ml_for_day(self, day: Optional[date] = None) -> int:
        entry_day = day or date.today()
        return sum(e.amount_ml for e in self.entries_for_day(entry_day))
        
    def average_ml_for_day(self, day: Optional[date] = None) -> float:
        entry_day = day or date.today()
        entries = self.entries_for_day(entry_day)
        if not entries:
            return 0.0
        return self.total_ml_for_day(entry_day) / len(entries)

    def limit_exceeded_for_day(self, day: Optional[date] = None) -> bool:
        entry_day = day or date.today()
        return self.coffee_count_for_day(entry_day) > self._daily_limit_count

    def weekly_totals_ml(self, week_start: date):
        totals = {}
        for i in range(7):
            d = date.fromordinal(week_start.toordinal() + i)
            totals[d] = self.total_ml_for_day(d)
        return totals


          entry_day = day or date.today()
          self._entries.append(CoffeeEntry(day=entry_day, amount_ml=amount_ml, kind=kind.strip().lower()))
    








