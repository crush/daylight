from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from daylight.db.models import User


@dataclass
class Photo:
    '''Model for a `Photo` entity.
    '''

    _id: int
    image_source: str
    _owner: int
    upload_date: datetime


    def owner(self) -> Optional[User]:
        '''Retrieve the `User` that owns the photo.
        '''

        return None
