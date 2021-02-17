import sys
import json
import time

from app             import app, models, utilities, db, AccountManager, AppSettingsHandler, generate, socketio, emit, send #, login
from app.generate    import generate_transactions_as_dict
from flask           import render_template, request, redirect, url_for
from flask_login     import LoginManager, login_required, login_user, logout_user, current_user

#login.login_view = "loginPage"

def confirm_msg():
    print("Message was received!")

@app.route("/")
def homePage():
    return "Home"

@app.route("/mine")
def blockPage():
    transactions = generate_transactions_as_dict(10)
    return render_template("tiddy-mine.html", transactions=transactions, version="1.0")

@app.route("/test")
def test():
    return "test"

@socketio.on("connect")
def connection_test():
    send("Connection established.")

@socketio.on("Disconnect")
def client_disconnect():
    pass