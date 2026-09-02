class AppException(Exception):
    """Base class for all exceptions in the application."""
    def __init__(self,message:str,code:str,status_code:int):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(self.message)