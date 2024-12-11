from dataclasses import dataclass

from domain.entity.subscription import Subscription
from domain.event.base_event import BaseEvent


@dataclass
class SubscriptionCancelledEvent(BaseEvent):
    """
    subscription: Subscription
    created_at: datetime
    """
    subscription: Subscription

    def __str__(self):
        return f"Subscription #{self.subscription.subscription_id} cancelled on {self.created_at}."
