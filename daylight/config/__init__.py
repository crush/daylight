from dataclasses import dataclass
import os
from typing import Any, Dict, Optional


_CONFIG_PARAMS = [
    'POSTGRES_HOST',
    'POSTGRES_USER',
    'POSTGRES_PASSWORD',
    'POSTGRES_DATABASE'
]

def load(defaults: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    '''Prepare a configuration by replacing a set of defaults with values pulled
    from environment variables.

    POSTGRES_HOST - host:port of the postgres database e.g. 127.0.0.1:5432
    POSTGRES_USER - user to connect to database as e.g. postgres
    POSTGRES_PASSWORD - password with which to authenticate to the database
    POSTGRES_DATABASE - name of the database to connect to
    '''

    env = os.environ
    config = defaults.copy() if defaults is not None else {}

    for param in _CONFIG_PARAMS:
        config[param] = env[param]

    return config

