from abc import ABC, abstractmethod

from domain.entity.product import Product


class ProductRepository(ABC):

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def save(self, product: Product) -> int:
        pass
