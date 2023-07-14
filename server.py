import translator
import flask
from flask import request, jsonify
import json
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
app.config["JSONIFY_MIMETYPE"] = "application/json"
app.config["JSON_AS_ASCII"] = False


@app.route('/engToFr/<eng>', methods=['GET'])
def engToFr(eng):
    return translator.englishToFrench(eng)


@app.route('/frToEng/<fr>', methods=['GET'])
def frToEng(fr):
    return translator.frenchToEnglish(fr)


app.run()
