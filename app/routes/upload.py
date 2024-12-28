from flask import request, jsonify
from routes import api

@api.route('/upload', methods=["POST"])
def upload_file():
    file = request.files.get('file')

    if not file:
        return jsonify({'error': 'No files sent'}), 400
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        file.save(f'./uploads/{file.filename}')
    except Exception as e:
        return jsonify({"Error": f"Failed to save to file: {str(e)} " }), 500

    
    return jsonify({'message': f'File "{file.filename}" uploaded successfully!'}), 200