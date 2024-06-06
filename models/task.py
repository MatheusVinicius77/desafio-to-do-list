from database.database import Base
from sqlalchemy import Column , String, DateTime, Integer , Enum as SqlAlchemyEnum
from enum import Enum


class TaskState(str,Enum):
    PENDING = "pending"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer,autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    state = Column(SqlAlchemyEnum(TaskState), nullable=False)
    data_creation = Column(DateTime)
    data_atualization = Column(DateTime, default="pending")


