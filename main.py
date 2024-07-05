from types import MethodType
from flask import Flask, request
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return 'Change Directory To /add, /subtract, /multiply, /divide'


@app.route('/add', methods=['POST'])
def addition():
    if request.method == "POST":
        data = request.get_json()
        x = float(data['x'])
        y = float(data['y'])
        if x and y:
            return str(x + y)
        else:
            return "ERROR: You need an 'x' and 'y' key in your JSON Payload."
    else:
        return "ERROR: You need to use POST method."


@app.route('/subtract', methods=['POST'])
def subtraction():
    if request.method == "POST":
        data = request.get_json()
        x = float(data['x'])
        y = float(data['y'])
        if x and y:
            return str(x - y)
        else:
            return "ERROR: You need an 'x' and 'y' key in your JSON Payload."
    else:
        return "ERROR: You need to use POST method."


@app.route('/multiply', methods=['POST'])
def multipllication():
    if request.method == "POST":
        data = request.get_json()
        x = float(data['x'])
        y = float(data['y'])
        if x and y:
            return str(x * y)
        else:
            return "ERROR: You need an 'x' and 'y' key in your JSON Payload."
    else:
        return "ERROR: You need to use POST method."

@app.route("/division", methods=['POST'])
def division():
    if request.method == "POST":
        data = request.get_json()
        x = float(data['x'])
        y = float(data['y'])
        if x and y:
            return str(x / y)
        else:
            return "ERROR: You need an 'x' and 'y' key in your JSON Payload."
    else:
        return "ERROR: You need to use POST method."
@app.route("/mean", methods=["POST"])
def mean():
    if request.method == "POST":
        data = request.get_json()
        x = float(data['x'])
        y = float(data['y'])
        if x and y:
            return str(np.mean([x, y]))
        else:
            return "ERROR: You need an 'x' and 'y' key in your JSON Payload."
    else:
        return "ERROR: You need to use POST method."

@app.route("/median", methods=["POST"])
def median():
    if request.method == "POST":
        data = request.get_json()
        x = float(data['x'])
        y = float(data['y'])
        if x and y:
            return str(np.median([x, y]))
        else:
            return "ERROR: You need an 'x' and 'y' key in your JSON Payload."
    else:
        return "ERROR: You need to use POST method."
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
