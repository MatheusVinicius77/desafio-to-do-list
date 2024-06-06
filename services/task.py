from schemas.task import TaskSchema
from sqlalchemy.orm import Session
from datetime import datetime
from models.task import TaskModel
from schemas.task import TaskSchema, TaskCreateSchema, TaskUpdateSchema

from fastapi import HTTPException



def get_task_by_id(db:Session, task_id:int) -> TaskModel:
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def get_all_tasks(db:Session):
    return db.query(TaskModel).all()


def update_task(db:Session, task_id:int ,change_task: TaskUpdateSchema) -> TaskModel:

    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if change_task.title is not None:
        task.title = change_task.title
    if change_task.description is not None:
        task.description = change_task.description
    if change_task.state is not None:
        task.state = change_task.state
    
    task.data_atualization = datetime.utcnow()
    db.commit()
    db.refresh(task)

    return task


def delete_task(db: Session, task_id: int) -> TaskModel:
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task


def create_task(db:Session, task: TaskCreateSchema) -> TaskModel:

    new_task = TaskModel(
        title=task.title,
        description=task.description,
        state=task.state,
        data_creation=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        data_atualization=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task