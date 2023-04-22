from pydantic import BaseSettings


class Settings(BaseSettings):
    CONSUMER_KEY: str
    CONSUMER_SECRET: str

    class Config:
        env_file = ".env"

settings = Settings()