from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Parcel(Base):
    __tablename__ = "parcels"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )

    track_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(100),
        default="Посылка",
    )

    carrier: Mapped[str] = mapped_column(
        String(100),
        default="Не определён",
    )

    status: Mapped[str] = mapped_column(
        String(200),
        default="Добавлена",
    )

    last_location: Mapped[str] = mapped_column(
        String(200),
        default="-",
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship(
        "User",
        back_populates="parcels",
    )