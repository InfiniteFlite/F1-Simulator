from flask import Flask, url_for, render_template, request, session, redirect

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/simsetup")
def render_setup():
    return render_template("setup.html")

if __name__=="__main__":
    app.run(debug=True)
