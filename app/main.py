from fastapi import FastAPI
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}
