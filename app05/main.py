from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    print("web Start!!")
    return {"name" : "AI"}