import os
from flask import *	
import copy 
app = Flask(__name__, static_url_path = "")

@app.route("/")
def index(name = None):
    name = ""
    for i in os.walk("."):
        name = name + " --- " + str(i)
    return render_template('login.html', name = "")
	
@app.route("/login_check", methods = ["POST"])
def login_check():
	username = request.form["username"];
	password = None
	password = request.form["password"];
	value = "<body>You are " + username 
	if not password =="benovelance": 
		#return redirect()
	else:
		value = value + ". You have a pasword, nice.. but ReaSE isn't up yet. So wait a little longer..."
	print "p--" + password
	
	value = value + "</body>"
	return value
if __name__ == "__main__":
    app.run(debug=True)
