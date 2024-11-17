from typing import Literal

from pydantic import ConfigDict, PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: str

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str = ''

    @field_validator('DATABASE_URL', mode='before')
    def assemble_db_connection(cls, v, info: ValidationInfo):
        values = info.data
        return f"postgresql+asyncpg://{values['DB_USER']}:{values['DB_PASS']}@{values['DB_HOST']}:{values['DB_PORT']}/{values['DB_NAME']}"
    


    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str
    TEST_DATABASE_URL: str = ""
    
    @field_validator('TEST_DATABASE_URL', mode='before')
    def assemble_test_db_connection(cls, v, info: ValidationInfo):
        values = info.data
        return f"postgresql+asyncpg://{values['TEST_DB_USER']}:{values['TEST_DB_PASS']}@{values['TEST_DB_HOST']}:{values['TEST_DB_PORT']}/{values['TEST_DB_NAME']}"
    
    SECRET_KEY: str
    ALGHORITHM: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    
    REDIS_HOST: str
    REDIS_PORT: int
    

    model_config = ConfigDict(env_file=".env", arbitrary_types_allowed=True) # type: ignore

settings = Settings() # type: ignore