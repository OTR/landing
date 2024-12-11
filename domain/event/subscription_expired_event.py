from dataclasses import dataclass

from domain.entity.subscription import Subscription
from domain.event.base_event import BaseEvent


@dataclass
class SubscriptionExpiredEvent(BaseEvent):
    """
    subscription: Subscription
    created_at: datetime
    """
    subscription: Subscription

    def __str__(self) -> str:
        return ""
