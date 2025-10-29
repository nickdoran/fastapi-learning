from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1 : {
        "name":"Josh",
        "website": "www.apple.com",
        "age": 28,
        "role": "developer"
    }
}

#Base pydantic mod


@app.get("/")
def root():
    return {"Message": "Hello World"}

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., description="The ID you want to get", gt=0, lt=100)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not Found!")
    return users[user_id];
    