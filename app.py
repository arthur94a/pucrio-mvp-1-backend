from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
import bcrypt

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete

from model import Session

from model import Comment
from schemas.comments import CreateCommentSchema, ListCommentsSchema, show_comment, show_comments, EditCommentSchema, DeleteCommentSchema

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
    

@app.post("/create", tags=[tag_add], responses={"200": CreateCommentSchema})
def create_comment(body: CreateCommentSchema):
    with Session() as session:
        hashed = bcrypt.hashpw(body.password.encode("utf-8"), bcrypt.gensalt())

        comment = Comment(
            username=body.username,
            password_hash=hashed,
            comment=body.comment
        )

        session.add(comment)
        session.commit()
        session.refresh(comment)

        return show_comment(comment), 200


@app.post("/update", tags=[tag_edit], responses={"200": EditCommentSchema})
def update_comment(body: EditCommentSchema):
    with Session() as session:
        id = body.id
        newComment = body.comment
        comment = session.get(Comment, id)

        password_form = body.password.encode("utf-8")

        if not comment:
            return {"error": "Comentário não encontrado"}, 404

        password_db = comment.password_hash

        if not bcrypt.checkpw(password_form, password_db):
            return {"error": "Senha incorreta"}, 401

        stmt = update(Comment).where(Comment.id == id).values(
            comment=newComment
        )

        session.execute(stmt)

        session.commit()

        comment_updated = session.get(Comment, id)
        
        if not comment_updated:
            return {"error": "Comentário não encontrado"}, 404

        return show_comment(comment_updated), 200

@app.post("/delete", responses={"200": DeleteCommentSchema})
def delete_comment(body: DeleteCommentSchema):
    with Session() as session:
        id = body.id

        comment = session.get(Comment, id)
        if not comment:
            return {"error": "Comentário não encontrado"}, 404

        password_form = body.password.encode("utf-8")
        password_db = comment.password_hash

        if not bcrypt.checkpw(password_form, password_db):
            return {"error": "Senha incorreta"}, 401

        delete_stmt = delete(Comment).where(Comment.id == id)

        session.execute(delete_stmt)

        session.commit()

        comment_to_delete = session.get(Comment, id)

        if comment_to_delete:
            return {"error": "Comentário não deletado"}, 404
        
        return {"succes": "Comentário deletado"}, 200
