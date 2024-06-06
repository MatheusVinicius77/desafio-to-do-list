from pydantic import BaseModel
from models.task import TaskState 
from datetime import datetime
from typing import Optional



# default schema 
class TaskSchema(BaseModel):
    id : int
    title : str
    description : str 
    state : TaskState
    data_creation: datetime
    data_atualization: datetime

# schema to update
class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    state: Optional[TaskState] = None


class TaskCreateSchema(BaseModel):
    title: str
    description: str
    state: TaskState