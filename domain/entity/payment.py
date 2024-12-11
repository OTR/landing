from dataclasses import dataclass, field
from datetime import datetime

from domain.entity.invoice import Invoice
from domain.vo.payment_method import PaymentMethod
from domain.vo.payment_status import PaymentStatus


@dataclass
class Payment:
    """
    payment_id: int
    invoice: Invoice
    amount: int
    payment_method: PaymentMethod
    status: PaymentStatus
    payment_date: datetime
    retry_count: int = field(default=0)
    """
    payment_id: int
    invoice: Invoice
    amount: int
    payment_method: PaymentMethod
    status: PaymentStatus
    payment_date: datetime
    retry_count: int = field(default=0)

    def __post_init__(self):
        if not isinstance(self.payment_id, int):
            raise TypeError(f"payment_id must be an int, got {type(self.payment_id).__name__}")
        if not isinstance(self.invoice, Invoice):
            raise TypeError(f"invoice must be an instance of Invoice, got {type(self.invoice).__name__}")
        if not isinstance(self.amount, int):
            raise TypeError(f"amount must be an int, got {type(self.amount).__name__}")
        if not isinstance(self.payment_method, PaymentMethod):
            raise TypeError(f"payment_method must be an instance of PaymentMethod, got {type(self.payment_method).__name__}")
        if not isinstance(self.status, PaymentStatus):
            raise TypeError(f"status must be an instance of PaymentStatus, got {type(self.status).__name__}")
        if not isinstance(self.payment_date, datetime):
            raise TypeError(f"payment_date must be a datetime object, got {type(self.payment_date).__name__}")
        if not isinstance(self.retry_count, int):
            raise TypeError(f"retry_count must be an int, got {type(self.retry_count).__name__}")

    def __str__(self) -> str:
        return f"Payment #{self.payment_id} - {self.status} for {self.amount} {self.invoice.product.currency}"

    def increase_retry_count(self) -> None:
        self.retry_count += 1
