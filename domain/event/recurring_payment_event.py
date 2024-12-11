from dataclasses import dataclass

from domain.entity.payment import Payment
from domain.entity.subscription import Subscription
from domain.event.base_event import BaseEvent


@dataclass
class RecurringPaymentEvent(BaseEvent):
    """
    subscription: Subscription
    payment: Payment
    amount_paid: int
    status: str
    created_at: datetime
    """
    subscription: Subscription
    payment: Payment
    amount_paid: int
    status: str

    def __str__(self):
        return (
            f"Recurring payment processed for Subscription #{self.subscription.subscription_id},"
            f" Payment #{self.payment.payment_id} - {self.status}.")
