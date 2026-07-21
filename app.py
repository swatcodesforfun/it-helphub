from flask import Flask, render_template


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



if __name__ == "__main__":

    app.run(debug=True)