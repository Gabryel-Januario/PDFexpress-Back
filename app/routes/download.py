from flask import send_from_directory, current_app, jsonify, Blueprint
import os


download_bp = Blueprint('download', __name__)

@download_bp.route("/download/<filename>", methods=['GET'])
def download_file(filename):

    converted_folder = current_app.config["CONVERTED_FOLDER"]

    file_path = os.path.join(converted_folder, filename)
    
    if not os.path.exists(file_path):
        current_app.logger.error(f"File not found: {file_path}")
        return jsonify({"error": "File not found"}), 404
    
    current_app.logger.info(f"Enviando arquivo: {file_path}")
    return send_from_directory(directory=converted_folder, path=filename, as_attachment=True)