from sqlmodel import SQLModel, Field, Column
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid

class Book(SQLModel, table=True):
    
    __tablename__ = "books"

    ## create unique id in postgresql database
    uid: uuid.UUID = Field(sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4()))
    title: str
    author: str
    publisher:str
    published_date: str  
    page_count: int
    language: str
    created_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(Column(pg.TIMESTAMP, default=datetime.now))


def __repr__(self):
    return f"<Book {self.title}>"