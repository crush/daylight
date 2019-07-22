import os

from flask import Flask

import daylight.config as config
import daylight.config.dev as dev
from daylight.db.engine import DaylightDB, DBError, DBErrorKind
import daylight.db.engine.query as query
import daylight.db.models as models


app = Flask(__name__)
app.config.from_object("daylight.default_settings")
app.config.from_envvar("DAYLIGHT_SETTINGS")

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler

    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(
        os.path.join(app.config["LOG_DIR"], "daylight.log"), "midnight"
    )
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(
        logging.Formatter("<%(asctime)s> <%(levelname)s> %(message)s")
    )
    app.logger.addHandler(file_handler)


cfg = config.load(dev.DEFAULTS)
print('Loaded configuration', cfg)


db = DaylightDB(config.postgres_url(cfg))
db.connect_to_backend()
print('Created database tables')


mutation = query.register_user(
        'test@site.com',
        'passw0rd',
        models.WomanFemmeAccountType)
user = db.execute(mutation)
print(f'New user = {user}')
db.disconnect()


import daylight.routes
