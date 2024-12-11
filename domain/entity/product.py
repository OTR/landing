from dataclasses import dataclass

from domain.vo.currency import Currency
from domain.vo.recurring_period import RecurringPeriod


@dataclass
class Product:
    """
    product_id: int
    name: str
    description: str
    base_price: int
    currency: Currency
    is_recurring: bool
    recurring_period: RecurringPeriod
    is_available: bool = True
    """
    product_id: int
    name: str
    description: str
    base_price: int
    currency: Currency
    is_recurring: bool
    recurring_period: RecurringPeriod
    is_available: bool = True

    def __post_init__(self):
        if not isinstance(self.product_id, int):
            raise TypeError(f"Expected product_id to be int, got {type(self.product_id).__name__}")
        if not isinstance(self.name, str):
            raise TypeError(f"Expected name to be str, got {type(self.name).__name__}")
        if not isinstance(self.description, str):
            raise TypeError(f"Expected description to be str, got {type(self.description).__name__}")
        if not isinstance(self.base_price, int):
            raise TypeError(f"Expected base_price to be int, got {type(self.base_price).__name__}")
        if not isinstance(self.currency, Currency):
            raise TypeError(f"Expected currency to be Currency, got {type(self.currency).__name__}")
        if not isinstance(self.is_recurring, bool):
            raise TypeError(f"Expected is_recurring to be bool, got {type(self.is_recurring).__name__}")
        if not isinstance(self.recurring_period, RecurringPeriod):
            raise TypeError(f"Expected recurring_period to be RecurringPeriod, got {type(self.recurring_period).__name__}")
        if not isinstance(self.is_available, bool):
            raise TypeError(f"Expected is_available to be bool, got {type(self.is_available).__name__}")
        if self.product_id <= 0:
            raise ValueError(f"product_id must be a positive integer, got {self.product_id}")

    def __str__(self):
        return f"Product: {self.name} ({self.currency}) - {self.base_price} {self.currency}"
