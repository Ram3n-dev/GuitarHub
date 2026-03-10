from http.client import HTTPException

import uvicorn
from fastapi import FastAPI, status, Body, Depends
from pydantic import BaseModel, EmailStr


app = FastAPI()

dbimitation = []
class User(BaseModel):
    id: int | None = None
    username: str
    email: EmailStr
    password: str
@app.get("/")
def root():
    return {"message": "GuitarHub API working"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return dbimitation[user_id]

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    dbimitation.pop(user_id)
@app.post("/users")
async def create_user(user: User):
    if user.id is None:
        user.id = len(dbimitation) + 1
    dbimitation.append(user)
    return {"id": user.id, "username": user.username, "email": user.email, "password": user.password }
@app.get("/ping")
def ping():
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
