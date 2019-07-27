from datetime import datetime

from daylight.db.engine.effects.state import State
import daylight.db.models as models


def revoke_like(cursor, like: models.Like) -> State:
    '''Revoke a like formerly sent by one user to another user.
    '''

    cursor.execute(
            '''
            delete from likes_relation
            where from_user = %s
              and to_user = %s;
            ''',
            like._from_user,
            like._to_user)

    return models.Like(-1, -1, datetime.now())


def send_like(cursor, fr: models.User, to: models.User) -> State:
    '''Send a like from one user to another.
    '''

    now = datetime.now()

    cursor.execute(
            '''
            insert into likes_relation (from_user, to_user, send_date)
            values (%s, %s, %s);
            ''',
            fr._id,
            to._id,
            now)

    return models.Like(fr._id, to._id, now)
