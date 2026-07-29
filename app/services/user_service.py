from sqlalchemy import select

from app.database.session import SessionLocal
from app.models.user import User


class UserService:

    @staticmethod
    async def get_user(telegram_id: int) -> User | None:
        async with SessionLocal() as session:
            result = await session.execute(
                select(User).where(User.telegram_id == telegram_id)
            )
            return result.scalar_one_or_none()

    @staticmethod
    async def create_user(
        telegram_id: int,
        first_name: str,
    ) -> User:
        async with SessionLocal() as session:

            user = User(
                telegram_id=telegram_id,
                display_name=first_name,
            )

            session.add(user)

            await session.commit()
            await session.refresh(user)

            return user

    @staticmethod
    async def get_or_create(
        telegram_id: int,
        first_name: str,
    ) -> User:

        user = await UserService.get_user(telegram_id)

        if user:
            return user

        return await UserService.create_user(
            telegram_id,
            first_name,
        )