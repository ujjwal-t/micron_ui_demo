from dash import Dash, dcc, html, Input, Output, callback
from pages.auth import validate_login_session
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash_renderjson


# @validate_login_session
def get_exp_details_layout(exp_id):
    return html.Div(
        [
            html.H3("Details experiments page"),
            dbc.NavItem(
                [
                    dbc.NavLink(
                        "Exp. Name:",
                        id="exp_name_tag",
                        # style={"size": "50px"},
                        style={"margin-left": "2%", "display": "inline"},
                    ),
                    dbc.NavLink(
                        str(exp_id),
                        id="exp_name",
                        # style={"size": "50px"},
                        style={"margin-left": "2%", "display": "inline"},
                    ),
                    dbc.NavLink(
                        "DUT Name:",
                        id="dut_name_tag",
                        # style={"size": "50px"},
                        style={"margin-left": "5%", "display": "inline"},
                    ),
                    dbc.NavLink(
                        "Lock v0",
                        id="dut_name",
                        # style={"size": "50px"},
                        style={"margin-left": "2%", "display": "inline"},
                    ),
                    # ],
                    #     style={"display": "inline"},
                    # ),
                    dbc.NavItem(
                        [
                            dbc.Button(
                                "Delete",
                                id="delete",
                                style={
                                    "margin-left": "1%",
                                    # "float": "right",
                                    # "margin-right": "10%",
                                },
                            ),
                            dbc.Button(
                                "Copy",
                                id="copy",
                                style={
                                    "margin-left": "1%",
                                    # "float": "right",
                                    # "margin-right": "50%",
                                },
                            ),
                            dbc.Button(
                                "Save",
                                id="save",
                                style={
                                    "margin-left": "1%",
                                    # "float": "right",
                                    # "margin-right": "0%",
                                },
                            ),
                        ],
                        # style={"margin-left": "86%"},
                        style={
                            "display": "inline",
                            # "float": "right",
                            "margin-left": "50%",
                            # "margin-left": "auto",
                            "margin-right": "2%",
                        },
                    ),
                ],
                # style={"display": "inline"},
            ),
            dcc.Tabs(
                id="tabs",
                value="summary_tab",
                children=[
                    dcc.Tab(label="Summary", value="summary_tab"),
                    dcc.Tab(label="Config", value="config_tab"),
                    dcc.Tab(
                        label="Warm up training",
                        value="warm_up_training_tab",
                    ),
                    dcc.Tab(label="Fine tuning", value="fine_tuning_tab"),
                    dcc.Tab(label="Results", value="results_tab"),
                ],
            ),
            html.Div(id="tabs-content"),
        ]
    )


def get_data():
    return {"a": 1, "b": [1, 2, 3, {"c": 4}]}


@callback(
    Output("tabs-content", "children"),
    Input("tabs", "value"),
)
def render_content(tab):
    if (tab == "summary_tab") or (tab == "results_tab"):
        heading = "Summary" if (tab == "summary_tab") else "Results"
        return html.Div(
            [
                html.H3(heading),
                dcc.Graph(
                    figure={
                        "data": [
                            {
                                "x": [i for i in range(10)],
                                "y": [
                                    0,
                                    20,
                                    25,
                                    50,
                                    90,
                                    91,
                                    92,
                                    93,
                                    94,
                                    95,
                                    96,
                                    97,
                                    98,
                                    99,
                                ],
                                "type": "scatter",
                                "name": "SF",
                            },
                        ],
                        "layout": {
                            "title": "Test case vs coverage plot",
                            "ytitle": "Coverage",
                            "x": "test_case",
                        },
                    }
                ),
            ]
        )
    elif tab == "config_tab":
        return html.Div(
            [
                html.Br(),
                html.H3("config"),
                html.Br(),
                dash_renderjson.DashRenderjson(
                    id="input",
                    data=get_data(),
                    max_depth=-1,
                    invert_theme=True,
                ),
            ],
            style={"margin-left": "5%"},
        )
