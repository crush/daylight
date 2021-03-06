import os
from typing import Any, Dict, Optional


_CONFIG_PARAMS = [
    'POSTGRES_HOST',
    'POSTGRES_USER',
    'POSTGRES_PASSWORD',
    'POSTGRES_DB'
]

def load(defaults: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    '''Prepare a configuration by replacing a set of defaults with values pulled
    from environment variables.

    POSTGRES_HOST - host:port of the postgres database e.g. 127.0.0.1:5432
    POSTGRES_USER - user to connect to database as e.g. postgres
    POSTGRES_PASSWORD - password with which to authenticate to the database
    POSTGRES_DB - name of the database to connect to
    '''

    env = os.environ
    config = defaults.copy() if defaults is not None else {}

    for param in _CONFIG_PARAMS:
        try:
            config[param] = env[param]
        except KeyError:
            continue

    return config


def postgres_url(config: Dict[str, Any]) -> str:
    '''Format a connection string used to connect to a Postgres database
    given an application configuration.
    '''

    (u, p, h, d) = (
        config['POSTGRES_USER'],
        config['POSTGRES_PASSWORD'],
        config['POSTGRES_HOST'],
        config['POSTGRES_DB']
    )

    return f'postgres://{u}:{p}@{h}/{d}'
