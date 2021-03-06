import os
import multiprocessing as mp

from werkzeug.contrib.fixers import ProxyFix

import text_statistics as ts
import json
from flask import Flask, request, Response, render_template
import copy

encode = json.JSONEncoder().encode
decode = json.JSONDecoder().decode
app = Flask(__name__, static_url_path="")
latest_text = None
pool1 = None
pool_result = None

ON_HEROKU = os.environ.get('PORT')

WELCOME_MESSAGE = """
Welcome fellow voyagers,
This is the home of Readability Shift Engine - ReaSE.
"""


def get_stats():
    return Response(encode({"code": "200", "value": latest_text.stats}))


def get_value(key):
    if key not in latest_text.stats:
        return Response(encode({"code": "200", "message": "No such stat"}), mimetype="text/json")

    else:
        return Response(encode({"code": "200", "value": latest_text.stats[key]}), mimetype="text/json")


get_funcs = {"stats": get_stats, "stat": get_value}


def start_pool():
    global pool1
    if not pool1:
        pool1 = mp.Pool(2)
    return pool1


def set_latest_text(result):
    global latest_text
    latest_text = result

@app.route("/")
def index():
    return WELCOME_MESSAGE


@app.route("/login_check", methods=["POST"])
def login_check():
    print "login_check()"
    username = request.form["username"];
    password = None
    password = request.form["password"];
    if password == "benovelance":
        return "http://localhost:1729/"

    return "false"


@app.route("/dashboard", methods=['GET'])
def dashboard():
    return "<html></html>"


@app.route("/text", methods=["POST"])
def setText():
    global pool1
    global pool_result
    pool1 = start_pool()
    pool_result = pool1.apply_async(ts.Text, [request.form["text"].encode('utf-8')], callback=set_latest_text)
    return Response(encode({"code": "200", "message": "success"}), mimetype='text/json')


@app.route("/text", methods=["GET"])
def getText():
    global pool1
    global pool_result
    if not pool_result:
        return Response(encode({"code": "200", "message": "Please post text first at /set as args"}),
                        mimetype="text/json")
    print latest_text
    if not latest_text:
        return Response(encode({"code": "200", "message": "still processing try again"}), mimetype="text/json")
    return latest_text.make_text_matrix()


@app.route("/text/substitute", methods=["POST"])
def subtitute_word():
    if not pool_result:
        return Response(encode({"code": "200", "message": "Please post text first at /set as args"}),
                        mimetype="text/json")
    print latest_text
    if not latest_text:
        return Response(encode({"code": "200", "message": "still processing try again"}), mimetype="text/json")
    data = request.get_data()
    substitution = decode(data)
    pool1.apply_async(latest_text.substitute_word(),
                      [substitution["sentence_index"], substitution["word_index"], substitution["new_word"]])
    return Response(encode({"code": "200", "message": "success"}))


@app.route("/text/<key>", methods=["GET"])
def getStats(key):
    if not pool_result:
        return Response(encode({"code": "200", "message": "Please post text first at /set as args"}),
                        mimetype="text/json")
    print latest_text
    if not latest_text:
        return Response(encode({"code": "200", "message": "still processing try again"}), mimetype="text/json")

    if key == "stats":
        return get_funcs["stats"]()

    else:
        return get_funcs["stat"](key)


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    if ON_HEROKU:
        # get the heroku port
        port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
        print "HEROKU PORT set ------------------" + str(port)
    else:
        port = 5000
        print "NOT HEROKU ------------------"
    app.run(host="0.0.0.0", port=port, debug=True)
