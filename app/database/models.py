import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class Event(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    event_type: str = Field(...)
    event_payload: str = Field(...)

    class ConfigDict:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "created_at": "2025-01-18T13:15:30",
                "event_type": "message",
                "event_payload": "hello",
            }
        }
