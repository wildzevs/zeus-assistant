from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    telegram_id: Mapped[int] = mapped_column(
        Integer,
        unique=True,
        index=True,
    )

    display_name: Mapped[str] = mapped_column(
        String(100),
        default="Пользователь",
    )

    city: Mapped[str] = mapped_column(
        String(100),
        default="Ростов-на-Дону",
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        default=47.2357,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        default=39.7015,
    )

    timezone: Mapped[str] = mapped_column(
        String(50),
        default="Europe/Moscow",
    )

    daily_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    daily_time: Mapped[str] = mapped_column(
        String(5),
        default="07:00",
    )

    parcels = relationship(
        "Parcel",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )