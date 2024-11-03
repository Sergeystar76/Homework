from fastapi import FastAPI
from app.routers import task, user
from .routers.task import router
from .routers.user import router
from xml.etree.ElementInclude import include



app = FastAPI()

@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)