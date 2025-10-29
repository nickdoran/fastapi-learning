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
class User(BaseModel):
    name: str
    website: str
    age: int
    role: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    website: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None



@app.get("/")
def root():
    return {"Message": "Hello World"}

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., description="The ID you want to get", gt=0, lt=100)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not Found!")
    return users[user_id];
    
@app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id: int, user:User):
    if user_id in users:
        raise HTTPException(status_code=404, detail="User already exists!")
    users[user_id] = user.model_dump()
    return user


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User is not here")
    
    current_user = users[user_id]

    if user.name is not None:
        current_user["name"] = user.name
    if user.website is not None:
        current_user["website"] = user.website
    if user.age is not None:
        current_user["age"] = user.age
    
    