from pymongo import MongoClient
from pymongo.synchronous.database import Database

from app.config import CONFIG


async def init_db() -> Database:
    client = MongoClient(
        f"mongodb://{CONFIG.MONGO_DB_HOST}:{CONFIG.MONGO_DB_PORT}",
        uuidRepresentation="standard",
    )
    return client[CONFIG.MONGO_DB_NAME]


async def close_db():
    MongoClient(
        f"mongodb://{CONFIG.MONGO_DB_HOST}:{CONFIG.MONGO_DB_PORT}",
        uuidRepresentation="standard",
    ).close()
