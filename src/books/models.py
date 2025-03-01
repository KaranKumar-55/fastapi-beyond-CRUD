from sqlmodel import SQLModel, Field, Column
from datetime import datetime, date
import sqlalchemy.dialects.postgresql as pg
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
import uuid

class Book(SQLModel, table=True):
    
    __tablename__ = "books"

    ## create unique id in postgresql database
    uid: uuid.UUID = Field(sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4))
    title: str
    author: str
    publisher:str
    published_date: date
    page_count: int
    language: str
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))


# class Book(SQLModel, table=True):
#     __tablename__ = "books"

#     uid: uuid.UUID = Field(default_factory=uuid.uuid4, sa_column=Column(UUID(as_uuid=True), primary_key=True))
#     title: str
#     author: str
#     publisher: str
#     published_date: date
#     page_count: int
#     language: str
#     created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(TIMESTAMP, default=datetime.utcnow))
#     update_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(TIMESTAMP, default=datetime.utcnow))

def __repr__(self):
    return f"<Book {self.title}>"