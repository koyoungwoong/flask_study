
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/userid/<int:userid>')
def getid(userid):
    # return 'UserID : %d' %userid
    return f'UserId : {userid}'

@app.route('/username/<username>')
def getname(username):
    return f'User Name : {username}'

if __name__ == "__main__": 
    app.run() 
