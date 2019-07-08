from dataclasses import dataclass
from typing import Optional

from daylight.db.models import User


@dataclass
class WomanFemmeAccountType:
    '''Model for a `WomanFemmeAccountType` entity.
    '''

    _owner: int


    def owner(self) -> Optional[User]:
        '''Retrieve the `User` owner of the account type in question.
        '''

        return None
