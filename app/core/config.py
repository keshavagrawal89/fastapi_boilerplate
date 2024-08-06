from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()