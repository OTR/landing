from enum import Enum


class PaymentMethod(Enum):
    ROBOKASSA = 'Robokassa'
    LAVATOP = 'Lava.Top'

    @classmethod
    def get_choices(cls):
        return [(method.name, method.value) for method in cls]

    def __str__(self) -> str:
        return self.value
