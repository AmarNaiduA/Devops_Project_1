from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "I am LW from India"

@app.route("/phone")
def lwphone():
	return "7989476233"

app.run(host="0.0.0.0.")