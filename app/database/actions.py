from pymongo.results import InsertOneResult

from app.database.database import init_db, close_db
from app.database.models import BaseModel


async def save_object_to_db(object_to_save: BaseModel) -> InsertOneResult:
    database = await init_db()
    database_collection = database["events"]
    saved_event = database_collection.insert_one(object_to_save.dict())
    await close_db()
    return saved_event
