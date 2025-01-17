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
        print("Abrindo o arquivo no Excel...")
        wb = excel.Workbooks.Open(input_path)

        print("Configurando as páginas...")
        for ws in wb.Sheets:
            try:
                ws.PageSetup.Orientation = 2 # Orientação paisagem
                ws.PageSetup.Zoom = False  # Desativa zoom automático
                ws.PageSetup.FitToPagesWide = 1  # Ajusta para caber em uma página de largura
                ws.PageSetup.FitToPagesTall = False  # Permite altura flexível
            except Exception as e:
                print(f"Erro ao configurar a página: {str(e)}")
                raise e

        print("Exportando para PDF...")
        wb.ExportAsFixedFormat(0, output_path)
        wb.Close(SaveChanges=False)

    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        raise e

    finally:
        try:
            print("Fechando Excel...")
            wb = None
            excel.Quit()
            pythoncom.CoUninitialize()
        except Exception as e:
            print(f"Erro ao liberar recursos: {str(e)}")

    print("Conversão concluída com sucesso.")
    return output_path
