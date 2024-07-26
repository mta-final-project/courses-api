from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class MongoSettings(BaseModel):
    url: str = "mongodb://user:pass@localhost:27017"
    database: str = "academease"


class S3Settings(BaseModel):
    access_key_id: str
    secret_access_key: str
    session_token: str
    region: str
    bucket_name: str = "academease"
    presigned_url_expiration: int = 3600


class CognitoSettings(BaseModel):
    client_id: str = "6r70ag4thnsitfb378fh87tj92"
    pool_id: str = "us-east-1_U2F78N1y3"
    region: str = "us-east-1"
    jwk_url: str = (
        f"https://cognito-idp.{region}.amazonaws.com/{pool_id}/.well-known/jwks.json"
    )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    api: ApiSettings = ApiSettings()
    mongo: MongoSettings = MongoSettings()
    s3: S3Settings = S3Settings()
    cognito: CognitoSettings = CognitoSettings()


@lru_cache
def get_settings():
    return Settings()
