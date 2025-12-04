# MVP 1 API -- PUC-Rio

This REST API was developed as part of the MVP for the PUC-Rio
postgraduate program. It allows a frontend application to perform CRUD
operations on comments. Each comment has its own password, which is
required for editing and deleting.

> **API REST desenvolvida como parte do MVP da pós-graduação da PUC-Rio.Permite que um frontend realize operações CRUD em comentários. Cada comentário possui uma senha própria, necessária para edição e exclusão.**

---

## 📘 General Information

-   **Base URL:** `http://<your-server>/`
-   **Format:** JSON
-   **Authentication:** Password per comment
-   **Documentation:** `/openapi`

### Techs

Python | Flask | Pydantic | SQLAlchemy | Bcrypt

---

## TO INSTALL

**obs: If Docker is your preferred option, skip to the next topic.**

All libs are listed in `requirements.txt`. It is required to automatically install all dependencies.

> Recommended for use with [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Fast start with virtualenv:

(1) Install the lib:

```
pip install virtualenv

```
(1.2) Create the enviroment folder:

```
virtualenv venv

```
(1.3) Activate enviroment:

(1.3.1) windows

```
venv\Scripts\activate

```

(1.3.2) Linux/macOS

```
source venv/bin/activate

```

(2) Install dependencies:

```
(env)$ pip install -r requirements.txt
```

(3) Install the tools for documentation:

```
(env)$  pip install -U flask-openapi3[swagger,redoc,rapidoc,rapipdf,scalar,elements]
```

(4) Run the follow commando to start API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```
---

## DO YOU USE DOCKER?
Just run:

    docker compose up --build

---

# 📚 Endpoints

## 🏠 GET `/`

Redirects to the OpenAPI documentation page.

---

## 📄 GET `/list`

Returns comments in batches of 10.

### Query Parameters

-   `last_id` *(optional)* --- used for infinite scroll pagination.

### Example

    GET /list?last_id=25

---

## ✏️ POST `/create`

Creates a new comment.

### Request Body

``` json
{
  "username": "johndow",
  "password": "myPassword",
  "comment": "My comment"
}
```

### Response

``` json
{
  "id": 42,
  "username": "johndoe",
  "comment": "My comment",
  "created_at": "2025-12-03T19:05:00"
}
```

---

## 🛠 PUT `/update`

Edits an existing comment.\
**Password is required.**

### Request Body

``` json
{
  "id": 42,
  "password": "myPassword",
  "comment": "Updated content"
}
```

---

## 🗑 DELETE `/delete`

Deletes an existing comment.\
**Password is required.**

### Request Body

``` json
{
  "id": 42,
  "password": "myPassword"
}
```

---

# 🔐 Security

-   Passwords are stored using **bcrypt**.
-   Passwords cannot be recovered --- only validated.

---

# 🗃 Comment Object Structure

``` json
{
  "id": 1,
  "username": "string",
  "comment": "string",
  "password_hash": "bytes",
  "created_at": "datetime",
  "updated_at": "datetime?"
}
```
