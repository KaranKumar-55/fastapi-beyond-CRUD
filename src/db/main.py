from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from src.config import Config
from sqlalchemy.future import select

engine = AsyncEngine(
    create_engine(
    url = Config.DATABASE_URL,
    echo = True)
)

async def init_db():
    async with engine.begin() as conn:
        statement = text("Select 'hello';")

        result = await conn.execute(statement)
        print(result.all())

    
