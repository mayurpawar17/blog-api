# Blog API

A simple FastAPI blog API with mock blog posts.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended)

## Install dependencies

Using uv:

```bash
uv sync
```

If you prefer pip:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Run the application

```bash
uv run uvicorn src.main:app --reload
```

Or, if your virtual environment is already active:

```bash
uvicorn src.main:app --reload
```

The API will start locally at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/blog
- http://127.0.0.1:8000/blog/1

## Available endpoints

- `GET /` — welcome message
- `GET /blog` — list all blog posts
- `GET /blog/{id}` — fetch a blog post by ID

## Development notes

This project uses FastAPI and is configured with a `pyproject.toml` file for dependency management.
