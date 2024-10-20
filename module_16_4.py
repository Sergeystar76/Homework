from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='Sergey'),
                    age: int = Path(ge=18, le=120, description='Enter age', example='45')):
    user_id = len(users)
    if user_id == 0:
        user = User(id=1, username=username, age=age)
    else:
        user = User(id=(user_id + 1), username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str = Path(min_length=5, max_length=20, description='Enter username', example='Sergey'),
                    age: int = Path(ge=18, le=120, description='Enter age', example='45')):
    try:
        edit_user = users[user_id-1]
        edit_user.username = username
        edit_user.age = age
        user = User(id=user_id, username=username, age=age)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    try:
        users.pop(user_id - 1)
        return users
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")