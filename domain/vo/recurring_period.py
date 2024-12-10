from enum import Enum


class RecurringPeriod(Enum):
    DAILY = 1
    WEEKLY = 7
    MONTHLY = 30
    YEARLY = 365

    @classmethod
    def get_choices(cls):
        return [(period.name, period.value) for period in cls]

    def __str__(self) -> str:
        return str(self.value)

    def get_days(self) -> int:
        return self.value
