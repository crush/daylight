'''This module provides a low level abstraction representing all of the queries
that higher level components should be allowed to execute against the database.
'''

from dataclasses import dataclass
import enum
from typing import Any, List


class QueryId(enum.Enum):
    '''An internal representation of an identifier for a search query that
    can be executed.
    '''

    __RETRIEVE_USER_BY_ID = '__retrieve_user_by_id__'


@dataclass
class Query:
    '''A package of everything required to execute a search query understood
    by a `DaylightDB`.
    '''

    query_id: QueryId
    parameters: List[Any]


def retrieve_user(user_id: str) -> Query:
    '''Create a `Query` capble of searching for a specific user.
    '''

    return Query(QueryId.__RETRIEVE_USER_BY_ID, args=[user_id])
