from db import engine, Base
from user import User
from task import Task

Base.metadata.create_all(bind=engine)