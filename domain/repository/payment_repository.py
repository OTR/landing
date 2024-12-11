from abc import ABC, abstractmethod

from domain.entity.payment import Payment


class PaymentRepository(ABC):

    @abstractmethod
    def get_payment_by_invoice_id(self, invoice_id: int) -> Payment:
        pass

    @abstractmethod
    def save(self, payment: Payment) -> int:
        pass
