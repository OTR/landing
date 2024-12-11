from dataclasses import dataclass

from domain.entity.payment import Payment
from domain.event.base_event import BaseEvent


@dataclass
class PaymentCancelledEvent(BaseEvent):
    """
    payment: Payment
    created_at: datetime
    """
    payment: Payment

    def __str__(self) -> str:
        return ""
