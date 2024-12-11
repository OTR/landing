from dataclasses import dataclass

from domain.entity.invoice import Invoice
from domain.event.base_event import BaseEvent


@dataclass
class InvoiceRefundedEvent(BaseEvent):
    """
    invoice: Invoice
    created_at: datetime
    """
    invoice: Invoice

    def __str__(self) -> str:
        return ""
