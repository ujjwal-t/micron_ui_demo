# package imports
import dash_bootstrap_components as dbc
from dash import dcc, html, no_update
from dash.dependencies import Input, Output, State
from flask import session

# local imports
from auth import authenticate_user, validate_login_session
from server import app


def Navbar():
    layout = html.Div(
        [
            dbc.Navbar(
                [
                    html.A(
                        [
                            html.Img(
                                src=r"Micron-logo.png",
                                alt="image",
                                sizes="0.1",
                                height="10%",
                                width="25%",
                            )
                        ],
                        href="experiment_history",
                        style={"height": "5%"},
                    ),
                    # html.Span(
                    #     [
                    #         dbc.NavItem(
                    #             dbc.NavLink(
                    #                 "User1",
                    #             ),
                    #             style={"margin-right": "2%"},
                    #         ),
                    #         dbc.NavItem(
                    #             dbc.NavLink("Logout", href="login_page"),
                    #         ),
                    #     ],
                    #     style={
                    #         "font-size": "1.5rem",
                    #         "width": "100%",
                    #         "display": "flex",
                    #         "align-items": "right",
                    #         "justify-content": "right",
                    #         "vertical-align": "super",
                    #         "margin-right": "2%",
                    #     },
                    # ),
                ],
                color="lightblue",
            )
        ]
    )

    return layout


nav = Navbar()


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


# home layout content
@validate_login_session
def app_layout():
    return html.Div(
        [
            dcc.Location(id="home-url", pathname="/home"),
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            [html.H2("Home page.")],
                        ),
                        justify="center",
                    ),
                    html.Br(),
                    dbc.Row(
                        dbc.Col(
                            dbc.Button(
                                "Logout",
                                id="logout-button",
                                color="danger",
                                size="sm",
                            ),
                            width=4,
                        ),
                        justify="center",
                    ),
                    html.Br(),
                ],
            ),
        ]
    )


# main app layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        nav,
        html.Div(login_layout(), id="page-content"),
    ]
)


###############################################################################
# utilities
###############################################################################


# router
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def router(url):
    if url == "/home":
        return app_layout()
    elif url == "/login":
        return login_layout()
    else:
        return login_layout()


# authenticate
@app.callback(
    [Output("url", "pathname"), Output("login-alert", "children")],
    [Input("login-button", "n_clicks")],
    [State("login-email", "value"), State("login-password", "value")],
)
def login_auth(n_clicks, email, pw):
    """
    check credentials
    if correct, authenticate the session
    otherwise, authenticate the session and send user to login
    """
    if n_clicks is None or n_clicks == 0:
        return no_update, no_update
    credentials = {"user": email, "password": pw}
    if authenticate_user(credentials):
        print(session)
        session["authed"] = True
        return "/home", ""
    session["authed"] = False
    return no_update, dbc.Alert(
        "Incorrect credentials.", color="danger", dismissable=True
    )


@app.callback(
    Output("home-url", "pathname"), [Input("logout-button", "n_clicks")]
)
def logout_(n_clicks):
    """clear the session and send user to login"""
    if n_clicks is None or n_clicks == 0:
        return no_update
    session["authed"] = False
    return "/login"


###############################################################################
# callbacks
###############################################################################

# @app.callback(
#     Output('...'),
#     [Input('...')]
# )
# def func(...):
#     ...

###############################################################################
# run app
###############################################################################

if __name__ == "__main__":
    app.run_server(debug=True, port=8082)
