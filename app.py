from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
# TODO - do we want cookies or no?

# Configure CS50 Library to use SQLite database
# TODO

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/start", methods=["GET", "POST"])
def start():
    """
    post = both players press start when ready
        generate cards for the players
            assign user id to each card
            assign id to winning card
            
    get = render.template(whatever the home page is called)
    """
