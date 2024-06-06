from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict

from schemas.task import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from services import task,utils
from database.db_dependency import get_db

router = APIRouter(prefix="/tasks")


# GET TASK BY ID

@router.get("/{task_id}", response_model=TaskSchema)
async def get_task(
    task_id: int,
    session: Session = Depends(get_db),
    current_user: dict = Depends(utils.get_current_user)

    
    ) -> TaskSchema:
    searched_task = task.get_task_by_id(session, task_id)
    if not searched_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return searched_task


# GET ALL TASKS
@router.get("/", response_model=list[TaskSchema])
async def get_all_tasks(
    session : Session = Depends(get_db),
    current_user: dict = Depends(utils.get_current_user)
    ) -> List[TaskSchema]:

    return task.get_all_tasks(session)


# ADD NEW TASK

@router.post("/create", response_model=TaskSchema)
async def create_task(
    new_task:TaskCreateSchema,
    session : Session = Depends(get_db),
    current_user: dict = Depends(utils.get_current_user)
    ) -> TaskSchema:
    return task.create_task(session, new_task)


# UPDATE TASK
@router.put("/update/{task_id}", response_model=TaskSchema)
async def update_task(
    task_id : int ,
    change_task:TaskUpdateSchema ,
    current_user: dict = Depends(utils.get_current_user),
    session : Session = Depends(get_db)) -> TaskSchema:
    return task.update_task(session, task_id, change_task)


# DELETING A TASK BY ID
@router.delete("/delete/{task_id}", response_model=Dict[str, str])
async def delete_task_by_id(
    task_id: int,
    session: Session = Depends(get_db),
    current_user: dict = Depends(utils.get_current_user)
    ) -> Dict[str,str]:
    deleted_task = task.delete_task(session, task_id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

