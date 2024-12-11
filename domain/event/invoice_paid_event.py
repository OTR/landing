from dataclasses import dataclass

from domain.entity.invoice import Invoice
from domain.entity.payment import Payment
from domain.event.base_event import BaseEvent


@dataclass
class InvoicePaidEvent(BaseEvent):
    """
    invoice: Invoice
    payment: Payment
    created_at: datetime
    """
    invoice: Invoice
    payment: Payment

    def __str__(self) -> str:
        return ""
