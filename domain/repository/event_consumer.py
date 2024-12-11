from abc import ABC, abstractmethod

from domain.repository.event_producer import E


class EventConsumer(ABC):

    @abstractmethod
    def consume(self) -> E:
        pass
