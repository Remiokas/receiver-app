from pymongo import MongoClient
from pymongo.synchronous.database import Database

from app.config import CONFIG


async def init_db() -> Database:
    client = MongoClient(
        CONFIG.MONGO_URL,
        uuidRepresentation="standard",
    )
    return client[CONFIG.MONGO_DB_NAME]


async def close_db():
    MongoClient(
        CONFIG.MONGO_URL,
        uuidRepresentation="standard",
    ).close()
