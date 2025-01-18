from fastapi import FastAPI
from app.events.routes import router as event_router

app = FastAPI()
app.include_router(event_router)


@app.get("/")
async def healthcheck():
    return {"message": "Hello World"}
