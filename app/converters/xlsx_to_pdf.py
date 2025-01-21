import os
import win32com.client
from app.utils import check_file_exists, get_file_extension
from flask import jsonify
import pythoncom


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
            try:

                used_range = ws.UsedRange
                total_columns = used_range.Columns.Count
                total_rows = used_range.Rows.Count

                if total_columns > total_rows:
                    ws.PageSetup.Orientation = 2  
                else:
                    ws.PageSetup.Orientation = 1  

                ws.PageSetup.Zoom = False  
                ws.PageSetup.FitToPagesWide = 1  
                ws.PageSetup.FitToPagesTall = False  
            except Exception as e:
                
                raise e

        
        wb.ExportAsFixedFormat(0, output_path)
        wb.Close(SaveChanges=False)

    except Exception as e:
        
        raise e

    finally:
         
        wb = None
        excel.Quit()
        pythoncom.CoUninitialize()
        

    
    return output_path
