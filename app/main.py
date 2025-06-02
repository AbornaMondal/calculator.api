# app/main.py

from fastapi import FastAPI, HTTPException
from app import calculator

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Calculator API!"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": calculator.add(a, b)}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": calculator.subtract(a, b)}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": calculator.multiply(a, b)}

@app.get("/divide")
def divide(a: float, b: float):
    try:
        result = calculator.divide(a, b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
