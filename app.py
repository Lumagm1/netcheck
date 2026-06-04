from flask import Flask,jsonify,render_template
from netcheck import single_host,ping_all,watch_timer,port
app = Flask(__name__)

@app.route('/single_host/<host_name>')
def single_host_check(host_name):
    return jsonify(single_host(host_name, True))

@app.route('/all_host')
def all_host():
    return jsonify(ping_all(True))

@app.route('/single_host/port/<host_name>/<port_num>')
def single_host_port(host_name,port_num):
    return jsonify(port(host_name,port_num,True))

@app.route('/single_host/watch/<host_name>/<int:watch>')
def single_host_interval(host_name,watch):
    return jsonify(watch_timer('s',watch,True,host_name))

@app.route('/')
def index():
    return render_template('index.html')