from flask import Flask
import os 
from app.routes import init_app

app = Flask(__name__)

UPLOADS_FOLDER = os.path.join(os.getcwd(), "uploads")
CONVERTED_FOLDER = os.path.join(os.getcwd(), "converted")

os.makedirs(UPLOADS_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOADS_FOLDER
app.config["CONVERTED_FOLDER"] = CONVERTED_FOLDER


init_app(app)


if __name__ == "__main__":
    app.run(debug=True)