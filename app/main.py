from fastapi import FastAPI
from app.routers import memes, media

app = FastAPI()

app.include_router(memes.router, prefix="/memes", tags=["memes"])
app.include_router(media.router, prefix="/media", tags=["media"])

@app.get("/")
def read_root():
    return {"Hello": "World"}
