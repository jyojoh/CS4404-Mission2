from flask import Flask, session, render_template, request, redirect
from flask_session import Session
import database as init
import library as db
import random
import string

init.initDatabase()

app = Flask(__name__)
app.secret_key = "twofaserver"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

twoFactorCode = None

@app.get("/")
def index_get():
    return render_template("login.html")

@app.post("/login")
def index_post():
    global twoFactorCode
    username = str(request.values.get("user"))
    password = str(request.values.get("pass"))

    if not db.checkUser(username, password):
        return render_template("loginfail.html")

    #Generate 2fa code, send to phone, and prompt for code
    twoFactorCode = "".join(random.choices(string.digits, k=6))
    ### Send twoFactorCode to phone here ###
    print("Generated 2FA code: " + twoFactorCode + " for user " + username)
    return render_template("twofactor.html")

@app.post("/twofactor")
def twofactor_post():
    global twoFactorCode
    #Check if code matches generated 2fa code
    code = str(request.values.get("code"))
    if code == twoFactorCode:
        return render_template("success.html")
    else:
        print("Recieved code " + code + " expected code " + twoFactorCode)
        return render_template("twofactorfail.html")

if __name__ == '__main__':
    app.run("0.0.0.0", 80)
