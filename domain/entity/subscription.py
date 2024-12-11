from datetime import datetime
from pydantic import BaseModel, Field,  model_validator
from typing_extensions import Self

from domain.entity.product import Product
from domain.entity.user import User
from domain.vo.subscription_status import SubscriptionStatus


class Subscription(BaseModel):
    subscription_id: int = Field(..., gt=0,
                                 description="The ID of the subscription (must be positive).")
    user: User
    product: Product
    start_date: datetime
    end_date: datetime
    status: SubscriptionStatus = SubscriptionStatus.ACTIVE

    @model_validator(mode="after")
    def validate_dates(self, info) -> Self:
        if self.end_date < self.start_date:
            raise ValueError(f"end_date ({self.end_date}) cannot be earlier"
                             f" than start_date ({self.start_date})")
        return self

    class Config:
        validate_assignment = True
        use_enum_values = False

    def __str__(self) -> str:
        return (f"Subscription #{self.subscription_id} - {self.product.name}"
                f" - Status: {self.status.value}")

    def cancel(self) -> None:
        self.status = SubscriptionStatus.CANCELLED

    def expire(self) -> None:
        self.status = SubscriptionStatus.EXPIRED
