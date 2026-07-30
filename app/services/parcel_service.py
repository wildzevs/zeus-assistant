from sqlalchemy import select

from app.database.session import SessionLocal
from app.models.parcel import Parcel
from app.models.user import User


class ParcelService:

    @staticmethod
    async def add_parcel(
        telegram_id: int,
        track_number: str,
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            user = result.scalar_one()

            parcel = Parcel(
                user_id=user.id,
                track_number=track_number,
            )

            session.add(parcel)

            await session.commit()

            return parcel

    @staticmethod
    async def get_user_parcels(
        telegram_id: int,
    ):

        async with SessionLocal() as session:

            result = await session.execute(
                select(User).where(
                    User.telegram_id == telegram_id
                )
            )

            user = result.scalar_one()

            result = await session.execute(
                select(Parcel).where(
                    Parcel.user_id == user.id
                )
            )

            return result.scalars().all()