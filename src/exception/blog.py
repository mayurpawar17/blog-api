from src.exception.app_exception import AppException


class PostNotFoundException(AppException):
    """Exception raised when a blog post is not found."""
    def __init__(self, post_id: int):

        super().__init__(message = f"Post with ID {post_id} not found.", code = "POST_NOT_FOUND", status_code = 404)