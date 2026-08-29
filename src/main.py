from fastapi import FastAPI

app = FastAPI(title="Blog API", version="1.0.0")

#mock database
posts = [
    {
        "id": 1,
        "title": "Getting Started with Python FastAPI",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python based on standard Python type hints.",
        "author": "Alice Johnson",
    },
    {
        "id": 2,
        "title": "Understanding Feature-First Architecture",
        "content": "Structuring applications by feature rather than by technical layers improves maintainability and keeps related code co-located.",
        "author": "Bob Smith",
    },
    {
        "id": 3,
        "title": "Mastering Pydantic for Data Validation",
        "content": "Pydantic simplifies data validation and serialization in Python using standard type annotations.",
        "author": "Carol White",
    },
    {
        "id": 4,
        "title": "Asynchronous Programming in Python",
        "content": "Asyncio enables concurrent execution of I/O bound operations without using traditional multi-threading.",
        "author": "David Lee",
    },
    {
        "id": 5,
        "title": "Building RESTful APIs Best Practices",
        "content": "Learn how to structure endpoints, use correct HTTP methods, and handle error responses gracefully.",
        "author": "Elena Rostova",
    },
]


@app.get("/")
def root():
    return {"message": "Welcome to the Blog API"}

@app.get("/blog")
def blog():
    return posts


@app.get("/blog/{id}")
def blog_by_id(id:int):
    for post in posts:
        if post["id"] == id:
            return post
    return {"message": "Post not found"}