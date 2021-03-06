import io
import random
import string
from unittest import TestCase

import daylight.config as config
import daylight.config.test as test_cfg 
from daylight.db.engine import DaylightDB, DBError, DBErrorKind
import daylight.db.engine.query as query
import daylight.db.models as models


def _random_email() -> str:
    allowed = string.ascii_letters + string.digits + '_-.'
    name = ''.join([random.choice(allowed) for _ in range(32)])

    return f'{name}@tester.com'


class TestEffects(TestCase):
    '''Integration tests for database effect combinations.
    '''

    def setUp(self):
        self.cfg = config.load(test_cfg.DEFAULTS)
        self.db = DaylightDB(config.postgres_url(self.cfg))

        self.db.connect_to_backend()


    def tearDown(self):
        self.db.disconnect()


    def test_user_lifecycle(self):
        new_user = self.db.execute(query.register_user(
            _random_email(),
            'P455w()rD!',
            models.AccountType.WOMAN_FEMME))

        profile = self.db.search(query.retrieve_profile(new_user))

        profile.biography = 'An awesome new user!'

        self.db.execute(query.update_profile(profile))

        updated_profile = self.db.search(query.retrieve_profile(new_user))

        assert updated_profile.biography == profile.biography

        self.db.execute(query.set_tags(new_user, [
            models.Tag('bondage'),
            models.Tag('cosplay')
        ]))

        tags = self.db.search(query.retrieve_tags(new_user))
        tag_names = sorted([t.tag for t in tags])

        assert tag_names == ['bondage', 'cosplay']

    
    def test_match_lifecycle(self):
        user1 = self.db.execute(query.register_user(
            _random_email(),
            'Password1',
            models.AccountType.WOMAN_FEMME))

        user2 = self.db.execute(query.register_user(
            _random_email(),
            'Password2',
            models.AccountType.MAN_MASC))
        
        match = self.db.execute(query.establish_match(user1, user2))
        
        matches = self.db.search(query.retrieve_matches(user1))

        assert len(matches) == 1

        self.db.execute(query.unmatch(match))

        matches = self.db.search(query.retrieve_matches(user1))

        assert len(matches) == 0


    def test_like_lifecycle(self):
        user1 = self.db.execute(query.register_user(
            _random_email(),
            'Password1',
            models.AccountType.WOMAN_FEMME))

        user2 = self.db.execute(query.register_user(
            _random_email(),
            'Password2',
            models.AccountType.MAN_MASC))
        
        like = self.db.execute(query.send_like(user1, user2))
        
        likes = self.db.search(query.retrieve_likes(user1))

        assert len(likes) == 1

        self.db.execute(query.revoke_like(like))

        found_likes = self.db.search(query.retrieve_likes(user1))

        assert len(found_likes) == 0


    def test_photo_lifecycle(self):
        user = self.db.execute(query.register_user(
            _random_email(),
            'password',
            models.AccountType.WOMAN_FEMME))

        photo_stream = io.BytesIO(b'test')
        photo = self.db.execute(query.upload_photo(user, photo_stream))

        found_photos = self.db.search(query.retrieve_photos(user))

        assert len(found_photos) == 1

        self.db.execute(query.delete_photo(photo))

        found_photos = self.db.search(query.retrieve_photos(user))

        assert len(found_photos) == 0
