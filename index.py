# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash import dcc, html, no_update
from flask import session
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app

# Connect the navbar to the index
from components import login, navbar
from pages.auth import authenticate_user, validate_login_session
from pages.experiment_history import get_exp_page_layout

# define the navbar

nav = navbar.Navbar()
login_page = login.login_layout()

# Define the index page layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        nav,
        html.Div(login_page, id="page-content"),
    ]
)


# URL paths
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        print("session: ", session)
        if ("authed" not in session.keys()) or (session["authed"] is False):
            return login_page
        else:
            return get_exp_page_layout()
    elif pathname == "/login":
        return login_page
    elif pathname == "/experiment_history":
        return get_exp_page_layout()
    else:
        return "404 Page Error! Please choose a link"


# Login
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
        session["authed"] = True
        session["username"] = email
        return "/experiment_history", ""
    session["authed"] = False
    return no_update, dbc.Alert(
        "Incorrect credentials.", color="danger", dismissable=True
    )


# Login / Logout button
@app.callback(
    [
        Output("user_action", "children"),
        Output("user_action", "href"),
        Output("user_name", "children"),
    ],
    [Input("page-content", "children")],
)
def user_logout(input1):
    print("user_logout: ", session)
    if ("authed" not in session.keys()) or (not session["authed"]):
        print("logout")
        return "login", "/login", "User"
    else:
        session["authed"] = False
        return "logout", "/login", session["username"]


# Run the app on localhost:8050
if __name__ == "__main__":
    app.run_server(debug=True)
