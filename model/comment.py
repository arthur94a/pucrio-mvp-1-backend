from model import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Comment(Base):
    __tablename__ = "Comentario"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(15), nullable=False)
    password_hash: Mapped[bytes] = mapped_column(LargeBinary, nullable=False) 
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.utcnow)
    updated_at: Mapped[datetime | none] = mapped_column(DateTime(), onupdate=datetime.utcnow)
    