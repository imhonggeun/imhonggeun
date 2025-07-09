from fastapi import FastAPI,Form
from typing import Annotated
import mariadb,os
import httpx
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"data": "안녕하세요"}

@app.get("/test")
def test(a : int):
    return {"A변수" : a}

@app.post("/test")
def tset(name : Annotated[str,Form()]):
    return {"이름" : name}

@app.get("/db")
def db():
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT')),    
    }
    
    conn = mariadb.connect(**conn_params)
    cur = conn.cursor()
    
    sql = "select * from movies"
    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()
    return {"result" : result}

@app.get("/year")
def year( y : str):
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT')),    
    }
    
    conn = mariadb.connect(**conn_params)
    cur = conn.cursor()
    sql = f"SELECT * FROM movies WHERE YEAR < '{y}';"

    cur.execute(sql)
    result = cur.fetchall()
    
    cur.close()
    conn.close()
    return {"result" : result}

@app.get("/movie")
async def movie(mn : str):
    async with httpx.AsyncClient() as client:
        key = os.getenv('API_KEY')
        url = f"https://www.omdbapi.com/?apikey={key}&s={mn}"
        response = await client.get(url)
        return response.json()
    
@app.get("/movie/item")
async def movie(id : str):
    async with httpx.AsyncClient() as client:
        key = os.getenv('API_KEY')
        url = f"https://www.omdbapi.com/?apikey={key}&i={id}&plot=full"
        response = await client.get(url)
        return response.json()
    
# def main():
#     print("Hello from app08!")


# if __name__ == "__main__":
#     main()
