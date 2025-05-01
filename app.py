# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/vision")
def vision():
    return render_template("vision.html")

@app.route("/vegetables")
def vegetables():
    return render_template("vegetables.html")

@app.route("/fruits")
def fruits():
    return render_template("fruits.html")

@app.route("/maps")
def maps():
    return render_template("maps.html")

@app.route("/accreditations")
def accreditations():
    return render_template("accreditations.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
