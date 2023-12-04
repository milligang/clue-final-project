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

N = 2 # the number of players
C = 15 # the number of cards
current_player = 1

#TODO: create sql tables
# create table cards (...)
# potential rows: player_id (unique), type, name
"""
CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    player_id INTEGER,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
);
"""

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
            redirect to game board

            for random column:
            SELECT column FROM table
            ORDER BY RAND ( )
            LIMIT 1
            '''
    '''
    UPDATE cards SET player_id = NULL
    UPDATE cards SET player_id = 0 WHERE id IN (SELECT id FROM cards ORDER BY RAND() LIMIT 3)
    for i in range(1, N+1):
        db.execute("UPDATE cards SET player_id = ? WHERE id IN (SELECT id FROM cards ORDER BY RAND() LIMIT ? WHERE player_id = NULL",
        i,
        (C - 3)/N
        )
    '''

@app.route("/gameboard2", methods=["GET", "POST"])
def gameboard2():
    if request.method == "POST":
        room = request.form.get("room")
        # error if the user does not a room, redirect user to gameboard to select a room
        if not room:
            return render_template("gameboard2.html")
        # if the location is harvard hall, the user is submitting their final guess to end the game
        elif room == "Harvard Hall":
            return render_template("harvard.html")
        # else, this is a typical turn and so proceed to page where the user can enter their guess
        else:
            flash(room)
            return render_template("guess.html")

    else:
        return render_template("gameboard2.html")

@app.route("/guess", methods=["GET", "POST"])
def guess():
    if request.method == "POST":
        weapon = request.form.get("weapon")
        person = request.form.get("person")
        # error if the player does not select a weapon and a person
        if not weapon or not person:
            #TODO (probs don't actually want to go back to the gameboard)
            return render_template("gameboard.html")

        # go to the next player so they can select which card to reveal
        current_player += 1
        if current_player > N:
            current_player = 1
        return render_template("homepage.html")
    else:
        return render_template("guess.html")

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
        cards = db.execute("SELECT * FROM cards WHERE player_id = ?", current_player)
        return render_template("mycards.html", cards = cards)
    """

@app.route("/allcards")
def allcards():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("allcards.html")

@app.route("/finalguess")
def finalguess():
    if request.method == "POST":
        return render_template("homepage.html")
    else:
        return render_template("harvard.html")
