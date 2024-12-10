from enum import Enum


class PaymentStatus(Enum):
    PENDING = 'Pending'
    SUCCESS = 'Success'
    FAILED = 'Failed'

    @classmethod
    def get_choices(cls):
        return [(status.name, status.value) for status in cls]

    def __str__(self) -> str:
        return self.value
