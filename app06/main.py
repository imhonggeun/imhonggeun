from fastapi import FastAPI ,Form
from controller import root

app = FastAPI()
app.include_router(root.controller)