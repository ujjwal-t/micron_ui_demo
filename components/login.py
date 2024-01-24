import dash_bootstrap_components as dbc
from dash import dcc, html


# login layout content
def login_layout():
    return html.Div(
        [
            dcc.Location(id="login-url", pathname="/login", refresh=False),
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            dbc.Card(
                                [
                                    html.H4("Login", className="card-title"),
                                    dbc.Input(
                                        id="login-email", placeholder="User"
                                    ),
                                    dbc.Input(
                                        id="login-password",
                                        placeholder="Assigned password",
                                        type="password",
                                    ),
                                    dbc.Button(
                                        "Submit",
                                        id="login-button",
                                        color="success",
                                    ),
                                    html.Br(),
                                    html.Div(id="login-alert"),
                                ],
                                body=True,
                            ),
                            width=6,
                        ),
                        justify="center",
                    )
                ]
            ),
        ]
    )
