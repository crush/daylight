import os
from flask import Flask

import config
import config.dev


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


cfg = config.load(config.dev.DEFAULTS)

print('Loaded configuration', cfg)

import daylight.routes
