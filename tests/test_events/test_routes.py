from fastapi.testclient import TestClient
from mock.mock import AsyncMock

from app.main import app

client = TestClient(app)


def test_create_event(mocker):
    event_input = [{"event_type": "message", "event_payload": "greetings"}]

    accept_events_mock = AsyncMock()
    mocker.patch("app.events.routes.accept_events", accept_events_mock)
    accept_events_mock.return_value = ["123"]

    response = client.post("/event", json=event_input)
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {"created_events": ["123"]},
    }
