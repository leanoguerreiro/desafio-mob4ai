from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, Float, create_engine
from pydantic import BaseModel




app = FastAPI()

from routes import process_router

app.include_router(process_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
