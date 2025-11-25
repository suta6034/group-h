from flask import jsonify, Blueprint, request
from ml_model.predict import predict
from ml_model.predict2 import predict2

DEFAULT_SONGS = [1, 2, 3]

song_bp = Blueprint("song", __name__)


@song_bp.route("/getDefault", methods=["GET"])
def getDefault():
    try:
        return jsonify(DEFAULT_SONGS), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@song_bp.route("/getSongs", methods=["POST"])
def get_songs():
    try:
        request_data = request.get_json()
        if not request_data:
            return jsonify({"songs": DEFAULT_SONGS}), 200

        type_ = request_data.get("type")
        key = request_data.get("key")
        algorithm = request_data.get("algorithm")

        if not all([type_, key, algorithm]):
            return jsonify({"songs": DEFAULT_SONGS}), 200

        predict_result = predict()
        predict2_result = predict2(
            type=type_,
            key=key,
            algorithm=algorithm,
        )

        return jsonify({"predict": predict_result, "predict2": predict2_result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
