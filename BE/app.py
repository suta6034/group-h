from flask import Flask
from flask_cors import CORS
from controller.song_controller import song_bp
import os

app = Flask(__name__)
CORS(app)
app.register_blueprint(song_bp)

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "False").lower() == "true")
