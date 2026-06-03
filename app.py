from flask import Flask,jsonify
from netcheck import single_host,all
app = Flask(__name__)

@app.route('/single_host/<host_name>')
def single_host_check(host_name):
    return jsonify(single_host(host_name, 'True'))

@app.route('/all_host/')
def all_host():
    return jsonify(all('True'))