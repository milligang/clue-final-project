from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
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

# Notes from creating sql table
"""
CREATE TABLE cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    player_id INTEGER,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    path VARCHAR(255)
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

    # forget any player_ids
    session.clear()

    if request.method == "POST":
        # assign cards to players, and create a player 0 to store the winning cards
        db.execute("UPDATE cards SET player_id = NULL")
        for type in ["Weapon", "Place", "Person"]:
            db.execute("UPDATE cards SET player_id = 0 WHERE id IN (SELECT id FROM cards WHERE type = ? ORDER BY RANDOM() LIMIT 1)", type)
        for i in range(1, N+1):
            db.execute("UPDATE cards SET player_id = ? WHERE id IN (SELECT id FROM cards WHERE player_id = NULL ORDER BY RANDOM() LIMIT ?)",
            i,
            (C - 3)/N
            )

        # it is player 1's turn
        session["current_player"] = 1
        return redirect("/mycards")

    else:
        return render_template("homepage.html")

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
            return redirect("/guess")

    else:
        return render_template("gameboard2.html")

@app.route("/guess", methods=["GET", "POST"])
def guess():
    if request.method == "POST":
        # store what the player inputted as their guess
        weapon = request.form.get("weapon")
        person = request.form.get("person")
        place = request.form.get("place")

        # error if the player does not select a weapon and a person
        if not weapon or not person:
            #TODO (probs don't actually want to go back to the gameboard)
            return render_template("gameboard.html")

        # go to the next player so they can select which card to reveal
        session["current_player"] += 1
        if session["current_player"] > N:
            session["current_player"] = 1

        # select all cards that the first player guessed and that the second player has
        session["player_cards"] = ("SELECT * FROM cards WHERE player_id = ? AND id IN (SELECT id FROM cards WHERE name = ? OR name = ? OR name = ?)",
                         session["current_player"],
                         weapon,
                         person,
                         place
                         )
        # if there are no cards in common, mention this
        if not session["player_cards"]:
            session["player_cards"] = {"id": 0, "}

        return redirect("/revealcards")

    else:
        weapons = db.execute("SELECT * FROM cards WHERE type = 'Weapon'")
        people = db.execute("SELECT * FROM cards WHERE type = 'Person'")
        return render_template("guess.html", weapons = weapons, people = people)

@app.route("/revealcards", methods=["GET", "POST"])
def revealcards():
    if request.method == "POST":
        card = request.form.get("card")
        if not card:
            # TODO: error if the user did not select a card to reveal
            return render_template("homepage.html")

        # TODO: need to tell the original player the card that was selected
        return redirect("/mycards")
    else:
        return render_template("reveal.html", player_cards = session["player_cards"])

@app.route("/mycards", methods=["GET", "POST"])
def mycards():
    if request.method == "POST":
        return redirect("/gameboard2")
    else:
        return render_template("mycards.html", cards = db.execute("SELECT * FROM cards"), current_player = session["current_player"])

@app.route("/allcards")
def allcards():
    return render_template("allcards.html", cards = db.execute("SELECT * FROM cards"))

@app.route("/finalguess")
def finalguess():
    if request.method == "POST":
        return redirect("/homepage")
    else:
        return render_template("harvard.html")
