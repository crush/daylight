from dataclasses import dataclass, field
from typing import Optional

from daylight.db.models import User


@dataclass
class ManMascAccountType:
    '''Model for a `ManMascAccountType` entity.
    '''

    _owner: int
    num_ratings: int = field(default=0)
    respectfulness_score: int = field(default=0)
    knowledgeable_score: int = field(default=0)
    supportiveness_score: int = field(default=0)


    def owner(self) -> Optional[User]:
        '''Retrieve the `User` owner of the account type.
        '''

        return None
