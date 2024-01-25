from dash import Dash, dcc, html, Input, Output, callback, no_update
from pages.auth import validate_login_session
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash_renderjson
import dash


# @validate_login_session
def get_create_exp_layout():
    return html.Div(
        [
            html.H3("Create new experiments"),
            # dbc.NavItem(
            #     [
            #         dbc.NavLink(
            #             "Exp. Name:",
            #             id="exp_name_tag",
            #             # style={"size": "50px"},
            #             style={"margin-left": "2%", "display": "inline"},
            #         ),
            #         dbc.NavLink(
            #             str(exp_id),
            #             id="exp_name",
            #             # style={"size": "50px"},
            #             style={"margin-left": "2%", "display": "inline"},
            #         ),
            #         dbc.NavLink(
            #             "DUT Name:",
            #             id="dut_name_tag",
            #             # style={"size": "50px"},
            #             style={"margin-left": "5%", "display": "inline"},
            #         ),
            #         dbc.NavLink(
            #             "Lock v0",
            #             id="dut_name",
            #             # style={"size": "50px"},
            #             style={"margin-left": "2%", "display": "inline"},
            #         ),
            #         # ],
            #         #     style={"display": "inline"},
            #         # ),
            #         dbc.NavItem(
            #             [
            #                 dbc.Button(
            #                     "Delete",
            #                     id="delete",
            #                     style={
            #                         "margin-left": "1%",
            #                         # "float": "right",
            #                         # "margin-right": "10%",
            #                     },
            #                 ),
            #                 dbc.Button(
            #                     "Copy",
            #                     id="copy",
            #                     style={
            #                         "margin-left": "1%",
            #                         # "float": "right",
            #                         # "margin-right": "50%",
            #                     },
            #                 ),
            #                 dbc.Button(
            #                     "Save",
            #                     id="save",
            #                     style={
            #                         "margin-left": "1%",
            #                         # "float": "right",
            #                         # "margin-right": "0%",
            #                     },
            #                 ),
            #             ],
            #             # style={"margin-left": "86%"},
            #             style={
            #                 "display": "inline",
            #                 # "float": "right",
            #                 "margin-left": "50%",
            #                 # "margin-left": "auto",
            #                 "margin-right": "2%",
            #             },
            #         ),
            #     ],
            #     # style={"display": "inline"},
            # ),
            dcc.Tabs(
                id="tabs-create-exp",
                value="initial_config_tab",
                children=[
                    dcc.Tab(
                        label="Initial Config", value="initial_config_tab"
                    ),
                    dcc.Tab(
                        label="Generator model Config", value="gen_config_tab"
                    ),
                    dcc.Tab(
                        label="Predictor model Config", value="pred_config_tab"
                    ),
                    dcc.Tab(label="run_experiment", value="run_experiment"),
                ],
            ),
            html.Div(id="tabs-create-exp-content"),
        ]
    )


def get_data():
    return {"a": 1, "b": [1, 2, 3, {"c": 4}]}


@callback(
    Output("tabs-create-exp-content", "children"),
    Input("tabs-create-exp", "value"),
)
def render_content(tab):
    if tab == "initial_config_tab":
        return html.Div(
            [
                html.H3(
                    "Please fill the below details to start the experiment"
                ),
                dbc.Row(
                    [
                        dbc.Label(
                            "Experiment Name", html_for="exp_name", width=2
                        ),
                        dbc.Col(
                            dbc.Input(
                                type="text",
                                id="exp_name",
                                placeholder="Enter Experiment Name",
                            ),
                            width=10,
                        ),
                    ],
                    className="mb-3",
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Label(
                            "Use preditor model?",
                            html_for="example-radios-row",
                            width=2,
                        ),
                        dbc.Col(
                            dbc.RadioItems(
                                id="example-radios-row",
                                options=[
                                    {"label": "Yes", "value": 1},
                                    {"label": "No", "value": 2},
                                ],
                            ),
                            width=10,
                        ),
                    ],
                    className="mb-3",
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Label(
                            "Select Generative Model", html_for="dropdown"
                        ),
                        dcc.Dropdown(
                            id="dropdown",
                            options=[
                                {"label": "Option 1", "value": 1},
                                {"label": "Option 2", "value": 2},
                            ],
                        ),
                    ],
                    className="mb-3",
                ),
                html.Br(),
                html.Div(
                    [
                        dbc.Label("Slider", html_for="slider"),
                        dcc.Slider(
                            id="slider", min=0, max=10, step=0.5, value=3
                        ),
                    ],
                    className="mb-3",
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


# @callback(
#     dash.dependencies.Output("tabs-create-exp", "active_tab"),
#     [
#         dash.dependencies.Input("submit", "n_clicks"),
#     ],
# )
# def on_click_val(click1):
#     btn = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
#     if btn == "submit":
#         return "gen_config_tab"
#     else:
#         return no_update
