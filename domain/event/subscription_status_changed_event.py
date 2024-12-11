from dataclasses import dataclass

from domain.vo.subscription_status import SubscriptionStatus
from domain.event.base_event import BaseEvent


@dataclass
class SubscriptionStatusChangedEvent(BaseEvent):
    """
    subscription_id: int
    old_status: SubscriptionStatus
    new_status: SubscriptionStatus
    created_at: datetime
    """
    subscription_id: int
    old_status: SubscriptionStatus
    new_status: SubscriptionStatus

    def __str__(self) -> str:
        return ""
