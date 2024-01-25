# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc
import base64
from flask import request
from dash import dcc, html, no_update, callback
from dash.dependencies import Input, Output, State
import time


# Define the navbar structure
def Navbar():
    logo_png = r"assets/Micron-logo.png"
    logo_base64 = base64.b64encode(open(logo_png, "rb").read()).decode("ascii")
    exp_page_url = "/experiment_history"
    layout = html.Div(
        [
            dbc.Navbar(
                [
                    html.A(
                        [
                            html.Img(
                                src="data:image/png;base64,{}".format(
                                    logo_base64
                                ),
                                alt="image",
                                sizes="0.1",
                                height="10%",
                                width="25%",
                            )
                        ],
                        # value=exp_page_url,
                        style={"height": "5%"},
                        id="logo-tag",
                    ),
                    dbc.NavItem(
                        [
                            dbc.NavLink(
                                "User",
                                id="user_name",
                                style={"margin-right": "2%"},
                            ),
                            dbc.NavLink(
                                "login",
                                id="user_action",
                                href="login",
                                style={
                                    "margin-right": "2%",
                                    "color": "7",
                                },
                            ),
                        ],
                        style={
                            "font-size": "1.5rem",
                            "width": "100%",
                            "display": "flex",
                            "align-items": "right",
                            "justify-content": "right",
                            "vertical-align": "super",
                            "margin-right": "2%",
                        },
                    ),
                ],
                color="lightblue",
            )
        ]
    )

    return layout


@callback(
    Output("url", "href", allow_duplicate=True),
    [Input("logo-tag", "n_clicks_timestamp")],
    prevent_initial_call=True,
)
def render_content(n_clicks_timestamp):
    print(
        (n_clicks_timestamp is not None)
        and (abs(n_clicks_timestamp / 10**3 - time.time()))
    )
    if (n_clicks_timestamp is not None) and (
        abs(n_clicks_timestamp / 10**3 - time.time()) < 5000
    ):
        return "/experiment_history"
    return no_update
