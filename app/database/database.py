from sqlalchemy import create_engine,inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv('.env')

username:str = os.getenv("POSTGRESUSER")
password:str = os.getenv("POSTGRESPASSWORD")
db_server:str = os.getenv("POSTGRESSERVER")
db_name:str = os.getenv("POSTGRESDB")
db_port:int = os.getenv("POSTGRESPORT", 5432)

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{db_server}:{db_port}/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

