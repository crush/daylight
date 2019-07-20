'''This module provides a low level abstraction representing all of the queries
with mutating functionality that higher level components should be allowed to
execute against the database.
'''

from dataclasses import dataclass
import enum
from typing import Any, List

import daylight.db.engine.query.security as security


class MutationId(enum.Enum):
    '''An internal representation of an identifier for a mutating query that
    can be executed.
    '''
    
    __REGISTER_USER = '__register_user__'


@dataclass
class Mutation:
    '''A package of everything required to execute a query understood by
    a `DaylightDB` that makes modifications to it.
    '''

    mutation_id: MutationId
    parameters: List[Any]


def register_user(email: str, password: str) -> Mutation:
    '''Create a `Query` that will insert a new user into the database.
    '''

    password = security.hash_password(password)
    return Mutation(MutationId.__REGISTER_USER, args=[email, password])
