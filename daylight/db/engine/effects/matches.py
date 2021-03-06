from datetime import datetime

from daylight.db.engine.effects.state import State
import daylight.db.models as models


def establish_match(cursor, fr: models.User, to: models.User) -> State:
    '''Create a match between two users.
    '''

    now = datetime.now()

    cursor.execute(
            '''
            insert into matches (first_user, second_user, match_date)
            values (%s, %s, %s);
            ''',
            (fr._id, to._id, now))

    return models.Match(fr._id, to._id, now)


def retrieve_matches(cursor, user: models.User) -> State:
    '''Retrieve a list of a user's matches.
    '''

    cursor.execute(
            '''
            select second_user, match_date
            from matches
            where first_user = %s;
            ''',
            (user._id,))

    return [models.Match(user._id, *row) for row in cursor.fetchall()]


def unmatch(cursor, match: models.Match) -> State:
    '''Delete a match.
    '''

    cursor.execute(
            '''
            delete from matches
            where first_user = %s
              and second_user = %s;
            ''',
            (match._first_user, match._second_user))

    return models.Match(-1, -1, datetime.now())
