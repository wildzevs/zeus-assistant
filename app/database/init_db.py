from app.database.base import Base
from app.database.session import engine

from app.models.parcel import Parcel  # noqa
from app.models.user import User  # noqa


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)