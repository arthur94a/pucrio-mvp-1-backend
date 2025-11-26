from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
import bcrypt

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update

from model import Session

from model import Comment
from schemas.comments import CreateCommentSchema, ListCommentsSchema, show_comment, show_comments, EditCommentSchema

from flask_cors import CORS

info = Info(title="MVP 1 API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

tag_list = Tag(name="Listar comentários", description="Lista os comentários em ordem de 10 por vez, query 'page'.")
tag_add = Tag(name="Adicionar comentário", description="Adição de um comentário a base.")
tag_edit = Tag(name="Editar comentário", description="Edita um comentário existente, exige o password.")

@app.get("/")
def home():
    return redirect("/openapi")


@app.get("/list", tags=[tag_list], responses={"200": ListCommentsSchema})
def list_comments():
    page = request.args.get('page', 1, type=int)
    COMMENTS_PER_PAGE = 10
    MAX = COMMENTS_PER_PAGE * page
    MIN = MAX - COMMENTS_PER_PAGE + 1

    with Session() as session:
        stmt = select(Comment).where((Comment.id >= MIN) & (Comment.id <= MAX))
        comments = session.execute(stmt).scalars().all()
        return show_comments(comments), 200
    

@app.post("/add", tags=[tag_add], responses={"200": CreateCommentSchema})
def add_comment(body: CreateCommentSchema):
    with Session() as session:
        hashed = bcrypt.hashpw(body.password.encode("utf-8"), bcrypt.gensalt())
        # hashed = body.password

        comment = Comment(
            username=body.username,
            password_hash=hashed,
            comment=body.comment
        )

        session.add(comment)
        session.commit()
        session.refresh(comment)

        return show_comment(comment), 200


@app.post("/edit", tags=[tag_edit], responses={"200": EditCommentSchema})
def edit_comment(body: EditCommentSchema):
    with Session() as session:
        id = body.id
        newComment = body.comment

        stmt = update(Comment).where(Comment.id == id).values(
            comment=newComment
        )

        session.execute(stmt)

        session.commit()

        comment_updated = session.get(Comment, id)
        
        if not comment_updated:
            return {"error": "Comentário não encontrado"}, 404

        return show_comment(comment_updated), 200
