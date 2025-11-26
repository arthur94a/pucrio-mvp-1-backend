
All libs are listed in `requirements.txt`. It is required to automatically install all dependencies.

> Recommended for use with [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Install dependencies:

```
(env)$ pip install -r requirements.txt
```

Install the tools for documentation:

```
(env)$  pip install -U flask-openapi3[swagger,redoc,rapidoc,rapipdf,scalar,elements]
```

Run the follow commando to start API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```