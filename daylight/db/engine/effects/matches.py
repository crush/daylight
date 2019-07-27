from datetime import datetime

from daylight.db.engine.effects.state import State
import daylight.db.models as models


def establish_match(cursor, fr: models.User, to: model.User) -> State:
    '''Create a match between two users.
    '''

    now = datetime.now()

    cursor.execute(
            '''
            insert into matches (first_user, second_user, match_date)
            values (%s, %s, %s);
            ''',
            fr._id,
            to._id,
            now)

    return models.Match(fr._id, to._id, now)


def unmatch(cursor, match: models.Match) -> State:
    '''Delete a match.
    '''

    cursor.execute(
            '''
            delete from matches
            where first_user = %s
              and second_user = %s;
            ''',
            match._first_user,
            match._second_usere)

    return models.Match(-1, -1, datetime.now())
