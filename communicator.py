# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals
import yaml
import urllib3
import json
decoder = None
routes = None
http = None


def initialize():
    """Initialize any parameters necessary for the communicator to perform"""
    global http, routes, decoder
    http = urllib3.PoolManager()
    routes = yaml.load(open("rscores.routes", "r"))
    decoder = json.JSONDecoder()

def do_request(values):
    """ Base function to perform a request through urllib3. Specialized wrapping for set, get and get specials
    """
    if "fields" in values:
        response = http.request(values["method"], values["url"], fields=values["fields"])
        return response
    else:
        response = http.request(values["method"], values["url"])
        return response


def set_text(text):
    """
    Method sets the text as the values for Stats
    :param text:
    :return: Response
    """
    request = dict()
    request["method"] = "POST"
    request["url"] = routes["target"] + routes["set"]
    request["fields"] = dict()
    request["fields"]["text"] = text
    return do_request(request)


def get_stats(stat=None):
    request = dict()
    request["method"] = "GET"
    if stat:
        request["url"] = routes["target"] + routes["stat"]
        request["url"] = request["url"] + stat

    else:
        request["url"] = routes["target"] + routes["stats"]

    return do_request(request)


if __name__ == "__main__":
    initialize()
    print set_text("reflection is the ability of a computer program to examine,\
         introspect, and modify its own structure and behavior at runtime.").data
    print get_stats().data

