import os 
import win32com.client

def docx_to_pdf(input_path, output_path):


    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file {input_path} not found.")
    
    if not output_path.lower().endswith('.pdf'):
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