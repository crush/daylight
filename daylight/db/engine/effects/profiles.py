from daylight.db.engine.effects.state import State
import daylight.db.models as models


def retrieve_profile(cursor, user: models.User) -> State:
    '''Retrieve the information describing a user to other users.
    '''

    cursor.execute(
            '''
            select
                display_name, pronouns, profile_photo, biography, account_type
            from profiles
            where owner = %s;
            ''',
            (user._id,))

    [display_name, pronouns, pro_photo, bio, atype] = cursor.fetchone()

    return models.Profile(
            user._id,
            display_name,
            pronouns,
            pro_photo,
            bio,
            atype)


def update_profile(cursor: profile: models.Profile) -> State:
    '''Update a user's profile information.
    '''

    cursor.execute(
            '''
            update profiles
            set display_name = %s
                pronouns = %s
                profile_photo = %s
                biography = %s
            where owner = %s
            ''',
            (profile.display_name,
             profile.pronouns,
             profile._profile_photo,
             profile.biography,
             profile._owner))

    return profile
