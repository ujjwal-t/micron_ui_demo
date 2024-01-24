# Import necessary libraries
from dash import Dash, dash_table, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dcc, html, no_update
import pandas as pd
from pages.auth import validate_login_session


def get_data_from_db():
    df = pd.DataFrame(
        {
            "dut_name": "lock_v0",
            "created_by": "user1",
            "creation_date": "2024-01-01",
            "description": "Modified this in the this model and run for this exeperiment",
            "status": "running",
            "coverage": "55%",
            "generative_model_id": "v0.1",
            "predictive_model_id": "v0.1",
        }
        for j in range(8)
    )
    df1 = df.copy()
    df1["created_by"] = "user2"
    df1["creation_date"] = "2024-01-12"
    df1["status"] = "completed"
    df1["generative_model_id"] = "v0.2"
    df1["predictive_model_id"] = "v0.2"
    df1["description"] = df1["description"].apply(lambda x: "By user2 " + x)
    df = pd.concat([df, df1], axis=0)
    df["dut_name"] = df["dut_name"].apply(
        lambda x: f"[{x}](http://127.0.0.1:8050/experiment_details?exp_id={x+'20'})"
    )
    return df.to_dict("records")


# Define the page layout
@validate_login_session
def get_exp_page_layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    html.Center(html.H1("List of historical experiments")),
                    html.Br(),
                    html.Hr(),
                    html.Div(
                        [
                            dash_table.DataTable(
                                id="editing-prune-data",
                                data=get_data_from_db(),
                                editable=False,
                                filter_action="native",
                                page_action="native",
                                page_current=0,
                                page_size=10,
                                sort_action="native",
                                sort_mode="multi",
                                css=[
                                    {
                                        "selector": ".Select-menu-outer",
                                        "rule": "display: block !important",
                                    }
                                ],
                                columns=[
                                    {
                                        "name": "DUT Name",
                                        "id": "dut_name",
                                        "presentation": "markdown",
                                    },
                                    {
                                        "name": "Created By",
                                        "id": "created_by",
                                    },
                                    {
                                        "name": "Creation Date",
                                        "id": "creation_date",
                                    },
                                    {
                                        "name": "Description",
                                        "id": "description",
                                    },
                                    {
                                        "name": "Status",
                                        "id": "status",
                                    },
                                    {
                                        "name": "Coverage",
                                        "id": "coverage",
                                    },
                                ],
                                style_data={
                                    "white-space": "normal",
                                    "color": "black !important",
                                },
                            ),
                        ],
                    ),
                ]
            )
        ]
    )
