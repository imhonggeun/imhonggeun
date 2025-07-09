from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"data": "안녕하세요"}

@app.get("/test")
def test(a : int):
    return{"A변수" : a}

#
# def main():
#     print("Hello from app08!")


# if __name__ == "__main__":
#     main()
