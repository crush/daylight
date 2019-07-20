'''This module provides a low level abstraction representing all of the queries
with mutating functionality that higher level components should be allowed to
execute against the database.
'''

from dataclasses import dataclass
import enum
from typing import Any, List, Union

import daylight.db.engine.query.security as security
import daylight.db.models as models


class MutationId(enum.Enum):
    '''An internal representation of an identifier for a mutating query that
    can be executed.
    '''
    
    __REGISTER_USER = '__register_user__'
    __RESET_PASSWORD = '__reset_password__'
    __DELETE_USER = '__delete_user__'
    __MATCH_USERS = '__match_users__'
    __UNMATCH = '__unmatch__'
    __UPDATE_PROFILE = '__update_user_profile__'
    __SET_TAGS = '__set_tags__'
    __UPLOAD_PHOTO = '__upload_photo__'
    __REMOVE_PHOTO = '__remove_photo__'


AccountType = Union[models.WomanFemmeAccountType, models.ManMascAccountType]


@dataclass
class Mutation:
    '''A package of everything required to execute a query understood by
    a `DaylightDB` that makes modifications to it.
    '''

    mutation_id: MutationId
    parameters: List[Any]


def register_user(
        email: str,
        password: str,
        account_type: AccountType,
        ) -> Mutation:
    '''Create a `Mutation` that will insert a new user into the database.
    '''

    password = security.hash_password(password)
    return Mutation(MutationId.__REGISTER_USER, [email, password, account_type])


def reset_password(updated_user: models.User) -> Mutation:
    '''Create a `Mutation` to update a user's password with a secure hash of a
    new password.
    '''

    new_password = security.hash_password(new_password)
    return Mutation(MutationId.__RESET_PASSWORD, [user_id, new_password])


def delete_user_account(user: models.User) -> Mutation:
    '''Create a `Mutation` that will completely delete a user account
    and all related data.
    '''

    return Mutation(MutationId.__DELETE_USER, [user_id])


def establish_match(from_user_id: int, to_user_id: int) -> Mutation:
    '''Create a `Mutation` that creates a match between two users.
    '''

    return Mutation(MutationId.__MATCH_USERS, [from_user_id, to_user_id])


def unmatch(match: models.Match) -> Mutation:
    '''Create a `Mutation` that will delete a match between two users.
    '''

    return Mutation(MutationId.__UNMATCH, [from_user_id, to_user_id])


def update_user_profile(updated_profile: models.Profile) -> Mutation:
    '''Create a `Mutation` that updates all of the fields in a user's profile.
    '''

    return Mutation(MutationId.__UPDATE_PROFILE, [updated_profile])


def set_user_profile_tags(
        user: models.User,
        tags: List[models.Tag]
        ) -> Mutation:
    '''Create a `Mutation` that will set the tags associated with a user's
    profile.
    '''

    return Mutation(MutationId.__SET_TAGS, [user, tags])


def upload_photo_to_profile(
        profile: models.Profile,
        photo_src: str
        ) -> Mutation:
    '''Create a `Mutation` that will relate a new photo to a user's profile.
    '''

    return Mutation(MutationId.__UPLOAD_PHOTO, [profile, photo_src])


def remove_photo_from_profile(
        profile: models.Profile,
        photo: models.Photo
        ) -> Mutation:
    '''Create a `Mutation` that will remove a photo from a user's profile.
    '''
    
    return Mutation(MutationId.__REMOVE_PHOTO, [profile, photo])


def set_profile_picture(
        profile: models.Profile,
        photo: models.Photo
        ) -> Mutation:
    '''Create a `Mutation` to set a particular photo as a user's profile
    picture.
    '''

    return Mutation(MutationId.__SET_PROFILE_PIC, [profile, photo])
