from fastapi import FastAPI
from supabase import create_client


from app.core.config import settings
from app.routers import user
from app.middlewares.auth import CustomAuthMiddleware
from app.db import database


app = FastAPI()

# Create Supabase client
supabase = create_client(settings.supabase_url, settings.supabase_key)

# Add middleware
app.add_middleware(CustomAuthMiddleware, supabase=supabase)

# Include the user router
app.include_router(user.router, prefix="/api/v1/user")

@app.on_event("startup")
def startup():
    pass  # Database pool is initialized at import

@app.on_event("shutdown")
def shutdown():
    database.close_all_connections()

@app.get("/api/v1/health")
def read_health():
    return {"status": "ok"}
