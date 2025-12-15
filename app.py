
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("hospital.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/patients", methods=["GET", "POST"])
def patients():
    con = get_db()
    cur = con.cursor()
    if request.method == "POST":
        cur.execute("INSERT INTO patients VALUES (?, ?, ?)", (
            request.form["id"],
            request.form["name"],
            request.form["age"]
        ))
        con.commit()
    patients = cur.execute("SELECT * FROM patients").fetchall()
    con.close()
    return render_template("patients.html", patients=patients)

@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    con = get_db()
    cur = con.cursor()
    if request.method == "POST":
        cur.execute("INSERT INTO appointments VALUES (?, ?, ?)", (
            request.form["pid"],
            request.form["date"],
            request.form["doctor"]
        ))
        con.commit()
    data = cur.execute("SELECT * FROM appointments").fetchall()
    con.close()
    return render_template("appointments.html", data=data)

@app.route("/billing", methods=["GET", "POST"])
def billing():
    con = get_db()
    cur = con.cursor()
    if request.method == "POST":
        cur.execute("INSERT INTO billing VALUES (?, ?)", (
            request.form["pid"],
            request.form["amount"]
        ))
        con.commit()
    bills = cur.execute("SELECT * FROM billing").fetchall()
    con.close()
    return render_template("billing.html", bills=bills)

if __name__ == "__main__":
    app.run(debug=True)
