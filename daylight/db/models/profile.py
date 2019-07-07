from dataclasses import dataclass


@dataclass
class Profile:
    '''Model for a `Profile` entity.
    '''

    owner: int
    display_name: str
    pronouns: str
    profile_photo: int
    biography: str
    account_type: int
