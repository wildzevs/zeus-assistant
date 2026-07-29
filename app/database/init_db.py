from app.database.base import Base
from app.database.session import engine

# импортируем модели, чтобы SQLAlchemy их увидела
from app.models.user import User  # noqa: F401


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)