from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
# from passlib.hash import bcrypt

from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert, select

from model import Session, engine

from model import Comment
from schemas.comments import CreateCommentSchema, ListCommentsSchema, show_comment, show_comments

from flask_cors import CORS

info = Info(title="MVP 1 API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

comment_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")

@app.get("/")
def home():
    return redirect("/openapi")


@app.get("/list", responses={"200": ListCommentsSchema})
def list_comments():
    page = request.args.get('page', 1, type=int)
    COMMENTS_PER_PAGE = 10
    MAX = COMMENTS_PER_PAGE * page
    MIN = MAX - COMMENTS_PER_PAGE + 1

    with Session() as session:
        stmt = select(Comment).where((Comment.id >= MIN) & (Comment.id <= MAX))
        comments = session.execute(stmt).scalars().all()
        return show_comments(comments), 200
    

@app.post("/add", tags=[comment_tag], responses={"200": CreateCommentSchema})
def add_comment(body: CreateCommentSchema):
    with Session() as session:
        # hashed = bcrypt.hash(body.password)
        hashed = body.password

        comment = Comment(
            username=body.username,
            password_hash=hashed,
            comment=body.comment
        )

        session.add(comment)
        session.commit()
        session.refresh(comment)

        return show_comment(comment), 200