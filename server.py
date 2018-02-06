from flask import Flask, render_template, request, redirect, session, jsonify
app = Flask(__name__)
app.secret_key = "aoksnjdfkoanpoedjnaw"
import random
from datetime import datetime

@app.route("/")
def index():
	if "gold" not in session:
		session["gold"] = 0
		session["log"] = []
	return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def process_money():
	if request.form["building"] == "farm":
		session["gain"] = random.randrange(10, 21)
		session["time"] = datetime.now()
		session["gold"] += session["gain"]
		session["log"].append({"class":"green", "text":"Earned " + str(session["gain"]) + " golds from the " + request.form["building"] +"! (" + str(session["time"]) + ")"})
	elif request.form["building"] == "cave":
		session["gain"] = random.randrange(5, 11)
		session["time"] = datetime.now()
		session["gold"] += session["gain"]
		session["log"].append({"class":"green", "text":"Earned " + str(session["gain"]) + " golds from the " + request.form["building"] +"! (" + str(session["time"]) + ")"})
	elif request.form["building"] == "house":
		session["gain"] = random.randrange(2, 6)
		session["time"] = datetime.now()
		session["gold"] += session["gain"]
		session["log"].append({"class":"green", "text":"Earned " + str(session["gain"]) + " golds from the " + request.form["building"] +"! (" + str(session["time"]) + ")"})
	elif request.form["building"] == "casino":
		session["gain"] = random.randrange(-50, 51)
		session["time"] = datetime.now()
		session["gold"] += session["gain"]
		if session["gain"] < 0:
			session["log"].append({"class":"red", "text":"Entered a casino and lost " + str(session["gain"]* (-1)) + " golds... Ouch.. (" + str(session["time"]) + ")"})
		elif session["gain"] > 0:
			session["log"].append({"class":"green", "text":"Entered a casino and won " + str(session["gain"]) + " golds... Nice! (" + str(session["time"]) + ")"})
		else:
			session["log"].append({"class":"green", "text":"Entered a casino and came out even. (" + str(session["time"]) + ")"})
	return redirect("/")

@app.route("/restart")
def restart():
	if "gain" not in session:
		return redirect("/")
	else:
		session.pop("gold")
		session.pop("gain")
		session.pop("time")
		session.pop("log")
		return redirect("/")

app.run(debug=True)