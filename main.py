from fastapi import FastAPI
import uvicorn
from database.database import Base,engine
from models.task import TaskModel
from routes.task import router as task_router
from routes.auth import router as auth_router, default_router
# Code bellow are commented because deletes the database
# data all the time. Just for development

app = FastAPI()


app.include_router(task_router, prefix='')
app.include_router(auth_router, prefix='')
app.include_router(default_router, prefix='')

