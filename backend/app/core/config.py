from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AgroRobust AI"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 8
    database_url: str = "postgresql+psycopg2://agro:agro@db:5432/agrodb"
    cors_origins: list[str] = ["*"]
    artifacts_dir: str = "artifacts"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
