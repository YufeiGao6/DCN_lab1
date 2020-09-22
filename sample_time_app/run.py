from flask import Flask
import time


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
	time_str = time.strftime('%A %B, %d %Y %H:%M:%S', time.localtime())
	return time_str


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
