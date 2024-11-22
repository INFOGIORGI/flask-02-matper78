from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run()