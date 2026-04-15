from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.context_processor
def inject_date():
    now = datetime.now().strftime("%d. %B %Y")
    return dict(last_updated=now)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sommerhus")
def sommerhus():
    return render_template("sommerhus.html")

@app.route("/omrade")
def omrade():
    return render_template("omrade.html")

@app.route("/aktiviteter")
def aktiviteter():
    return render_template("aktiviteter.html")

@app.route("/budget")
def budget():
    return render_template("budget.html")

if __name__ == "__main__":
    app.run(port=5059, debug=True)