from fastapi import FastAPI, Path, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
templates = Jinja2Templates(directory="templates")
app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def get_users(user_id: int, request: Request) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.post("/user/{username}/{age}")
async def post_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='Sergey'),
                    age: int = Path(ge=18, le=120, description='Enter age', example='41')):
    user_id = max(users, key=lambda m: int(m.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str = Path(min_length=5, max_length=20, description='Enter username', example='Sergey'),
                    age: int = Path(ge=18, le=120, description='Enter age', example='45')):
    try:
        edit_user = users[user_id - 1]
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