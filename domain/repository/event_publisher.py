from abc import ABC, abstractmethod


class EventPublisher(ABC):

    @abstractmethod
    def emit(self, purchase_event) -> None:
        pass
