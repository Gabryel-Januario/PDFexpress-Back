from flask import request, jsonify, current_app, Blueprint
from werkzeug.utils import secure_filename

import os 

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file provided."}),400

    file = request.files["file"]
    method = request.form.get('method')

    if method == "docx_to_pdf":
        allowed_extensions = ['.docx']
    elif method == "image_to_pdf":
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.svg']
    elif method == "xlsx_to_pdf":
        allowed_extensions = ['.xlsx']
    elif method == "txt_to_pdf":
        allowed_extensions = ['.txt']
    else:
        return jsonify({"error": "Invalid method provided."}), 400

    if file:
        filename = secure_filename(file.filename)
        if not any(filename.lower().endswith(ext) for ext in allowed_extensions):
            return jsonify({"error": f"Invalid file type for {method}. Allowed types are {', '.join(allowed_extensions)}."}), 400

        input_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename )
        file.save(input_path)
        return jsonify({"message": "File uploaded successfully", "filename": filename, "method": method}), 200
    
    return jsonify({"error": "File upload failed"}), 500
    
