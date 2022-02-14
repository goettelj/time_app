from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Docker!'

@app.route('/time')
def current_time():
    now = datetime.now()
    return now.strftime("%I:%M%p")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
