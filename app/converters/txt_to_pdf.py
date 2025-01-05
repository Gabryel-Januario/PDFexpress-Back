import os
from fpdf import FPDF
from app.utils import check_file_exists, get_file_extension




def txt_to_pdf(input_path, output_path):
    

    check_file_exists(input_path)
    
    if get_file_extension(output_path).lower() != ".pdf":
        raise ValueError("The output file must have a .pdf extension")


    pdf = FPDF()
    pdf.auto_page_break = 15
    pdf.add_page()
    pdf.set_font('Arial', size=12)


    with open(input_path, "r", encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        pdf.multi_cell(0,10, line.strip())

    pdf.output(output_path)


    return output_path