import os
from flask import *	
import copy 
app = Flask(__name__, static_url_path = "")

@app.route("/index")
def index(name = None):
    name = ""
    for i in os.walk("."):
        name = name + " --- " + str(i)
    return render_template('rease.html', name = "")
	
@app.route("/login_check", methods = ["POST"])
def login_check():
	username = request.form["username"];
	password = None
	password = request.form["password"];
	value = "You are " + username 
	if not password =="benovelance": 
		value = value + ". You don't have a password. So, bring a stash of golden apples to start  with ReaSE."
	else:
		value = value + ". You have a pasword, nice.. but ReaSE isn't up yet. So wait a little longer..."
	print "p--" + password
	return value
if __name__ == "__main__":
    app.run(debug=True)
