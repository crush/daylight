from typing import List

from daylight.db.engine.effects.state import State
import daylight.db.models as models


def retrieve_tags(cursor, user: models.User) -> State:
    '''Retrieve a list of tags associated with a user's profile.
    '''

    cursor.execute(
            '''
            select tag
            from profile_tag_relation
            where profile = %s;
            ''',
            user._id)

    return [models.Tag(row[0]) for row in cursor.fetchall()]


def set_tags(cursor, user: models.User, tags: List[models.Tag]) -> State:
    '''Set the tags associated with a user's profile.
    '''

    cursor.execute(
            '''
            delete from profile_tag_relation
            where profile = %s;
            ''',
            user._id)

    for tag in tags:
        cursor.execute(
                '''
                insert into profile_tag_relation (profile, tag)
                values (%s, %s);
                ''',
                user._id,
                tag)

    return tags
