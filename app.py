from urllib import request
from flask import Flask, render_template
import opp_averages

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def add():
    name = int(request.args.get("name"))
    answer = int(request.args.get("answer"))
    result = opp_averages.main(name, answer)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
