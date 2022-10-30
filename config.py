from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Forecast API"
    api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
