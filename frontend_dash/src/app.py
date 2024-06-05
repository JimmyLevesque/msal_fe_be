
# package imports
from dash import Dash, page_container, html, dcc
import dash_bootstrap_components as dbc

# local imports
from components import footer, navbar

app = Dash(
    __name__,
    use_pages=True,    # turn on Dash pages
    external_stylesheets=[
        dbc.themes.CERULEAN,
        dbc.icons.FONT_AWESOME
    ],  # fetch the proper css items we want
    suppress_callback_exceptions=True,
    title='Dash app'
)


def serve_layout():
    '''Define the layout of the application'''
    return html.Div(
        [
            navbar,
            dbc.Container(
                page_container,
                class_name='random name'
            ),

            footer,

            dcc.Store(id='store-data-flow', 
                    data=[], 
                    storage_type='session', clear_data=True), # 'memory', 'local' or 'session'

            dcc.Store(id='store-data-token', 
                    data=[], 
                    storage_type='session'), # 'memory', 'local' or 'session'
        ]
    )


app.layout = serve_layout   # set the layout to the serve_layout function


if __name__ == "__main__":
    app.run(debug=True)

