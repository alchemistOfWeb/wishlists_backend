from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "app"
    SECRET_KEY: str = "super_secret_key"

    class Config:
        env_file = ".env"

settings = Settings()