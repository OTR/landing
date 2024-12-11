from abc import ABC, abstractmethod

from domain.entity.invoice import Invoice


class InvoiceRepository(ABC):

    @abstractmethod
    def get_invoice_by_id(self, invoice_id: int) -> Invoice:
        pass

    @abstractmethod
    def save(self, invoice: Invoice) -> int:
        pass
