from datetime import datetime

from daylight.db.engine.effects.state import State
import daylight.db.models as models


def create_user(
        cursor,
        email: str,
        password_hash: str
        ) -> State:
    '''A mutating effect that attempts to register a new user.
    '''

    now = datetime.now()

    cursor.execute(
            '''
            insert into users (email, password_hash, join_date)
            values (%s, %s, %s)
            returning (id);
            ''',
            (email, password_hash, now))

    user_id = cursor.fetchone()[0]

    return models.User(user_id, email, password_hash, now)


def delete_user(cursor, user: models.User) -> State:
    '''A mutating effect that attempts to delete an existing user.
    Returns a `User` with effectively nulled values.
    '''

    cursor.execute(
            '''
            delete from users
            where id = %s
            ''',
            (user._id,))

    return models.User(-1, '', '', datetime.now())


def reset_password(cursor, new_user: models.User) -> State:
    '''A mutating effect that updates a user's password hash with a new value.
    '''

    cursor.execute(
            '''
            update users
            set password_hash = %s
            where id = %s
            ''',
            (new_user.password_hash, new_user._id))

    return new_user


def retrieve_user(cursor, user_id: int) -> State:
    '''A query effect that retrieves information about a user given an ID.
    '''

    cursor.execute(
            '''
            select email, password_hash, join_date
            from users
            where id = %s
            ''',
            (user_id,))

    (email, password_hash, join_date) = cursor.fetchone()

    return models.User(user_id, email, password_hash, join_date)
