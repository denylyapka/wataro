from fastapi import APIRouter, Request

from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="src/templates")
router = APIRouter(prefix="/main_menu", tags=["Главное меню"])


@router.get("/{tg_id}", include_in_schema=False)
async def main_menu(tg_id: int, request: Request):
    return templates.TemplateResponse("main_menu.html", {"request": request, "tg_id": tg_id})
