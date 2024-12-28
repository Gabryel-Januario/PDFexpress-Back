from flask import Flask
import os 

app = Flask(__name__)

UPLOADS_FOLDER = os.path.join(os.getcwd(), "uploads")
CONVERTED_FOLDER = os.path.join(os.getcwd(), "converted")

os.makedirs(UPLOADS_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOADS_FOLDER
app.config["CONVERTED_FOLDER"] = CONVERTED_FOLDER


from routes import api
app.register_blueprint(api, url_prefix="/files")


if __name__ == "__main__":
    app.run(debug=True)