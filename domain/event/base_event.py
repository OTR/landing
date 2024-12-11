from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEvent:
    """created_at: datetime"""
    created_at: datetime
