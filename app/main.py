from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task
from sqlalchemy.schema import CreateTable

Base.metadata.create_all(bind=engine)

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
