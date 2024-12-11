from abc import abstractmethod, ABC
from typing import TypeVar

from domain.event.base_event import BaseEvent

E = TypeVar("E", bound=BaseEvent)


class EventProducer(ABC):

    @abstractmethod
    def produce(self, event: E) -> None:
        raise NotImplementedError()
