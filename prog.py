from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, REST API!"}

# GET API
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"Hello {name}"}

# POST API
@app.post("/add")
def add_numbers(a: int, b: int):
    return {"sum": a + b}