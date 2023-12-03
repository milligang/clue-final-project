from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# TODO - need to make the .db first

#TODO: create sql tables

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return render_template("homepage.html")
    '''both players press start when ready
        generate cards for the players
            assign user id to each card
            assign id to winning card set
        redirect to game board'''

    else:
        return render_template("homepage.html")

@app.route("/game_board", methods=["GET", "POST"])
def game_board():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("gameboard.html")
    """
    post = player clicks on one of the locations
        flash the location (so that the next page can use it as input)
        redirect(page where player inputs their guess)

    else:
        return render_template("game_board.html")
    """

@app.route("/guess", methods=["GET", "POST"])
def guess():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("guess.html")
    """
    post =

    get = render.template(the page where the player can select the suspect, room, and weapon)
    """

@app.route("/reveal_cards", methods=["GET", "POST"])
def reveal_cards():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("homepage.html")
    """
    post = player selects card from the dropdown and clicks submit
        card = request.form.get(the item selected from the dropdown)
        redirect(page that tells first player the card, take card as input)

    get = render.template(the page where the player chooses which card to show)
    """

@app.route("/show_cards")
def show_cards():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("mycards.html")
    """
    cards = select * from cards where player_id = ?, current_player
    render.template(page of player's cards, cards = cards)
    """

@app.route("/all_cards")
def all_cards():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("allcards.html")
    """
    cards = select * from cards where player_id = ?, current_player
    render.template(page of player's cards, cards = cards)
    """
