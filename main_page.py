from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/card")
def card():
    return render_template("card.html")


@app.route("/category_card")
def category_card():
    return render_template("category-card.html")


@app.route("/gardening")
def gardening():
    return render_template("gardening.html")


@app.route("/sailing")
def sailing():
    return render_template("sailing.html")


@app.route("/airbnb")
def airbnb():
    return render_template("airbnb.html")



if __name__ == "__main__":
    app.run(debug=True)