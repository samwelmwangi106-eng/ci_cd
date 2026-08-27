"""
Tests for app.py.

These are exactly what the CI workflow runs on every push/PR.
Try breaking one on purpose (e.g. change assertEqual value) and push —
that's the best way for students to *see* CI catch a bug.
"""
from app import app


def client():
    app.testing = True
    return app.test_client()


def test_health():
    resp = client().get("/api/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_greet():
    resp = client().get("/api/greet/Joseph")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello, Joseph!"


def test_greet_empty_name():
    resp = client().get("/api/greet/%20")
    assert resp.status_code == 400


def test_add_success():
    resp = client().post("/api/add", json={"a": 2, "b": 3})
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5


def test_add_missing_field():
    resp = client().post("/api/add", json={"a": 2})
    assert resp.status_code == 400


def test_add_non_numeric():
    resp = client().post("/api/add", json={"a": "x", "b": 2})
    assert resp.status_code == 400
