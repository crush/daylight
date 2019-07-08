from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from daylight.db.models import User


@dataclass
class Like:
    '''Model for the `Like` relation.
    '''

    _from_user: int
    _to_user: int
    send_date: datetime


    def from_user(self) -> Optional[User]:
        '''Retrieve the `User` that sent the like.
        '''

        return None
    
    
    def to_user(self) -> Optional[User]:
        '''Retrieve the `User` that the like was sent to.
        '''

        return None
