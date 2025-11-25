from flask import jsonify, Blueprint, request
from ml_model.predict import predict
from ml_model.predict2 import predict2

song_bp = Blueprint("song", __name__)


@song_bp.route("/getDefault", methods=["GET"])
def getDefault():
    return jsonify([1, 2, 3])


@song_bp.route("/getSongs", methods=["POST"])
def getSongs():
    predict_result = predict()

    request_data = request.get_json()

    predict2_result = predict2(
        type=request_data.get("type"),
        key=request_data.get("key"),
        algorithm=request_data.get("algorithm"),
    )

    return jsonify({"predict": predict_result, "predict2": predict2_result})
