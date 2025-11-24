from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def predict():
    return [1, 2, 3, 4]

@app.route('/get-data', methods=['GET'])
def get_data():
    result = predict()
    return jsonify({"data": result})

if __name__ == '__main__':
    app.run(debug=True)
