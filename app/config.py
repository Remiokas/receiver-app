from typing import NamedTuple
from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config(NamedTuple):
    SEND_INTERVAL: int = getenv("SEND_INTERVAL", 60)
    EVENT_CONSUMER_URL: str = getenv("EVENT_CONSUMER_URL", "localhost")
    EVENT_CONSUMER_PORT: int = getenv("EVENT_CONSUMER_PORT", 5000)
    EVENT_JSON_PATH: str = getenv("EVENT_JSON_PATH", "/event_json")
    MONGO_DB_HOST: str = getenv("MONGO_DB_HOST", "localhost")
    MONGO_DB_PORT: int = getenv("MONGO_DB_PORT", 27017)
    MONGO_DB_NAME: str = getenv("MONGO_DB_NAME", "EVENTS")
    LOG_LEVEL: str = getenv("LOG_LEVEL", "INFO")


CONFIG = Config()
