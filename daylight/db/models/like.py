from dataclasses import dataclass
from datetime import datetime


@dataclass
class Like:
    '''Model for the `Like` relation.
    '''

    from_user: int
    to_user: int
    send_date: datetime
