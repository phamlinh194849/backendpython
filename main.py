from fastapi import FastAPI
from routers import auth
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
