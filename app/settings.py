from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # DB
    DB_HOST: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # JWT
    JWT_TOKEN_LIFETIME_MINUTES: int


settings = Settings()  # type: ignore
