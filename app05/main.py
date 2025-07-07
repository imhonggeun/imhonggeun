from fastapi import FastAPI
from controller import home

app = FastAPI()

app.get("/")
app.include_router(home.controller)