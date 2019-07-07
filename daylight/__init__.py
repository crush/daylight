import os

from flask import Flask
import psycopg2 as postgres

import daylight.config as config
import daylight.config.dev as dev
import daylight.db.tables as db_tables


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


conn = postgres.connect(config.postgres_url(cfg))
with conn.cursor() as cursor:
    db_tables.create_tables(cursor)
conn.close()
print('Created database tables')

import daylight.routes
