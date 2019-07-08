from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Tuple

from daylight.db.models import User


@dataclass
class Match:
    '''Model for a `Match` entity.
    '''

    _first_user: int
    _second_user: int
    match_date: datetime


    def users(self) -> Optional[Tuple[User, User]]:
        '''Retrieve the `Users` whom are matched.
        '''

        return None
