import dash
from dash import html, callback, Input, Output, dcc
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import requests
import webbrowser
import time

from config import settings

dash.register_page(
    __name__,
    path='/',
    redirect_from=['/home'],
    title='Home'
)

layout = html.Div(
    [
        html.H1('This is home'),

        # html.Button('Click to login', 
        #             id='btn-login', 
        #             n_clicks=0,
        #             style={'width': '200px',
        #                    'margin-bottom': '10px',
        #                    'margin-left': '10px',}), 
        # html.Br(),
        # html.Br(),
        # html.Div(id='login-status', children=[html.H3('You are not logged in')])

    ]
)


# @callback(
#     [Output('store-data-flow', 'data'),
#      Output('login-status', 'children')],
    
#     Input('btn-login', 'n_clicks'), 
#     prevent_initial_call=True
# )
# def login_btn(n_clicks):
#     print(f'logging login, {n_clicks=}')

#     if n_clicks == 0:
#         print('prevented update')
#         raise PreventUpdate
    
#     api_url = settings.API_URL
    
#     resp_flow = requests.get(api_url + '/login',  verify=False)

#     data = resp_flow.json()
#     print(f'{data=}')

#     return data, html.H3('first step in logging in')
    

# @callback(
#     Input('store-data-flow', 'data'), 
#     prevent_initial_call=True
# )
# def redirect(data):

#     print('logging login again')
#     print(f'{data=}')

#     if data is None:
#         print('prevented update')
#         raise PreventUpdate

#     time.sleep(1)

#     webbrowser.open_new(data['auth_uri'])

#     return None

    

    

    # print(resp.json())
    # webbrowser.open(url=resp.json()['auth_uri'], new=2)
    # html.A(
    #             dbc.Row(
    #                 [
    #                     dbc.Col(html.H3("Link to Plotly"))
    #                 ],
    #                 align='center',
    #                 className='g-0',
    #             ),
    #             href='https://plotly.com',
    #             style={'textDecoration': 'none'},
    #         ),

    # return [dcc.Link(href=resp.json()['auth_uri'])]



