from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Settings(BaseSettings):
    AZURE_TENANT: str
    AZURE_CLIENT_ID: str
    AZURE_CLIENTSECRET: str
    AZURE_RESOURCE: str
    AZURE_REDIRECT: str
    MSFT_GRAPH: str
    ENTRA_ID_GROUP_ACCESS1: str
    ENTRA_ID_GROUP_ACCESS2: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()
