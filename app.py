from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from sqlalchemy.exc import IntegrityError

from flask_cors import CORS

info = Info(title="MVP 1 API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

@app.get("/")
def home():
    return redirect("/openapi")