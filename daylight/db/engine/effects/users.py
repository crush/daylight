from datetime import datetime

from daylight.db.engine.effects.state import State
import daylight.db.models as models


def create_user(
        cursor: postgres.cursor,
        email: str,
        password_hash: str
        ) -> State:
    '''A mutating effect that attempts to register a new user.
    '''

    now = datetime.now()

    cursor.execute(
            '''
            insert into users
            values (%s, %s, %s)
            returning (id);
            ''',
            email,
            password_hash,
            now)

    user_id = cursor.fetchone()[0]

    return models.User(user_id, email, password_hash, now)


def delete_user(cursor: postgres.cursor) -> State:
    return []


def reset_password(cursor: postgres.cursor) -> State:
    return []


def retrieve_user(cursor: postgres.cursor) -> State:
    return []
