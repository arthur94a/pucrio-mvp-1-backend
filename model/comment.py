from datetime import datetime
from sqlalchemy import String, LargeBinary, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from model import Base


class Comment(Base):
    __tablename__ = "Comentario"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(15), nullable=False)
    password_hash: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.utcnow
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(), onupdate=datetime.utcnow
    )

    def __init__(self, username:str, password_hash:str, comment:str):
        """
        Cria um 'Comment'

        Arguments:
            username: Usuário para definir o dono do comentário.
            password_hash: Senha para autenticação
            comment: Texto do conteúdo
            created_at: Data de quando o comentário foi inserido à base
        """
        self.username = username
        self.password_hash = password_hash
        self.comment = comment

    def to_dict(self):
        """ Converte para JSON
        """
        
        return {
            "id": self.id,
            "username": self.username,
            "comment": self.comment,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
