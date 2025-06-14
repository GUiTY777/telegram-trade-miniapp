from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os

app = Flask(__name__)

TRADES_FILE = "trades.json"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_trade", methods=["POST"])
def create_trade():
    wallet = request.form["wallet"]
    nft_name = request.form["nft_name"]
    token = request.form["token"]

    trade = {"wallet": wallet, "nft_name": nft_name, "token": token}

    trades = []
    if os.path.exists(TRADES_FILE):
        with open(TRADES_FILE, "r") as f:
            trades = json.load(f)

    trades.append(trade)

    with open(TRADES_FILE, "w") as f:
        json.dump(trades, f)

    return redirect(url_for("index"))

@app.route("/trades")
def list_trades():
    trades = []
    if os.path.exists(TRADES_FILE):
        with open(TRADES_FILE, "r") as f:
            trades = json.load(f)
    return render_template("trades.html", trades=trades)

# ✅ Новый маршрут для манифеста
@app.route("/tonconnect-manifest.json")
def tonconnect_manifest():
    return send_from_directory("static", "tonconnect-manifest.json")

if __name__ == "__main__":
    app.run(debug=True)
