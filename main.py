from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import auth
from database import engine, Base
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create static directory if it doesn't exist
os.makedirs("static", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

app.include_router(auth.router)

@app.get("/", response_class=HTMLResponse)
async def web(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})