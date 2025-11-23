from datetime import datetime
from sqlalchemy import String, LargeBinary, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from model import Base


class Comment(Base):
    __tablename__ = "Comentario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(15), nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.utcnow
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(), onupdate=datetime.utcnow
    )
