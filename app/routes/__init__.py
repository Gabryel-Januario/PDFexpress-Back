from flask import Flask
from .upload import upload_bp

def init_app(app: Flask):
    app.register_blueprint(upload_bp, url_prefix='/api')