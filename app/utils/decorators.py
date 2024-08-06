from fastapi import HTTPException, Request
from functools import wraps

def public_route():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

def protected_route():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request: Request = kwargs.get("request")
            if not request.state.user:
                raise HTTPException(status_code=403, detail="Not authenticated")
            return func(*args, **kwargs)
        return wrapper
    return decorator
