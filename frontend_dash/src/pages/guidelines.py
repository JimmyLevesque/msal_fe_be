import dash
from dash import html, callback, Input, Output, State

dash.register_page(
    __name__,
    path='/guidelines',
    title='Guidelines'
)

layout = html.Div(
    [
        html.H1('Guidelines!'),
        
        html.Textarea('Use this app correctly'),

        html.Button('Click to get data', 
                    id='btn-get-data', 
                    n_clicks=0,
                    style={'width': '200px',
                           'margin-bottom': '10px',
                           'margin-left': '10px',}), 
        html.Br(),
        html.Br(),
        html.Div(id='get-data-div', children=html.H3('Button not clicked'))
    ]
)



@callback(
    Output('get-data-div', 'children'),
    Input('btn-get-data', 'n_clicks'), 
    State('store-data-flow', 'data'),
    prevent_initial_call=True
)
def login_btn(n_clicks, data):
    print('*'*100)
    print('clicked to get data')
    print(f'{data=}')

    return html.H3(data)