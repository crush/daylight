from dataclasses import dataclass
from datetime import datetime


@dataclass
class Photo:
    '''Model for a `Photo` entity.
    '''

    id: int
    image_source: str
    owner: int
    upload_date: datetime
