from flask import Flask, jsonify
app = Flask(__name__)

"""
@api {get} /sample/{message} hello world sample request
@apiName GetSample
@apiParam (Url) {String} message the message to return
@apiSuccess (Success_200) {String} data the hello world data
@apiSuccess (Success_200) {String} output what the user entered in the url
"""
@app.route("/sample/<message>")
def hello(message):
    return  jsonify(
        data='Hello World',
        output=message
    )
