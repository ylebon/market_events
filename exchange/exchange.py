from dataclasses import dataclass
from hamcrest import *


@dataclass
class Exchange:
    """
    Exchange

    """
    name: str

    def to_string(self) -> str:
        return self.name.upper()

    def __post_init__(self):
        assert_that(self.name, matches_regexp("^[A-Z]+$"))
        self.name = self.name.upper()
