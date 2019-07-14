from dataclasses import dataclass
import json
from typing import Optional

from flask import request

from daylight import app


@dataclass
class _Request:

    username: str
    email: str
    password: str
    account_type: str


@dataclass
class _Response:
    error: Optional[str]
    data: None


@app.route('/users/register', methods=['POST'])
def register():
    req = _Request(**request.json)
    res = _Response('test error')

    return json.dumps(res)
