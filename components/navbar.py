# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc


# Define the navbar structure
def Navbar():
    layout = html.Div(
        [
            dbc.Navbar(
                [
                    html.A(
                        [
                            html.Img(
                                src=r"assets/Micron-logo.png",
                                alt="image",
                                sizes="0.1",
                                height="10%",
                                width="25%",
                            )
                        ],
                        href="experiment_history",
                        style={"height": "5%"},
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
