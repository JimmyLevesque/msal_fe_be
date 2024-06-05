import dash
from dash import html, callback, Input, Output, State, dcc
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import requests
import webbrowser
import time

from urllib.parse import urlparse, parse_qs


from config import settings

dash.register_page(
    __name__,
    path='/login',
    title='Login'
)

layout = html.Div(
    [
        html.H1('This is login page'),

        html.Button('Click to login', 
                    id='btn-login', 
                    n_clicks=0,
                    style={'width': '200px',
                           'margin-bottom': '10px',
                           'margin-left': '10px',}), 
        html.Br(),
        html.Br(),
        html.Div(id='login-status', children=[html.H3('You are not logged in')]),

        html.Textarea('Lets see'),
        html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(id='content'),
            ]
            )
    ]
)



@callback(
    Output('login-status', 'children'),
    Input('btn-login', 'n_clicks'), 
    prevent_initial_call=True
)
def login_btn(n_clicks):
    print(f'logging login, {n_clicks=}')

    if n_clicks == 0: #check if user is logged in (ie. has token)
        print('prevented update')
        raise PreventUpdate
    
    api_url = settings.API_URL
    
    print('before request')
    resp = requests.get(api_url + '/login',  verify=False, allow_redirects=False)
    

    print(resp)
    print(resp.headers['Location'])
    webbrowser.open_new(resp.headers['Location'])
    print('after redirect')

    return html.H3('first step in logging in')



@callback(
        Output('content', 'children'),
        Input('url', 'href'),
        prevent_initial_call=True)
def get_url_params(href: str):

    parsed_url = urlparse(href)
    param_dict = parse_qs(parsed_url.query)
    print(parsed_url.path.split('/'))
    print(f'{param_dict=}')

    if parsed_url.path.split('/')[-1] != 'login':
        print('callback prevented not in login page')
        raise PreventUpdate
    
    if param_dict == {}:
        print('callback prevented in login page, but no callback')
        raise PreventUpdate
    
    cleaned_params = {k: v[0] for k, v in param_dict.items()}

    api_url = settings.API_URL
    resp = requests.get(api_url + '/login',  verify=False)
    

    return html.P(children=[f"{k}: {v[0]} \n" for k, v in param_dict.items()] )