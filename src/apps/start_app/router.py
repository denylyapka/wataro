import asyncio
from typing import Annotated

import aiohttp

from fastapi import APIRouter, Request, Form, Depends
from sqlalchemy.orm import Session

from . import crud
from src.db_app.main import get_db
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="src/templates")
router = APIRouter(prefix="/start", tags=["Главное меню"])


@router.get("", include_in_schema=False)
async def start(request: Request):
    print("start")
    return templates.TemplateResponse("start.html", {
        "request": request
    })


@router.post("/get_name", include_in_schema=False)
async def get_name(
        tg_id: Annotated[int, Form()] = None,
        first_name: Annotated[str, Form()] = None,
        username: Annotated[str, Form()] = None,
        db: Session = Depends(get_db)
):
    crud.CreateUser.auto_create_user(data={"tg_id": tg_id, "username": username, "fullname": first_name}, db=db)


async def send_user_id_to_bot_server(tg_id: int):
    async with aiohttp.ClientSession() as session:
        try:
            url = "http://195.54.178.243:26352/sub_check"
            params = {"tg_id": tg_id}
            async with session.get(url, json=params) as response:
                result = await response.json()
                return result
        except Exception as e:
            print(f"Error sending request to bot server: {e}")


@router.get("/get_status_check/{tg_id}")
async def get_status_check(tg_id: int, db: Session = Depends(get_db)):
    response = await send_user_id_to_bot_server(tg_id=tg_id)
    return {"code": 201, "status": "OK" if response['status'] != "left" else "NOT OK"}


@router.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("test_3.html", {
        "request": request
    })
