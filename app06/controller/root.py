from fastapi import FastAPI ,Form,APIRouter
from typing import Annotated

controller=APIRouter()

@controller.get("/")
def root():
    return {"test": 1}

@controller.get("/test")
def test(a):
    return {"여기야": a}

@controller.post("/body")
def body( a: Annotated[str, Form()]):
    return {"data" : a}