import os 
import win32com.client

from app.utils import check_file_exists, get_file_extension

def docx_to_pdf(input_path, output_path):

    check_file_exists(input_path)
    
    if get_file_extension(output_path).lower() != ".pdf":
        raise ValueError("The output file must have a .pdf extension")
    
    word = win32com.client.Dispatch('word.application')
    word.Visible = False

    try:

        doc = word.Documents.Open(input_path)

        doc.SaveAs(output_path, FileFormat=17)
        doc.Close()
    finally:
        word.Quit()
    
    return output_path  