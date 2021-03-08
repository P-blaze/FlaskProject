from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask("__name__")

# in this we will get the info and then output it into registrants.html, but everytime we refresh the page
# the stored value will get reseted that is our data is not storing anywhere
# REGISTRANTS ={}

# now instead of using the dictionary which is totally no savable, we will use sqlite database 
# to store the values permanently

db = SQL("sqlite:///froshims.db")


SPORTS = [
		"DogeBall",
		"FootBall",
		"Soccer",
		"Cricket",
		"VollyBall"
	]

@app.route("/")
def index():
	return render_template("index.html", sports=SPORTS)


# def register():
# 	# the below line is keeping the security of the client side editing value of sport and sending it to
# 	# the server 
# 	if not request.form.get("name") or request.form.get("sport") not in SPORTS:
# 		return render_template("failure.html")
# 	# for supporting multiple sports inside the list SPORT as below only when we are using checkboxes
# 	#if not request.form.get("name") or  request.form.getlist("sport") not in SPORTS:
		
# 	return render_template("success.html")
@app.route("/register", methods=["POST"])
def register():
	name= request.form.get("name")
	if not name:
		return render_template("error.html", message="Missing name")
	sport = request.form.get("sport")
	if not sport:
		return render_template("error.html", message="Missing sport")
	if sport not in SPORTS:
		return render_template("error.html", message="INvalid sport")

	db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)",name,sport)
	
	# REGISTRANTS[name] = sport
	# print(REGISTRANTS)

	return redirect("/registrants") 
	

@app.route("/registrants")
def registrants():
	registrants = db.execute("SELECT * FROM registrants") # this is getting back rows which are dict in themselves
	return render_template("registrants.html", registrants = registrants)
	# return render_template("success.html")
	# return render_template("registrants.html", registrants = REGISTRANTS)
