from fastapi import Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
import msal
import requests
import jwt

from typing import List, Annotated
import datetime

from ..models import AzureResponse, AuthUser
from ..config import settings

msal_app = msal.ConfidentialClientApplication(
        settings.AZURE_CLIENT_ID,
        authority=f"{settings.AZURE_RESOURCE}/{settings.AZURE_TENANT}",
        client_credential=settings.AZURE_CLIENTSECRET,
        )


oauth2_scheme = OAuth2AuthorizationCodeBearer(authorizationUrl=msal_app.authority.authorization_endpoint,
                                              tokenUrl='/token',
                                              refreshUrl=msal_app.authority.token_endpoint,
                                            #   scopes=msal_app._decorate_scope([]) # doesnt work but ok
                                              )


TEMP_AUTH_FLOW = {}


def get_openid_auth_uri():
    
    flow = msal_app.initiate_auth_code_flow(scopes=[], #openid scopes are added automatically, no need to add
                                            redirect_uri=settings.AZURE_REDIRECT)
    
    TEMP_AUTH_FLOW.update({flow['state']: flow})

    return flow['auth_uri']


def fetch_cache_flow(state: str) -> dict:
    print(f'{TEMP_AUTH_FLOW=}')
    tmp_value = TEMP_AUTH_FLOW.get(state).copy()
    del TEMP_AUTH_FLOW[state]

    print(f'{TEMP_AUTH_FLOW=}')
    print(f'{tmp_value=}')
    return tmp_value


def exchange_code_for_azure_token(azure_response: AzureResponse) -> dict:

    print('in exchage')

    initial_flow = fetch_cache_flow(azure_response.state)

    auth_resp = msal_app.acquire_token_by_auth_code_flow(auth_code_flow=initial_flow, 
                                                         auth_response=azure_response.model_dump())

    return auth_resp


def get_entra_id_groups_with_token(auth_resp: dict) -> List:

    azure_token = f"Bearer {auth_resp['access_token']}"

    msft_graph_endpoint = settings.MSFT_GRAPH + f"/{auth_resp['id_token_claims']['oid']}" +'/memberOf'

    user_group_resp = requests.get(msft_graph_endpoint, headers={'Authorization': azure_token}).json()

    user_groups = []
    for dict_grp in user_group_resp['value']:
        if dict_grp['@odata.type'] == '#microsoft.graph.group':
            user_groups.append(dict_grp['id'])

    return user_groups


def get_user_access_from_groups(user_groups: List) -> str:

    if settings.ENTRA_ID_GROUP_ACCESS2 in user_groups:
        return 'Top level access'
    
    if settings.ENTRA_ID_GROUP_ACCESS1 in user_groups:
        return '2nd level access'
    
    return 'No access'


def create_api_access_token(user: str, access_level: str):

    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {
        "sub": user,
        "access_level": access_level,
        "exp": expire
        }
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> AuthUser:
    """get user from token that was passed in a request

    Args:
        token (Annotated[str, Depends): Takes the bearer token from request

    Returns:
        AuthUser: User with its access level
    """    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user: str = payload.get("sub")
        access_level: str = payload.get("access_level")

        print(f'{user=}')
        print(f'{access_level=}')

        #TODO: terrible error handling
        if (access_level is None):
            raise Exception
        if (access_level == 'No access'):
            raise Exception
        
    except Exception:
        raise Exception()

    return AuthUser(username=user, access_level=access_level)



# def get_user_access(params):
    
#     token = f"Bearer {params['access_token']}"
#     print(f'{token=}')

#     results = requests.get(settings.MSFT_GRAPH 
#                            + f"/{params['id_token_claims']['oid']}" 
#                            +'/memberOf', 
#                            headers={'Authorization': token}).json()
#     access = ''
#     for dict_grp in results['value']:
#         if dict_grp['@odata.type'] == '#microsoft.graph.group':
#             access = dict_grp['id']
        
#     return {'preferred_username': params['preferred_username'], 'access': access}

     

# from fastapi.security import OpenIdConnect, OAuth2PasswordBearer
# from fastapi.security.o