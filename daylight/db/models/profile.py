from dataclasses import dataclass
from typing import Optional, Union

from daylight.db.models import\
    ManMascAccountType, Photo, User, WomanFemmeAccountType


PossibleAccountType = Optional[Union[WomanFemmeAccountType, ManMascAccountType]]


@dataclass
class Profile:
    '''Model for a `Profile` entity.
    '''

    _owner: int
    display_name: str
    pronouns: str
    _profile_photo: int
    biography: str
    _account_type: int


    def owner(self) -> Optional[User]:
        '''Retrieve the `User` owner of the profile.
        '''

        return None


    def profile_photo(self) -> Optional[Photo]:
        '''Retrieve the `Photo` that serves as the main account picture.
        '''

        return None


    def account_type(self) -> PossibleAccountType:
        '''Retrieve the account type of a profile.
        Account types can either be a `WomanFemmeAccountType` or a
        `ManMascAccountType`.
        '''

        return None
