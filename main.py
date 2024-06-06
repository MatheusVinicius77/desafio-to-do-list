from fastapi import FastAPI
import uvicorn
from database.database import Base,engine
from models.task import TaskModel
from routes.task import router

# Code bellow are commented because deletes the database
# data all the time. Just for development

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(router, prefix='')

if __name__ == '__main__':
    uvicorn.run("main:app", port=3000, reload=True)
