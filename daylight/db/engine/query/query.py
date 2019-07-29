'''This module provides a low level abstraction representing all of the queries
that higher level components should be allowed to execute against the database.
'''

from dataclasses import dataclass
import enum
from typing import Any, List, Union, Union

import daylight.db.models as models


class QueryId(enum.Enum):
    '''An internal representation of an identifier for a search query that
    can be executed.
    '''

    RETRIEVE_USER_BY_ID = '__retrieve_user_by_id__'
    RETRIEVE_PHOTOS = '__retrieve_profile_photos__'
    RETRIEVE_MATCHES = '__retrieve_matches__'
    RETRIEVE_PROFILE = '__retrieve_profile__'
    RETRIEVE_TAGS = '__retrieve_tags__'
    RETRIEVE_ACCOUNT_TYPE = '__retrieve_account_type'


@dataclass
class Query:
    '''A package of everything required to execute a search query understood
    by a `DaylightDB`.
    '''

    query_id: QueryId
    parameters: List[Any]


AccountType = Union[models.WomanFemmeAccountType, models.ManMascAccountType]


def retrieve_user(user_id: int) -> Query:
    '''Create a `Query` capble of searching for a specific user.
    '''

    return Query(QueryId.RETRIEVE_USER_BY_ID, [user_id])


def retrieve_matches_for_user(user: models.User) -> Query:
    '''Create a `Query` to fetch all matches a user has.
    '''

    return Query(QueryId.RETRIEVE_MATCHES_FOR_USER, [user])


def retrieve_user_profile(user: models.User) -> Query:
    '''Create a `Query` that retrieves the profile information for a user.
    '''

    return Query(QueryId.RETRIEVE_USER_PROFILE, [user])


def retrieve_user_tags(user: models.User) -> Query:
    '''Create a `Query` that will retrieve the tags describing a user's
    profile.
    '''

    return Query(QueryId.RETRIEVE_TAGS, [user])


def retrieve_user_photos(user: models.User) -> Query:
    '''Create a `Query` to retrieve the photos associated with a user's
    profile.
    '''

    return Query(QueryId.RETRIEVE_PHOTOS, [user])


def retrieve_typed_profile(profile: models.Profile) -> Query:
    '''Create a `Query` that will retrieve the extra profile information
    associated with each of the different types of profiles supported.
    '''

    return Query(QueryId.RETRIEVE_TYPED_PROFILE, [profile])


def retrieve_profile(user: models.User) -> Query:
    '''Create a `Query` that will retrieve a user's profile information.
    '''

    return Query(QueryId.RETRIEVE_PROFILE, [user])


def retrieve_tags(user: models.User) -> Query:
    '''Create a `Query` that will retrieve a list of tags associated with a
    user's profile.
    '''

    return Query(QueryId.RETRIEVE_TAGS, [user])


def retrieve_matches(user: models.User) -> Query:
    '''Create a `Query` that will retrieve a list of a user's matches.
    '''

    return Query(QueryId.RETRIEVE_MATCHES, [user])


def retrieve_photos(user: models.User) -> Query:
    '''Create a `Query` that will retrieve a list of photos uploaded to a
    user's account.
    '''

    return Query(QueryId.RETRIEVE_PHOTOS, [user])


def retrieve_account_type(profile: models.Profile) -> Query:
    '''Create a `Query` that retrieve the additional account type-specific
    information associated with a user's profile.
    '''

    return Query(QueryId.RETRIEVE_ACCOUNT_TYPE, [profile])
