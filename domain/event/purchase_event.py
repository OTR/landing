from dataclasses import dataclass

from domain.entity.invoice import Invoice
from domain.entity.payment import Payment
from domain.event.base_event import BaseEvent
from domain.vo.payment_method import PaymentMethod


@dataclass
class PurchaseEvent(BaseEvent):
    """
    invoice: Invoice
    payment: Payment
    amount_paid: int
    payment_method: str
    created_at: datetime
    """
    invoice: Invoice
    payment: Payment
    amount_paid: int
    payment_method: PaymentMethod

    def __str__(self):
        return (f"Purchase completed for Invoice #{self.invoice.invoice_id} with Payment "
                f"#{self.payment.payment_id}. Amount: {self.amount_paid}.")
