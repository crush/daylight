from dataclasses import dataclass


@dataclass
class Tag:
    '''Model for a `Tag` entity.
    '''

    tag: str


AllowedTags = [
    Tag('bondage'),
    Tag('cosplay')
]
