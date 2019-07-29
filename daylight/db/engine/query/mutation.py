'''This module provides a low level abstraction representing all of the queries
with mutating functionality that higher level components should be allowed to
execute against the database.
'''

from dataclasses import dataclass
import enum
import io
from typing import Any, List, Union

import daylight.db.engine.query.security as security
import daylight.db.models as models


class MutationId(enum.Enum):
    '''An internal representation of an identifier for a mutating query that
    can be executed.
    '''
    
    REGISTER_USER = '__register_user__'
    RESET_PASSWORD = '__reset_password__'
    DELETE_USER = '__delete_user__'
    REVOKE_LIKE = '__revoke_like__'
    SEND_LIKE = '__send_like__'
    ESTABLISH_MATCH = '__establish_match__'
    UNMATCH = '__unmatch__'
    DELETE_PHOTO = '__delete_photo__'
    UPLOAD_PHOTO = '__upload_photo__'
    UPDATE_PROFILE = '__update_profile__'
    SET_TAGS = '__set_tags__'


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
    return Mutation(MutationId.REGISTER_USER, [email, password])


def reset_password(updated_user: models.User) -> Mutation:
    '''Create a `Mutation` to update a user's password with a secure hash of a
    new password.
    '''

    new_password = security.hash_password(new_password)
    return Mutation(MutationId.RESET_PASSWORD, [user, new_password])


def delete_user_account(user: models.User) -> Mutation:
    '''Create a `Mutation` that will completely delete a user account
    and all related data.
    '''

    return Mutation(MutationId.DELETE_USER, [user])


def establish_match(from_user: models.User, to_user: models.User) -> Mutation:
    '''Create a `Mutation` that creates a match between two users.
    '''

    return Mutation(MutationId.MATCH_USERS, [from_user, to_user])


def unmatch(match: models.Match) -> Mutation:
    '''Create a `Mutation` that will delete a match between two users.
    '''

    return Mutation(MutationId.UNMATCH, [match])


def revoke_like(like: models.Like) -> Mutation:
    '''Create a `Mutation` that revokes a like from one user to another.
    '''

    return Mutation(MutationId.REVOKE_LIKE, [like])


def send_like(fr: models.User, to: models.User) -> Mutation:
    '''Create a `Mutation` that registers a like sent from one user to another.
    '''

    return Mutation(MutationId.SEND_LIKE, [fr, to])


def establish_match(fr: models.User, to: models.User) -> Mutation:
    '''Create a `Mutation` that registers two users as matched.
    '''

    return Mutation(MutationId.ESTABLISH_MATCH, [fr, to])


def unmatch(match: models.Match) -> Mutation:
    '''Create a `Mutation` that deletes a match.
    '''

    return Mutation(MutationId.UNMATCH, [match])


def delete_photo(photo: models.Photo) -> Mutation:
    '''Create a `Mutation` that deletes a photo.
    '''

    return Mutation(MutationId.DELETE_PHOTO, [photo])


def upload_photo(user: models.User, photo_b64: io.BytesIO) -> Mutation:
    '''Create a `Mutation` that uploads a photo to a user's profile.
    '''

    return Mutation(MutationId.UPLOAD_PHOTO, [user, photo_b64])


def update_profile(profile: models.Profile) -> Mutation:
    '''Create a `Mutation` that updates a user's profile.
    '''

    return Mutation(MutationId.UPDATE_PROFILE, [profile])


def set_tags(user: models.User, tags: List[models.Tag]) -> Mutation:
    '''Create a `Mutation` that sets the tags associated with a user's profile.
    '''

    return Mutation(MutationId.SET_TAGS, [user, tags])
