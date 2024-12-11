from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    """
    user_id: int
    username: str
    join_date: datetime
    full_name: Optional[str] = None
    """
    user_id: int
    username: str
    join_date: datetime
    full_name: Optional[str] = None

    _MIN_JOIN_YEAR: int = 2024
    _MAX_JOIN_YEAR: int = 2030

    def __post_init__(self):
        if not isinstance(self.user_id, int):
            raise TypeError(f"Expected user_id to be int, got {type(self.user_id).__name__}")
        if not isinstance(self.username, str):
            raise TypeError(f"Expected username to be str, got {type(self.username).__name__}")
        if not isinstance(self.join_date, datetime):
            raise TypeError(
                f"Expected join_date to be datetime, got {type(self.join_date).__name__}")
        if self.full_name is not None and not isinstance(self.full_name, str):
            raise TypeError(
                f"Expected full_name to be str or None, got {type(self.full_name).__name__}")
        if not (self._MIN_JOIN_YEAR <= self.join_date.year <= self._MAX_JOIN_YEAR):
            raise ValueError(f"join_date year must be between {self._MIN_JOIN_YEAR}"
                             f" and {self._MAX_JOIN_YEAR},"
                             f" got {self.join_date.year}")



    def __str__(self) -> str:
        return f"{self.username} ({self.full_name if self.full_name else 'N/A'})"
