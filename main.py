from fastapi import FastAPI
import uvicorn
from database.database import Base,engine
# from models.task import Task


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run("main:app", port=3000, reload=True)
