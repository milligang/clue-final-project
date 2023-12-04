from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///clue.db")

#TODO: create sql tables

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return render_template("mycards.html")
    else:
        return render_template("homepage.html")
    '''both players press start when ready
            generate cards for the players
                assign user id to each card
                assign id to winning card set
            redirect to game board'''

@app.route("/gameboard", methods=["GET", "POST"])
def gameboard():
    if request.method == "POST":
        room = request.form.get("room")
        # error if the user does not a room, redirect user to gameboard to select a room
        if not room:
            return render_template("gameboard.html")
        # if the location is harvard hall, the user is submitting their final guess to end the game
        elif room == "Harvard Hall":
            return render_template("harvard.html")
        # else, this is a typical turn and so proceed to page where the user can enter their guess
        else:
            flash(room)
            return render_template("guess.html")

    else:
        return render_template("gameboard.html")

@app.route("/guess", methods=["GET", "POST"])
def guess():
    if request.method == "POST":
        weapon = request.form.get("weapon")
        person = request.form.get("person")
        # error if the player does not select a weapon and a person
        if not weapon or not person:
            #TODO (probs don't actually want to go back to the homepage)
            return render_template("homepage.html")

        return render_template("guess.html")
    else:
        return render_template("guess.html")
    """
    post =

    get = render.template(the page where the player can select the suspect, room, and weapon)
    """

@app.route("/revealcards", methods=["GET", "POST"])
def revealcards():
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

@app.route("/mycards")
def mycards():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("mycards.html")
    """
    cards = select * from cards where player_id = ?, current_player
    render.template(page of player's cards, cards = cards)
    """

@app.route("/allcards")
def allcards():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("allcards.html")
    """
    cards = select * from cards where player_id = ?, current_player
    render.template(page of player's cards, cards = cards)
    """

@app.route("/finalguess")
def finalguess():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("harvard.html")
