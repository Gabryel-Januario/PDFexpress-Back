import os 
from app.converters.xlsx_to_pdf import xlsx_to_pdf

def test_xlsx_to_pdf():

    input_path = os.path.abspath('uploads/test.xlsx')
    output_path = os.path.abspath('converted/output.pdf')

    try:
        result = xlsx_to_pdf(input_path, output_path)
        print(f"Excel file successfully converted to PDF: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    test_xlsx_to_pdf()