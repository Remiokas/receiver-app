from typing import List

from app.events.mapping import EventTemplate, EventInput
from app.database.actions import save_object_to_db
from app.database.models import Event


async def accept_events(events: EventInput) -> List[str]:
    created_event_ids = []
    for event in events:
        event_object = await process_event(event)
        created_event = await save_object_to_db(event_object)
        created_event_ids.append(str(created_event.inserted_id))
    return created_event_ids


async def process_event(event_input: EventTemplate) -> Event:
    return Event(**event_input.model_dump())
