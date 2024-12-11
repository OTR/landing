from dataclasses import dataclass
from datetime import datetime

from domain.entity.subscription import Subscription
from domain.event.base_event import BaseEvent


@dataclass
class SubscriptionRenewalEvent(BaseEvent):
    """
    subscription: Subscription
    new_end_date: datetime
    created_at: datetime
    """
    subscription: Subscription
    new_end_date: datetime

    def __str__(self):
        return (f"Subscription #{self.subscription.subscription_id} renewed."
                f" New end date: {self.new_end_date}.")
