'''Exports `DaylightDB` which provides the foundation for the execution of
queries against the database.
'''

import enum
from typing import Optional

import psycopg2 as postgres

from daylight.db.engine.query import Mutation, Query
from daylight.db.engine.tables import create_tables


class DBErrorKind(enum.Enum):
    '''Enumerates all of the errors that a `DaylightDB` may raise.
    '''

    CONNECTION_ERROR = 'CONNECTION ERROR' 


class DBError(Exception):
    '''Errors that may be raised by the `DaylightDB`.
    '''

    def __init__(self, kind: DBErrorKind, msg: str):
        self.message = f'Database error: {kind}: {msg}'
        

class DaylightDB:
    '''The primary abstraction over a connection to a Postgres database.
    It consumes `Query` and `Mutation` instances to search for and manipulate
    data in Postgres.
    '''

    def __init__(self, postgres_url: str):
        self._conn_url: str = postgres_url
        self._connection: Optional[postgres.connection] = None


    def connect_to_backend(self):
        '''Attempt to establish a connection to the underlying persistence
        medium.  This function must be called before any actual work can be
        done by the database.  In the event that a connection cannot be
        established, a `DBError` will be raised.

        In order to release the connection, the `disconnect()` method must be
        called.

        Calling this multiple times before calling `disconnect()` will not have
        any affect beyond the first initialization of the connection.
        '''

        if self._connection is not None:
            return

        try:
            self._connection = postgres.connect(self._conn_url)

            with self._connection.cursor() as cursor:
                create_tables(cursor)

        except postgres.ProgrammingError:
            raise DBError(DBErrorKind.CONNECTION_ERROR, 'invalid connection string')

        except postgres.OperationalError as err:
            raise DBError(
                    DBErrorKind.CONNECTION_ERROR,
                    f'failed to connect: {err.message}')


    def disconnect(self):
        '''Disconnect from the underlying persistence medium.

        Calling this multiple times before calling `connect_to_backend()` will
        not have any effect beyond the first disconnection.
        '''

        if self._connection is not None:
            self._connection.close()


    def search(self, q: Query):
        '''
        '''


    def execute(self, m: Mutation):
        '''
        '''
