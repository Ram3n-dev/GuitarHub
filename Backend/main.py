import uvicorn
from fastapi import FastAPI

from Backend.routers.user import router as user_router

app = FastAPI(title="GuitarHub API")

app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "GuitarHub API working"}


@app.get("/ping")
def ping():
    return {"ping": "pong"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)