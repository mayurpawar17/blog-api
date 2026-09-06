from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from src.exception.app_exception import AppException
from src.exception.blog import PostNotFoundException
from src.exception.handlers import app_exception_handler
from src.schemas.response import ApiResponse, ErrorResponse

app = FastAPI(title="Blog API", version="1.0.0")


app.add_exception_handler(
    AppException,
    app_exception_handler,
)

# mock database
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
    print(f"Fetching all blog posts {len(posts)}")
    return posts


@app.get("/shipment")
def shipment(shipment_id: int | None = None):
    if shipment_id is None or shipment_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment ID must be a positive integer",
        )
    return {
        "shipment_id": shipment_id,
        "status": "In Transit",
        "estimated_delivery": "2024-06-15",
        "origin": "New York, NY",
        "destination": "Los Angeles, CA",
    }


@app.get("/shipment/{shipment_id}")
def shipment_by_id(shipment_id: int):
    if shipment_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment ID must be a positive integer",
        )
        
    return {
        "shipment_id": shipment_id,
        "status": "In Transit",
        "estimated_delivery": "2024-06-15",
        "origin": "New York, NY",
        "destination": "Los Angeles, CA",
    }


@app.get("/blog/{id}")
def blog_by_id(id: int):

    for post in posts:
        if post["id"] == id:
            return ApiResponse(success=True, data=post)
    raise PostNotFoundException(post_id=id)


@app.get("/scalar", include_in_schema=False)
async def scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )   