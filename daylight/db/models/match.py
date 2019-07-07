from dataclasses import dataclass
from datetime import datetime


@dataclass
class Match:
    '''Model for a `Match` entity.
    '''

    first_user: int
    second_user: int
    match_date: datetime
