from flask import Flask, jsonify
app = Flask(__name__)

"""
@api {get} /hello/{name} Prints "Hello {name}"
@apiName HelloWorld
@apiParam (Url) {String} name the name to print
@apiSuccess (200) {String} message the hello {name} message
"""
@app.route("/hello/<name>")
def hello(name):
    return  jsonify(
        message='Hello ' + name
    )
