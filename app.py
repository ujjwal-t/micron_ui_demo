# Define the Dash App and it's properties here

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    suppress_callback_exceptions=True,
)
app.title = "MICRON"
server = app.server
server.config["SECRET_KEY"] = "k1LUZ1fZShowB6opoyUIEJkJvS8RBF6MMgmNcDGNmgGYr"
