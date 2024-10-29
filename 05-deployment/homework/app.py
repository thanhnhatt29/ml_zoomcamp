import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model2.bin'
dv_file = 'dv.bin'

def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)

model = load(model_file)
dv = load(dv_file)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'subcription_probabiltiy': float(y_pred),
        'subcription': bool(churn)
    }

    return jsonify(result)

@app.route('/', methods=['GET'])
def helloworld():
    return("HelloWorld!")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)