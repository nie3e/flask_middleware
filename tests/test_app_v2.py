from app.app_v2 import app


def test_app_returns_msg():
    test_app = app.test_client()
    res = test_app.get("/v2/hello")
    assert res.get_json(force=True) == {"msg": "Hello from app v2"}
