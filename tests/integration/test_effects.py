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


    def test_profile_creation(self):
        new_user = self.db.execute(query.register_user(
            _random_email(),
            'P455w()rD!',
            models.AccountType.WOMAN_FEMME))

        profile = self.db.search(query.retrieve_profile(new_user))

        profile.biography = 'An awesome new user!'

        self.db.execute(query.update_profile(profile))

        updated_profile = self.db.search(query.retrieve_profile(new_user))

        assert updated_profile.biography == profile.biography
