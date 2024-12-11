from dataclasses import dataclass

from domain.entity.invoice import Invoice
from domain.entity.payment import Payment
from domain.event.base_event import BaseEvent


@dataclass
class PaymentSuccessEvent(BaseEvent):
    """
    payment: Payment
    invoice: Invoice
    created_at: datetime
    """
    payment: Payment
    invoice: Invoice

    def __str__(self) -> str:
        return ""
