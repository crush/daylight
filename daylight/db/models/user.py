from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    '''Model for a `User` entity.
    '''

    _id: int
    email: str
    password_hash: str
    join_date: datetime
