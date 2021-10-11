from dataclasses import dataclass
from enum import Enum

@dataclass
class Balance:
    """
    Asset Balance

    """
    exchange: str
    symbol: str
    available: float
    locked: float = 0.0

    def __post_init__(self):
        self.available = float(self.available)
