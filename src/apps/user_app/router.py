from typing import Annotated

from fastapi import APIRouter, Request, Depends, Form
from sqlalchemy.orm import Session

from . import crud
from src.db_app.main import get_db
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="src/templates")
router = APIRouter(prefix="/profile", tags=["Профиль"])


@router.get("/{tg_id}", include_in_schema=False)
async def main_menu(tg_id: int, request: Request, db: Session = Depends(get_db)):
    username = crud.CreateUser.get_username(tg_id=tg_id, db=db)
    name = crud.CreateUser.get_name(tg_id=tg_id, db=db)
    choice_paul = crud.CreateUser.get_paul(tg_id=tg_id, db=db)
    choice_device = crud.CreateUser.get_device(tg_id=tg_id, db=db)
    # username = "username"
    # name = "name"
    # choice_paul = "Мужикмен"
    # choice_device = "IOS"
    print("choice_paul:", choice_paul)
    print("choice_device:", choice_device)
    return templates.TemplateResponse("profile.html", {"request": request, "tg_id": tg_id, "choice_paul": choice_paul,
                                                       "choice_device": choice_device, "username": username, "name": name})


@router.post("/create_data", include_in_schema=False)
async def profile_create_data(
        tg_id: Annotated[int, Form()] = None,
        paul: Annotated[str, Form()] = None,
        device: Annotated[str, Form()] = None,
        db: Session = Depends(get_db)
):
    crud.CreateUser.recreate_user(tg_id=tg_id, paul=paul, device=device, db=db)