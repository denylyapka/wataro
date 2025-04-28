from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.apps.start_app.router import router as start_router
from src.apps.main_menu_app.router import router as choice_router
from src.apps.forecast_app.router import router as start_card_deal_router
from src.apps.user_app.router import router as profile_router
from src.apps.rating_app.router import router as rating_router


app = FastAPI(docs_url="/admin-docs-app-986516564-mk@cs!n!i$89eb%$%%v9odwe")
templates = Jinja2Templates(directory="src/templates")


app.include_router(start_router)
app.include_router(choice_router)
app.include_router(start_card_deal_router)
app.include_router(profile_router)
app.include_router(rating_router)
