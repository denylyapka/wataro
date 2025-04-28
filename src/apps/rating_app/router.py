from typing import Annotated

from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.orm import Session

from . import crud
from src.db_app.main import get_db
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="src/templates")
router = APIRouter(prefix="/rating", tags=["Рейтинг"])


@router.get("/{tg_id}")
async def rating_open(tg_id: int, r: Request, db: Session = Depends(get_db)):
    rating_data, your_place = crud.Rating.get_rating_data(tg_id=tg_id, db=db)
    username = crud.UserData.get_username(tg_id=tg_id, db=db)
    print("rating_data:", rating_data)
    print("your_place:", your_place)

    return templates.TemplateResponse("rating.html", {
        "request": r, "tg_id": tg_id, "rating_data": rating_data, "username": username, "your_place": your_place,
        "ref_link": f"https://t.me/WA_TaroBot?start={tg_id}"
    })


@router.get("/referal_reg/{tg_id_master}/{tg_id_friend}/{code}")
async def referal_reg(tg_id_master: int, tg_id_friend: int, code: str, db: Session = Depends(get_db)):
    return crud.Rating.referal_reg(tg_id_master=tg_id_master, tg_id_friend=tg_id_friend, code=code, db=db)
