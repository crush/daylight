'''Exports `DaylightDB` which provides the foundation for the execution of
queries against the database.
'''

import enum
from typing import Optional
from threading import Lock

import psycopg2 as postgres

import daylight.db.engine.effects as effects
from daylight.db.engine.effects.state import State
from daylight.db.engine.query import Mutation, MutationId, Query, QueryId
from daylight.db.engine.tables import create_tables


class DBErrorKind(enum.Enum):
    '''Enumerates all of the classes of errors that a `DaylightDB` may raise.
    '''

    CONNECTION_ERROR = 'CONNECTION ERROR' 
    UNSUPPORTED_QUERY = 'UNSUPPORTED QUERY'
    UNSUPPORTED_MUTATION = 'UNSUPPORTED MUTATION'
    EXECUTION_ERROR = 'EXECUTION ERROR'
    INTERNAL_ERROR = 'INTERNAL ERROR'
    PROGRAMMING_ERROR = 'PROGRAMMING ERROR'


class DBError(Exception):
    '''The only type of exception that `DaylightDB` may raise.  All variance
    is accounted for in the `DBErrorKind` enumeration.
    '''

    def __init__(self, kind: DBErrorKind, msg: str):
        self.kind: DBErrorKind = kind
        self.message: str = f'Database error: {kind}: {msg}'


class DaylightDB:
    '''The primary abstraction over a connection to a Postgres database.
    It consumes `Query` and `Mutation` instances to search for and manipulate
    data in Postgres.
    '''

    def __init__(self, postgres_url: str):
        self._conn_url: str = postgres_url
        self._connection: Optional[postgres.connection] = None
        self._lock: Lock = Lock()


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

            self._lock.acquire()
            with self._connection.cursor() as cursor:
                create_tables(cursor)
            self._lock.release()

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

        self._lock.acquire()
        if self._connection is not None:
            self._connection.close()
        self._lock.release()


    def search(self, q: Query) -> State:
        '''Execute a search query against the database.
        '''

        allowed_effects = {
            QueryId.RETRIEVE_USER_BY_ID: effects.retrieve_user,
            QueryId.RETRIEVE_PROFILE: effects.retrieve_profile,
            QueryId.RETRIEVE_TAGS: effects.retrieve_tags,
            QueryId.RETRIEVE_MATCHES: effects.retrieve_matches,
            QueryId.RETRIEVE_PHOTOS: effects.retrieve_photos,
            QueryId.RETRIEVE_ACCOUNT_TYPE: effects.retrieve_account_type
        }

        effect = allowed_effects.get(q.query_id)
        if effect is None:
            raise DBError(
                    DBErrorKind.UNSUPPORTED_QUERY,
                    f'unsupported query {q.query_id}')

        self._lock.acquire()
        with self._connection.cursor() as cursor:
            try:
                return effect(cursor, *q.parameters)

            except postgres.InterfaceError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'{err.message}')

            except postgres.DatabaseError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'{err.message}')

            except postgres.DataError as err:
                raise DBError(
                        DBErrorKind.EXECUTION_ERROR,
                        f'query execution failed: {err.message}')

            except postgres.OperationalError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'unexpected database error: {err.message}')

            except postgres.IntegrityError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'failed to maintain relation integrity: {err.message}')

            except postgres.InternalError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'unexpected database error {err.message}')

            except postgres.ProgrammingError as err:
                raise DBError(
                        DBErrorKind.PROGRAMMING_ERROR,
                        f'bad effect {effect.__name__}: {err.message}')

            except postgres.NotSupportedError as err:
                raise DBError(
                        DBErrorKind.PROGRAMMING_ERROR,
                        f'bad effect {effect.__name__}: {err.message}')
       
            finally:
                self._lock.release()


    def execute(self, m: Mutation) -> State:
        '''Execute a mutation query against the database.
        '''

        allowed_effects = {
            MutationId.REGISTER_USER: effects.create_user,
            MutationId.RESET_PASSWORD: effects.reset_password,
            MutationId.DELETE_USER: effects.delete_user,
            MutationId.SEND_LIKE: effects.send_like,
            MutationId.REVOKE_LIKE: effects.revoke_like,
            MutationId.ESTABLISH_MATCH: effects.establish_match,
            MutationId.UNMATCH: effects.unmatch,
            MutationId.DELETE_PHOTO: effects.delete_photo,
            MutationId.UPLOAD_PHOTO: effects.upload_photo,
            MutationId.UPDATE_PROFILE: effects.update_profile
        }

        effect = allowed_effects.get(m.mutation_id)
        if effect is None:
            raise DBError(
                    DBErrorKind.UNSUPPORTED_MUTATION,
                    f'unsupported mutation {m.mutation_id}')

        self._lock.acquire()
        with self._connection.cursor() as cursor:
            try:
                result = effect(cursor, *m.parameters)

                return result
            
            except postgres.InterfaceError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'{err.message}')

            except postgres.DatabaseError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'{err.message}')

            except postgres.DataError as err:
                raise DBError(
                        DBErrorKind.EXECUTION_ERROR,
                        f'query execution failed: {err.message}')

            except postgres.OperationalError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'unexpected database error: {err.message}')

            except postgres.IntegrityError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'failed to maintain relation integrity: {err.message}')

            except postgres.InternalError as err:
                raise DBError(
                        DBErrorKind.INTERNAL_ERROR,
                        f'unexpected database error {err.message}')

            except postgres.ProgrammingError as err:
                raise DBError(
                        DBErrorKind.PROGRAMMING_ERROR,
                        f'bad effect {effect.__name__}: {err.message}')

            except postgres.NotSupportedError as err:
                raise DBError(
                        DBErrorKind.PROGRAMMING_ERROR,
                        f'bad effect {effect.__name__}: {err.message}')
        
            finally:
                self._connection.commit()
                self._lock.release()
