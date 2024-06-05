from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class AuthUser(BaseModel):
    username: str
    access_level: str


class AzureResponse(BaseModel):
    code: str
    client_info: str
    state: str
    session_state: str


class OauthCodeResp(BaseModel):
    code: str
    client_info: str
    state: str
    session_state: str


