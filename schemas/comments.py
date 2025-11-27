from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
from model.comment import Comment

class CommentBase(BaseModel):
    username: str = Field(default="johndoe", max_length=15)
    comment: str


class CommentSchema(CommentBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None


class CreateCommentSchema(CommentBase):
    password: str = Field(min_length=4, max_length=30)


class EditCommentSchema(CommentSchema):
    password: str = Field(min_length=4, max_length=30)


class ListCommentsSchema(BaseModel):
    comments: List[CommentSchema]

class DeleteCommentSchema(CommentSchema):
    password: str = Field(min_length=4, max_length=30)

def show_comments(comments: List[Comment]):
    """ Retorna a lista de comentarios seguindo o schema definido em
        CommentSchema.
    """
    result = []
    for comment in comments:
        result.append(comment.to_dict())

    return {"comments": result}

def show_comment(comment: Comment):
    """ Retorna uma representação do comentario seguindo o schema definido em
        CommentSchema.
    """
    return comment.to_dict()
