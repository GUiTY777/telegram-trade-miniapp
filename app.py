from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS trades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    owner_id TEXT,
                    offer TEXT,
                    want TEXT
                )''')
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_trade", methods=["POST"])
def create_trade():
    owner_id = request.form.get("owner_id")
    offer = request.form.get("offer")
    want = request.form.get("want")
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("INSERT INTO trades (owner_id, offer, want) VALUES (?, ?, ?)", (owner_id, offer, want))
    conn.commit()
    conn.close()
    return "Trade created!"

@app.route("/trades")
def trades():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM trades")
    all_trades = c.fetchall()
    conn.close()
    return {"trades": all_trades}

if __name__ == "__main__":
    init_db()
    app.run()