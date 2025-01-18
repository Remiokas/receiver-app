from app.events.methods import accept_events
from app.events.mapping import EventInput
from fastapi import APIRouter

router = APIRouter(prefix="/event", tags=["event"])


@router.post("")
async def create_event(event_input: EventInput):
    created_events = await accept_events(event_input)
    return {"message": "success", "data": {"created_events": created_events}}
