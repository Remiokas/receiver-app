import datetime
from uuid import UUID

import pytest
from mock import AsyncMock
from mock.mock import MagicMock, Mock

from app.database.models import Event
from app.events.mapping import EventInput, EventTemplate
from app.events.methods import accept_events, process_event


@pytest.mark.asyncio
async def test_accept_events(mocker):
    event = Event(event_type="message", event_payload="greetings")
    process_event_mock = AsyncMock()
    mocker.patch("app.events.methods.process_event", process_event_mock)
    process_event_mock.return_value = event

    inserted_object_mock = MagicMock()
    inserted_object_mock.inserted_id = "123"

    save_object_to_db_mock = AsyncMock()
    mocker.patch("app.events.methods.save_object_to_db", save_object_to_db_mock)
    save_object_to_db_mock.return_value = inserted_object_mock

    event_input = EventInput(
        root=[
            {"event_type": "message", "event_payload": "greetings"},
        ]
    )

    actual_value = await accept_events(event_input)
    expected_value = ["123"]

    process_event_mock.assert_called_once_with(event_input[0])
    save_object_to_db_mock.assert_called_once_with(event)

    assert actual_value == expected_value


@pytest.mark.asyncio
async def test_process_event(mocker):
    event_input = EventTemplate(event_type="message", event_payload="greetings")

    event = Event(
        id=UUID("f94b9ae6-8db4-4630-ad07-14a376df28a8"),
        created_at=datetime.datetime(2025, 1, 19, 15, 59, 42, 330120),
        event_type="message",
        event_payload="greetings",
    )

    event_mock = Mock()
    mocker.patch("app.events.methods.Event", event_mock)
    event_mock.return_value = event

    actual_value = await process_event(event_input)
    expected_value = event

    assert actual_value == expected_value
