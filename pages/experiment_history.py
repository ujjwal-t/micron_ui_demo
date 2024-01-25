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
        lambda x: f"[{x}](http://127.0.0.1:8050/experiment_details/{'20_'+x})"
    )
    return df


# Define the page layout
@validate_login_session
def get_exp_page_layout():
    df = get_data_from_db()
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    html.Center(html.H1("List of historical experiments")),
                    html.Br(),
                    html.H4("Select columns to add from the below dropdown"),
                    dcc.Dropdown(
                        id="dropdown",
                        options=[
                            {"label": id, "value": id} for id in df.columns
                        ],
                    ),
                    html.Hr(),
                    html.Div(
                        [
                            dash_table.DataTable(
                                id="table",
                                data=df.to_dict("records"),
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
    return layout


@callback(
    Output("table", "columns"),
    [Input("dropdown", "value")],
    [State("table", "columns")],
)
def update_columns(value, columns):
    if value is None or columns is None:
        return no_update

    inColumns = any(c.get("id") == value for c in columns)

    if inColumns:
        return no_update

    columns.append(
        {
            "name": value,
            "id": value,
            "deletable": True,
        }
    )
    return columns
