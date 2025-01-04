import os 
from app.converters.txt_to_pdf import txt_to_pdf

def test_text_to_pdf():
    print(f"Type of text_to_pdf: {type(txt_to_pdf)}")

    input_path = os.path.abspath('uploads/test.txt')
    output_path = os.path.abspath('converted/output.pdf')

    try:
        result = txt_to_pdf(input_path, output_path)
        print(f"Text successfully converted to PDF: {result}")
    except Exception as e:
        print(f'Error: {e}')
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_text_to_pdf()