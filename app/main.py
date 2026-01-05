from fastapi import FastAPI
from .database import engine, Base
from .routes import notes, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Note Taking API")

app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/")
def root():
    return {"message": "API running"}
