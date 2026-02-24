import uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message": "GuitarHub API working"}

if __name__ == "__main__":
    uvicorn.run('CRUD:app', host="127.0.0.1", port=8000, reload=True)