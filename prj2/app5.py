from flask import Flask , render_template ,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('main5.html')

@app.route('/state/<button>')
def state(button): 
    return render_template('state5.html',btn_state=button)

if __name__ == "__main__":
    app.run()


