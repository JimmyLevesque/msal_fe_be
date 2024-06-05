# import dash
# from dash import html, dcc, Input, Output, State, callback
# from dash.exceptions import PreventUpdate
# import requests

# from urllib.parse import urlparse, parse_qs
# from config import settings

# dash.register_page(
#     __name__,
#     path='/callback',
#     title='Login'
# )

# layout = html.Div(
#     [
#         html.H1('Login!'),
        
#         html.Textarea('Lets see'),
#         html.Div([
#             dcc.Location(id='url', refresh=False),
#             html.Div(id='content'),
#     ])
#     ]
# )


# @callback(
#         [Output('store-data-flow', 'clear_data'),
#         Output('content', 'children')],
#         Input('url', 'href'),
#         State('store-data-flow', 'data'),
#         prevent_initial_call=True)
# def get_url_params(href: str, data: dict):

#     parsed_url = urlparse(href)
#     print(parsed_url.path.split('/'))

#     if parsed_url.path.split('/')[-1] != 'callback':
#         print('callback prevented not in callback page')
#         raise PreventUpdate

#     data_copy = data.copy()

#     print(f'{data_copy=}')


#     param_dict = parse_qs(parsed_url.query)
#     param_dict.update(data_copy)

#     print(f'{param_dict=}')

#     return True, html.P(children=[f"{k}: {v[0]} \n" for k, v in param_dict.items()] )

    # if parsed_url.path.split('/')[-1] != 'callback':
    #     print('callback prevented')
    #     raise PreventUpdate
    
    # param_dict = parse_qs(parsed_url.query)
    # param_dict.update(data)
    # api_url = settings.API_URL
    
    # resp = requests.get(api_url + '/callback', data=param_dict, verify=False)

    # print(f'{resp=}')

    # return html.P(children=[f"{k}: {v[0]} \n" for k, v in param_dict.items()] )


    # {'code': ['0.AagALFNky06yB0GOd4yk_snb9nyobQZfLTRAoBqdRpTMvQPzAPU.AgABBAIAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P9vKq7Qnu9L4Ccz10NprZB6i-fqn67To-yVJBUBQVNmlb4I_10aeO115Kk3P6ZDHc38zCNtvzsC4OIfKf8Ya9zninXWfQnbgx1cNqnHdYp5kVCKp7tYfJD5TcHhZqwl0zsLs9lTvJIu0t4MJGB91j0G3cgD-bqpDDqTFcHfxZoP-8-cN_MI-gE7Dp1b5V_4yjvFZJI5gkkrAARPg2fDs8UD_BVcVHr9FUG6tEwGu6A_Kg5qQSoAM1vNGokHkea_j-iLRg7MKjLAdEAyD-3B36la-LnFod3Hp9SuKK_luCNsLdEiEXa1Abln1NkjzdAQNtlDvJvRBGgLM1Giw0jllxdDq5JgP3I5h3eIdHw93PjRli3Zw2M3zxlU1UrelQQEffHblCeCJ4GsZrXTMryTuWFyz37zApY4-pyRnYTfrQvFVcPJtQCAIb2nHYVnEE0kQPSbYbeOHmRWlbxIRpUukk3XXuAEkolSux3rcPkeB7MiuuFCF8RdX_NT68sJeuv52QE-fFGrkVUeBhkSIkWsl-jt8QRhOyQMmWOJ8U3eabH-c5NLI6uuu3CoDTO0M18YZMX6g9xpfeZEde2mtTDazOYiO5JgCJ0znzPNF61gOxzWo0zZP5_R8yh20z12y6LpbAkUB0Zh6kHufGyRWluvy89wPhwyCWDqb7YtYsNTRZm0y3RED20U-iGDQIoDzhQvpO0Dt9cij8wa9CrwstF7_0hk0v7F0yT52_dbda2MyrIaouhKc2Q9gWGeZ2v2JA6gfv0V2vRX0BfVwAhONECEpD1m_YmUk9XdHcbD90MiT8a7Xr-gZ2NqWK45AIyU4JAIXc5EZuy2hNFerElPVJEO4kL6q7Wyzuqrazl1jS-C8claMG5_TQCKooD6oecSFuuLKbP6XSVqN02ifG9NlspVvsUWA4Qmqan2aZ-vwK3Ty14fjTKw1Zr0Xmk7X6X81hxYzk08V-o_DkOqHXg6NXaN2Bn4NBV5EcQKcDxef1SkFEXNedCHImsK19DX6k-SCvrZKLFuouHO33qnWAoFO4cY_I8mJMBpDRSMlk0-0tY1jUuiGsKkYxgL901MyhAmcqUQ-YJbn-lz8_qBe6iQcV24yAwNa9gsdrkm8HJiiijm-uHxRtPTQ62vFEBkfnmlHwfizJqoCdcSWpsUbsW65OWpvYVq2HdE9YICZ0NeX6SU6ov3mjbnZfIzb2D6IeXnXRpKvSeOtv9cgVTmugxcFjtJh7_46xqiaK_RAfmhjjRmjKWF1_N6zbVQRs-9R1d4nfyV0jTEMiLbMlzNmO2qczSoJzWp9pZ_v8Ph7CfGYwZqA3sTJxqWUxUQCyelDvQ05Uls8PKTqbgqt0oth5YkZOyHE6El2io_Z4yN62n6oa_C333RnZT-fX_X9PrNSQ8FqGfgoHjyMhr94tjJguWeUj6z4EUd9lKLHGxOXIf3WgMuShOjGRxCuA'], 
    #  'client_info': ['eyJ1aWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtNDQ1My05ZjUxYzgzNmU1NWUiLCJ1dGlkIjoiOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkIn0'], 
    #  'state': ['UJcBWCwSlTEAZDuj'], 'session_state': ['f4fb3dc1-9be0-48df-8b0e-2f2cc96bc63e']}
