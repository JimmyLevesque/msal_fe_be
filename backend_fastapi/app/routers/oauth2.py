from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from ..utils.auth import (get_openid_auth_uri, 
                          exchange_code_for_azure_token,
                          get_entra_id_groups_with_token,
                          get_user_access_from_groups,
                          create_api_access_token)
from ..models import AzureResponse

router = APIRouter(tags=['Oauth2'])



@router.get('/initiate_login', 
            response_class=RedirectResponse, 
            status_code=status.HTTP_307_TEMPORARY_REDIRECT)
def initiate_login():

    print('got in login')

    auth_uri = get_openid_auth_uri()

    return auth_uri



@router.post('/token')
def login_for_access_token(azure_resp: AzureResponse):

    print('got in login part 2')

    auth_resp = exchange_code_for_azure_token(azure_resp)

    user_groups = get_entra_id_groups_with_token(auth_resp)
    print(f'{user_groups=}')

    access_level = get_user_access_from_groups(user_groups)
    print(f'{access_level=}')

    user = auth_resp.get('id_token_claims').get('preferred_username')

    encoded_jwt = create_api_access_token(user=user,
                                          access_level=access_level)


    return encoded_jwt


