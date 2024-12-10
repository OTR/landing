from enum import Enum


class SubscriptionStatus(Enum):
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'
    EXPIRED = 'Expired'

    @classmethod
    def get_choices(cls):
        return [(status.name, status.value) for status in cls]

    def __str__(self) -> str:
        return self.value
