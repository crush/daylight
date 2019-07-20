import unittest

import daylight


class DaylightTestCase(unittest.TestCase):

    def setUp(self):
        self.app = daylight.app.test_client()

    def test_index(self):
        rv = self.app.get('/')


if __name__ == '__main__':
    unittest.main()
