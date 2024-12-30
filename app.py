import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, jsonify, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helper import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///tracker.db")

# ensures the user gets the latest version (not outdated)
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return redirect("/login")



@app.route("/add_task", methods=["POST"])
@login_required
def add_task():
    task_name = request.form.get("task_name")
    task_type = request.form.get("task_type")  # Indicates if it's a daily or weekly task

    print("Task Name:", task_name)
    print("Task Type:", task_type)

    if task_name and task_type in ['daily', 'weekly']:

        db.execute("INSERT INTO tasks (user_id, task, completed, task_type) VALUES (:user_id, :task_name, 0, :task_type)",
                   user_id=session["user_id"], task_name=task_name, task_type=task_type)
        # Redirect to /tracker after task is added
        return redirect("/tracker")

    return redirect("/tracker")


@app.route("/delete_task/<int:task_id>")
@login_required
def delete_task(task_id):
    # Delete the task with the given task_id
    db.execute("DELETE FROM tasks WHERE id = :task_id AND user_id = :user_id", task_id=task_id, user_id=session["user_id"])

    # After deletion, redirect to /tracker
    return redirect("/tracker")




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username", "error")
            return redirect("/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password", "error")
            return redirect("/login")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("invalid username and/or password", "error")
            return redirect("/login")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/tracker")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/tracker")
@login_required
def tracker():
    tasks = db.execute("SELECT id, task, task_type FROM tasks WHERE user_id = :user_id", user_id=session["user_id"])

    return render_template("tracker.html", tasks=tasks)





@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
# ensures username
        if not request.form.get("username"):
            flash("Must Enter Username", "error")
            return redirect("/register")
# ensures password
        elif not request.form.get("password"):
            flash("Must Enter password", "error")
            return redirect("/register")
# ensures passowrd confirmation
        elif not request.form.get("confirmation"):
            flash("must confirm password", "error")
            return redirect("/register")
# checks if password matches confirmation
        elif request.form.get("password") != request.form.get("confirmation"):
            flash("password dont match", "error")
            return redirect("/register")
# Query db for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
# ensures username doesnt exist
        if len(rows) != 0:
            flash("Username already exists", "error")
            return redirect("/register")
#insert new user into db
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), generate_password_hash(request.form.get("password")))
# quesry db for new user
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
# remember wich user logged in
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    else:
        return render_template("register.html")



