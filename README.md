# Python Example

A sample of a python microservice block for [kintohub](http://kintohub.com)


It is using python `3.6.4`

# First time setup
* `pip install -r requirements.txt`

# Run
- `FLASK_APP=hello.py flask run` runs on port `5000`
- `FLASK_APP=hello.py flask run --port=80 --host=0.0.0.0` runs on port 80 and the server is accessable by external calls
 
