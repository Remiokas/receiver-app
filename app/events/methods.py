from app.events.mapping import EventTemplate, EventInput
from app.database.actions import save_object_to_db
from app.database.models import Event


async def accept_events(events: EventInput):
    created_events = []
    for event in events:
        event_object = await process_event(event)
        created_event_id = await save_object_to_db(event_object)

        created_events.append(str(created_event_id.inserted_id))
    return created_events


async def process_event(event_input: EventTemplate) -> Event:
    return Event(**event_input.dict())
