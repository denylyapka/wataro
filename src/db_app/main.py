from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.db_app import models
from src.db_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

