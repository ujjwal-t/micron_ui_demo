import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from dash_table import DataTable, FormatTemplate
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "label: " + id, "value": id}
                for id in ["b", "c", "d", "e", "f"]
            ],
        ),
        DataTable(
            id="table",
            columns=[{"name": x, "id": x, "selectable": True} for x in ["a"]],
            column_selectable="single",
            data=[
                {
                    "a": "a" + str(x),
                    "b": "b" + str(x),
                    "c": "c" + str(x),
                    "d": "d" + str(x),
                    "e": "e" + str(x),
                    "f": "f" + str(x),
                }
                for x in range(0, 100)
            ],
        ),
    ]
)


@app.callback(
    Output("table", "columns"),
    [Input("dropdown", "value")],
    [State("table", "columns")],
)
def update_columns(value, columns):
    if value is None or columns is None:
        raise PreventUpdate

    inColumns = any(c.get("id") == value for c in columns)

    if inColumns == True:
        raise PreventUpdate

    columns.append({"label": "label: " + value, "id": value})
    return columns


if __name__ == "__main__":
    app.run_server(debug=False, port=8051)
