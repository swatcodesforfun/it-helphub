from flask import Flask, render_template, request
from tools.password_generator import generate_password


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")



@app.route("/tools")
def tools():

    return render_template("tools.html")



@app.route("/troubleshooting")
def troubleshooting():

    return render_template("troubleshooting.html")



@app.route("/learn")
def learn():

    return render_template("learn.html")

@app.route("/password-generator", methods=["GET", "POST"])
def password_generator():

    password = None

    if request.method == "POST":

        length = int(request.form["length"])

        uppercase = "uppercase" in request.form
        numbers = "numbers" in request.form
        symbols = "symbols" in request.form

        password = generate_password(
            length,
            uppercase,
            numbers,
            symbols
        )

    return render_template(
        "password_generator.html",
        password=password
    )

if __name__ == "__main__":

    app.run(debug=True)