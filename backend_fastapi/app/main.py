from fastapi import FastAPI, status, Depends
from fastapi.responses import RedirectResponse

from typing import Annotated

from .models import AuthUser
from .utils.auth import get_current_user
from .routers import oauth2

app = FastAPI()

app.include_router(oauth2.router)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello world no auth needed"}




# is_in_cache = False
# def get_refresh_token():
#     pass
# get_refresh_token_sucess = True


# @app.get('/login',  response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
# def initiate_login():
#     print('got in login')

#     # if is_in_cache:
#     #     get_refresh_token()
#     #     if get_refresh_token_sucess:
#     #         return 1
    
#     flow = get_openid_auth_uri()

#     return flow['auth_uri']





# @app.get("/callback") #, response_model=OauthCodeResp)
# def auth_path(params):
#     print("in callback")
#     user_acess = get_user_access()

#     return user_acess


@app.get("/fastapi", response_class=RedirectResponse, status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def redirect_fastapi():
    return "https://fastapi.tiangolo.com"



@app.get("/get_info")
def read_own_items(
    current_user: Annotated[AuthUser, Depends(get_current_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username, "acc": current_user.access_level}]