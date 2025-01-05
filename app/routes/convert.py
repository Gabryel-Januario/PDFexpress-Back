from flask import request, jsonify, current_app, Blueprint
from werkzeug.utils import secure_filename
import os 

from app.converters import docx_to_pdf, image_to_pdf, txt_to_pdf, xlsx_to_pdf


convert_bp = Blueprint('convert', __name__)

@convert_bp.route('/convert', methods=['POST'])
def convert_file():
    data = request.json
    filename = data.get('filename')
    method = data.get('method')

    if method not in ['docx_to_pdf', 'image_to_pdf', 'txt_to_pdf', 'xlsx_to_pdf']:
        return jsonify({"error": "Invalid conversion method"}), 400

    input_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    output_path = os.path.join(current_app.config["CONVERTED_FOLDER"], f"{filename.rsplit('.', 1)[0]}.pdf")

    try:
        if method == 'docx_to_pdf':
            docx_to_pdf(input_path, output_path)
        elif method == 'image_to_pdf':
            image_to_pdf(input_path, output_path)
        elif method == 'txt_to_pdf':
            txt_to_pdf(input_path, output_path)
        elif method == 'xlsx_to_pdf':
            xlsx_to_pdf(input_path, output_path)

        return jsonify({"message": "File converted successfully", "download_url": f"/api/download/{output_path.split('/')[-1]}"})
   
    except Exception as e:
        return jsonify({'message': 'error converting file', 'error': str(e)}), 500