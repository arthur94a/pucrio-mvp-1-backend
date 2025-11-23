from model import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Comments(Base):
    __tablename__ = "Comentario"

    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(15))
    password: Mapped[bytes] = mapped_column(LargeBinary) 
    comment: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.utcnow)
    updated_at: Mapped[datetime | none] = mapped_column(DateTime(), onupdate=datetime.utcnow)
    