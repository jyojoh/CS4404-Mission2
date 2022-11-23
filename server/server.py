from flask import Flask, session, render_template, request, redirect
from flask_session import Session
import database as init
import library as db

init.initDatabase()

app = Flask(__name__)
app.secret_key = "twofaserver"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        username = str(request.values.get("user"))
        password = str(request.values.get("pass"))

        if not db.checkUser(username, password):
            return render_template("loginfail.html")

        return render_template("twofactor.html")


    return render_template("login.html", **data)


if __name__ == '__main__':
    app.run("0.0.0.0", 80)
