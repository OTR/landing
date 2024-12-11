from abc import ABC, abstractmethod

from domain.entity.subscription import Subscription


class SubscriptionRepository(ABC):

    @abstractmethod
    def get_subscription_by_user_id(self, user_id: int) -> Subscription:
        pass

    @abstractmethod
    def save(self, subscription: Subscription) -> int:
        pass

    @abstractmethod
    def get_subscription_by_id(self, subscription_id: int) -> Subscription:
        pass
