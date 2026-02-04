python

from __future__ import annotations
from datacalsses import date
from typing import List, Optional

@dataclass(frozen=True)
class CoffeeEntry:
    day: date
    amount_ml: int
    kind: str = "coffee"
