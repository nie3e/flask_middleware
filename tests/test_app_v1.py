from app_v1 import app
from flask.testing import FlaskClient


def test_app_returns_msg():
    test_app = app.test_client()
    res = test_app.get("/v1/hello")
    assert res.get_json(force=True) == {"msg": "Hello from app v1"}
