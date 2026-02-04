python

from __future__ import annotations
from datacalsses import date
from typing import List, Optional

@dataclass(frozen=True)
class CoffeeEntry:
    day: date
    amount_ml: int
    kind: str = "coffee"

class CoffeeTracker;
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



