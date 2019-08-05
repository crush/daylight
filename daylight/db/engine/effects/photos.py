from datetime import datetime
import io
import random

from daylight.db.engine.effects.state import State
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
            (photo._id,))

    return models.Photo(-1, '', -1, datetime.now())


def retrieve_photos(cursor, user: models.User) -> State:
    '''Retrieve the list of photos uploaded to a user's account.
    '''

    cursor.execute(
            '''
            select id, image_source, upload_date
            from photos
            where owner = %s;
            ''',
            (user._id,))

    return [
        models.Photo(row[0], row[1], user._id, row[2])
        for row in cursor.fetchall()
    ]


def set_profile_pic(cursor, user: models.User, photo: models.Photo) -> State:
    '''Set a user's profile photo to a picture they've uploaded.
    '''

    cursor.execute(
            '''
            update profiles
            set profile_photo = %s
            where owner = %s;
            ''',
            (photo._id, user._id))

    return photo


def upload_photo(cursor, user: models.User, byte_stream: io.BytesIO) -> State:
    '''Upload a photo to storage and associate a user's profile with it.
    '''

    # TODO: Save to image store.

    allowed = 'ABCDEF0123456789'
    image_src = ''.join([random.choice(allowed) for _ in range(32)])

    now = datetime.now()

    cursor.execute(
            '''
            insert into photos (image_source, owner, upload_date)
            values (%s, %s, %s)
            returning id;
            ''',
            (image_src, user._id, now))

    photo_id = cursor.fetchone()[0]

    return models.Photo(photo_id, image_src, user._id, now)
