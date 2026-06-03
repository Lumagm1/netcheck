from flask import Flask,jsonify
from netcheck import single_host
app = Flask(__name__)

@app.route('/single_host/<host_name>')
def single_host_check(host_name):
    return jsonify(single_host(host_name, 'True'))

