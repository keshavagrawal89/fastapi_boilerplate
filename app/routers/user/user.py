from fastapi import APIRouter, Request


from app.utils.decorators import public_route, protected_route
from app.resources.user import get_user_profile


router = APIRouter()

@router.get("/profile/")
@protected_route()
def get_profile(request: Request):
    return get_user_profile()

@router.get("/subscriptions/")
@protected_route()
def get_subscriptions(request: Request):
    return {"subscriptions": "user subscriptions"}

@router.get("/public-info/")
@public_route()
def get_public_info():
    return {"info": "public information"}
