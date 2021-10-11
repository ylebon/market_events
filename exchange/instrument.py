from dataclasses import dataclass
from hamcrest import *

from exchange.asset import Asset


@dataclass
class Instrument:
    """
    Instrument


    """
    exchange: str
    base: Asset
    quote: Asset
    exchange_code: str = ""
    step_size: float = None
    min_size: float = None
    max_size: float = None
    tick_size: float = None
    min_price: float = None
    max_price: float = None
    pip: float = None
    trade_fee: tuple = ()

    def __str__(self):
        return self.to_string()

    def get_id(self) -> tuple:
        return self.exchange.upper(), self.symbol.upper()

    def to_json(self) -> dict:
        return {}

    def to_string(self) -> str:
        return self.exchange.upper() + "_" + self.symbol.upper()

    @property
    def symbol(self) -> str:
        return f"{self.base.symbol}_{self.quote.symbol}"

    @property
    def float_round(self):
        if self.tick_size:
            x = format(self.tick_size, '.15f').rstrip("0")
            return len(x.split(".")[1])
        elif self.pip:
            x = format(self.pip, '.15f').rstrip("0")
            return len(x.split(".")[1])
        else:
            return None

    @property
    def step_price(self):
        return self.tick_size or self.pip or None

    def __post_init__(self):
        assert_that(self.exchange, instance_of(str))
        assert_that(self.base, instance_of(Asset))
        assert_that(self.quote, instance_of(Asset))
