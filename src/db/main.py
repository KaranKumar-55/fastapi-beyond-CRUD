from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession


async_engine = AsyncEngine(
    create_engine(
    url = Config.DATABASE_URL,
    echo = True)
)

async def init_db():
    async with async_engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)

        # statement = text("Select 'hello';")

        # result = await conn.execute(statement)
        # print(result.all())

async def get_session()-> AsyncSession:
    Session = sessionmaker(
        bind = async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with Session() as session:
        yield session
