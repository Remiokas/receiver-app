from typing import List

from pydantic import BaseModel, RootModel


class EventTemplate(BaseModel):
    event_type: str
    event_payload: str


class EventInput(RootModel):
    root: List[EventTemplate]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
