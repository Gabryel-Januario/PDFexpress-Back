# .xlsx

import os 
import win32com.client

def xlsx_to_pdf(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file {input_path} not found.")
    
    if not output_path.lower().endswith(".pdf"):
        raise ValueError("The output file must have a .pdf extension.")

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False

    try:
        wb = excel.Workbooks.Open(input_path)

        wb.ExportAsFixedFormat(0, output_path)

        wb.close()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        
        excel.Quit()

    return output_path