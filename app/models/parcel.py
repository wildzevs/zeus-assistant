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
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(150),
        default="",
    )

    carrier: Mapped[str] = mapped_column(
        String(100),
        default="",
    )

    status: Mapped[str] = mapped_column(
        String(200),
        default="Ожидает проверки",
    )

    status_code: Mapped[str] = mapped_column(
        String(50),
        default="pending",
    )

    last_location: Mapped[str] = mapped_column(
        String(200),
        default="",
    )

    last_checked: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
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