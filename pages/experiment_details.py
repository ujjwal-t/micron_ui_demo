from dash import Dash, dcc, html, Input, Output, callback
from pages.auth import validate_login_session
import dash_bootstrap_components as dbc


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
                            "margin-left": "55%",
                            # "margin-left": "auto",
                            "margin-right": "2%",
                        },
                    ),
                ],
                # style={"display": "inline"},
            ),
            dcc.Tabs(
                id="tabs-example-graph",
                value="tab-1-example-graph",
                children=[
                    dcc.Tab(label="Summary", value="summary_tab"),
                    dcc.Tab(label="Config", value="config_tab"),
                    dcc.Tab(
                        label="Warm up training",
                        value="warm_up_training_tab",
                    ),
                    dcc.Tab(label="Fine tuning", value="fine_tuning_tab"),
                    dcc.Tab(label="Results", value="result_tab"),
                ],
            ),
            html.Div(id="tabs-content-example-graph"),
        ]
    )


@callback(
    Output("tabs-content-example-graph", "children"),
    Input("tabs-example-graph", "value"),
)
def render_content(tab):
    if tab == "tab-1-example-graph":
        return html.Div(
            [
                html.H3("Tab content 1"),
                dcc.Graph(
                    figure={
                        "data": [
                            {"x": [1, 2, 3], "y": [3, 1, 2], "type": "bar"}
                        ]
                    }
                ),
            ]
        )
    elif tab == "tab-2-example-graph":
        return html.Div(
            [
                html.H3("Tab content 2"),
                dcc.Graph(
                    id="graph-2-tabs-dcc",
                    figure={
                        "data": [
                            {"x": [1, 2, 3], "y": [5, 10, 6], "type": "bar"}
                        ]
                    },
                ),
            ]
        )
