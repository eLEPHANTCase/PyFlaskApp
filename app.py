from flask import Flask, Markup

# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    headers = {"Content-Type": "application/json"}
    return make_response("It worked!", 200, headers)
