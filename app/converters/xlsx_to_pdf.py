import os 
import win32com.client
from app.utils import check_file_exists, get_file_extension
from flask import jsonify
import pythoncom
import time



def xlsx_to_pdf(input_path, output_path):
    pythoncom.CoInitialize()

    if os.path.basename(input_path).startswith("~$"):
        raise ValueError("Temporary Excel files cannot be converted.")

    check_file_exists(input_path)
    
    if get_file_extension(output_path).lower() != ".pdf":
        raise ValueError("The output file must have a .pdf extension")

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False 

    try:
        wb = excel.Workbooks.Open(input_path)

        for ws in wb.Sheets:
            ws.PageSetup.Orientation = 2

        wb.ExportAsFixedFormat(0, output_path)

        wb.close(SaveChanges=False)

    except Exception as e:
        return jsonify({"error": str(e)}),500
    finally:
        try:
            # Fechar o Excel, garantir que todos os objetos COM sejam descartados
            wb = None  # Elimina o objeto Workbook
            excel.Quit()  # Tenta fechar a aplicação Excel
           
            
            pythoncom.CoUninitialize()  # Libera o COM
        except Exception as e:
            print(f"Erro ao tentar fechar o Excel: {str(e)}")

    return output_path