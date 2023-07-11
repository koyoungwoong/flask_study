from flask import Flask, render_template, request
import pickle
#import numpy as np
import stock_demo

#model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    #data1 = request.form['sp500.csv']
    #data2 = request.form['b']
    #data3 = request.form['c']
    #data4 = request.form['d']
    #arr = np.array([[data1, data2, data3, data4]])

    stock_demo.stock_predict()
    return render_template('after.html')


if __name__ == "__main__":
    app.run(debug=True)















