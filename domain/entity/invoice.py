from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from domain.entity.product import Product
from domain.entity.user import User
from domain.vo.payment_status import PaymentStatus


@dataclass
class Invoice:
    invoice_id: int
    user: User
    product: Product
    issued_at: datetime
    status: PaymentStatus = PaymentStatus.PENDING
    payment_date: Optional[datetime] = None

    _MIN_ISSUED_YEAR: int = 2024
    _MAX_ISSUED_YEAR: int = 2030

    def __post_init__(self):
        if not isinstance(self.invoice_id, int):
            raise TypeError(f"Expected invoice_id to be int, got {type(self.invoice_id).__name__}")
        if not isinstance(self.user, User):
            raise TypeError(f"Expected user to be User, got {type(self.user).__name__}")
        if not isinstance(self.product, Product):
            raise TypeError(f"Expected product to be Product, got {type(self.product).__name__}")
        if not isinstance(self.issued_at, datetime):
            raise TypeError(
                f"Expected issued_at to be datetime, got {type(self.issued_at).__name__}")
        if not isinstance(self.status, PaymentStatus):
            raise TypeError(
                f"Expected status to be PaymentStatus, got {type(self.status).__name__}")
        if self.payment_date is not None and not isinstance(self.payment_date, datetime):
            raise TypeError(
                f"Expected payment_date to be datetime or None,"
                f" got {type(self.payment_date).__name__}")

        if not (self._MIN_ISSUED_YEAR <= self.issued_at.year <= self._MAX_ISSUED_YEAR):
            raise ValueError(f"issued_at year must be between {self._MIN_ISSUED_YEAR}"
                             f" and {self._MAX_ISSUED_YEAR},"
                             f" got {self.issued_at.year}")

    def __str__(self) -> str:
        return f"Invoice #{self.invoice_id} - {self.product.name} - Status: {self.status}"

    def mark_as_paid(self, status: PaymentStatus, payment_date: datetime) -> None:
        if not isinstance(status, PaymentStatus):
            raise TypeError(f"Expected status to be PaymentStatus, got {type(status).__name__}")
        if not isinstance(payment_date, datetime):
            raise TypeError(
                f"Expected payment_date to be datetime, got {type(payment_date).__name__}")

        self.status = status
        self.payment_date = payment_date
