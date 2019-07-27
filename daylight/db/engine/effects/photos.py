from datetime import datetime
import io

from dayfrom daylight.db.engine.effects.state import State
import daylight.db.models as models


def delete_photo(cursor, photo: models.Photo) -> State:
    '''Delete a photo.
    '''

    # TODO: Remove from image store.
    
    cursor.execute(
            '''
            delete from photos
            where id = %s;
            ''',
            phoo._id)

    return models.Photo(-1, '', -1, datetime.now())


def set_profile_pic(cursor, user: models.User, photo: modesl.Photo) -> State:
    '''Set a user's profile photo to a picture they've uploaded.
    '''

    cursor.execute(
            '''
            update profiles
            set profile_photo = %s
            where owner = %s;
            ''',
            photo._id,
            user._id)

    return photo


def upload_photo(cursor, user: models.User, byte_stream: io.BytesIO) -> State:
    '''Upload a photo to storage and associate a user's profile with it.
    '''

    # TODO: Save to image store.

    image_src = ''

    now = datetime.now()

    cursor.execute(
            '''
            insert into photos (image_source, owner, upload_date)
            values (%s, %s, %s)
            returning id;
            ''',
            image_src,
            user._id,
            now)

    photo_id = cursor.fetch_one()[0]

    return models.Photo(photo_id, image_src, user._id, now)
