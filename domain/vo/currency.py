from enum import Enum


class Currency(Enum):
    USD = 'US Dollar'
    EUR = 'Euro'
    RUR = 'Russian Ruble'
    BTC = 'Bitcoin'
    USDT = 'Tether'
    TON = 'Toncoin'
    XTR = 'Telegram stars'

    @classmethod
    def get_choices(cls):
        return [(currency.name, currency.value) for currency in cls]

    def __str__(self) -> str:
        return self.value
