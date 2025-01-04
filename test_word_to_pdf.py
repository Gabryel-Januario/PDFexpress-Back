import os 
from app.converters.docx_to_pdf import docx_to_pdf

def test_word_to_pdf():

    file_path = os.path.abspath('uploads/doc.docx')
    output_path = os.path.abspath('converted/doc.pdf')

    try:
        result = docx_to_pdf(file_path, output_path)
        print(f"Word document successfully converted to PDF: {result}")
    except Exception as e:
        print(f'error: {e}')

test_word_to_pdf()