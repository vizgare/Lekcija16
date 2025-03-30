from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    random_message = "Hoj"
    current_year = datetime.datetime.now().year
    cities = ["Ljubljana", "Bohinj", "Srednja vas 26"]


    return render_template("index.html", message = random_message,year = current_year, cities = cities)

@app.route("/game")
def game():
    return render_template("game.html")

if __name__ == "__main__":
    app.run()


