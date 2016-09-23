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
	print "login_check()"
	username = request.form["username"];
	password = None
	password = request.form["password"];
	if password =="benovelance": 
		 return "http://localhost:1729/"
	
	return "false"
	
@app.route("/dashboard",methods = ['GET'])
def dashboard():
	return "<html></html>"
if __name__ == "__main__":
	port = int(os.environ.get('PORT',1729))
	app.run(host = "127.0.0.1",port = port ,debug=True)
