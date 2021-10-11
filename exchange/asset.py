from dataclasses import dataclass
from hamcrest import *

from exchange.balance import Balance


@dataclass
class Asset:
    """
    Exchange Asset

    """
    exchange: str
    symbol: str
    balance: Balance = None
    withdrawal_fee: float = 0
    withdrawal_min: float = 0
    withdrawal_step: float = 0

    def get_id(self) -> tuple:
        return self.exchange, self.symbol

    def __eq__(self, other):
        return other.get_id() == self.get_id()

    def __post_init__(self):
        assert_that(self.exchange, instance_of(str))
        self.exchange = self.exchange.upper()
        self.symbol = self.symbol.upper()
