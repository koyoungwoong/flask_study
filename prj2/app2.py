from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    uname = "hong gil dong"
    return 'your name : %s' %uname