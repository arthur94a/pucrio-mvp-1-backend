from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from model.comment import Comment

class CommentBase(BaseModel):
    username: str = Field(default="johndoe", max_length=15)
    comment: str


class CreateCommentSchema(CommentBase):
    password: str = Field(min_length=4, max_length=30)


class CommentSchema(CommentBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None


class ListCommentsSchema(BaseModel):
    comments: List[CommentSchema]

def show_comment(comment: Comment):
    """ Retorna uma representação do comentario seguindo o schema definido em
        CommentSchema.
    """
    return {
        "id": comment.id,
        "username": comment.username,
        "comment": comment.comment,
        "created_at": comment.created_at,
        "updated_at": comment.updated_at
    }
