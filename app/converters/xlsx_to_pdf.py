import os 
import win32com.client
from app.utils import check_file_exists, get_file_extension
from flask import jsonify
import pythoncom

def xlsx_to_pdf(input_path, output_path):
    pythoncom.CoInitialize()

    check_file_exists(input_path)
    
    if get_file_extension(output_path).lower() != ".pdf":
        raise ValueError("The output file must have a .pdf extension")

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False

    try:
        wb = excel.Workbooks.Open(input_path)

        for ws in wb.Sheets:
            ws.PageSetup.Orientation = 2

        wb.ExportAsFixedFormat(0, output_path)

        wb.close(SaveChanges=False)

    except Exception as e:
        return jsonify({"error": str(e)}),500
    finally:
        excel.Quit()

    return output_path