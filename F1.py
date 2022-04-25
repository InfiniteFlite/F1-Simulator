from flask import Flask, url_for, render_template, request, session, redirect
import math
import random

app = Flask(__name__)

constructors = ["RedBull", "Ferrari", "Mercedes", "Mclaren", "Haas", "Alpha Tauri", "Alfa Romeo", "Alpine", "Aston Martin", "Williams"]

def randomize_constructors_for_form():
    random.shuffle(constructors)
    options = ""
    for c in constructors:
        options+= c + ", "
    return options

@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/simsetup")
def render_setup():
    c = randomize_constructors_for_form()
    return render_template("setup.html", constructorListValues = c)

@app.route("/sim")
def render_sim():
    return render_template("sim.html")

if __name__=="__main__":
    app.run(debug=True)
