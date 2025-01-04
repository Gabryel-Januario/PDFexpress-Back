import os
from fpdf import FPDF

def text_to_pdf(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f'The file {input_path} not found.')
    
    if not output_path.lower().endswith('.pdf'):
        raise ValueError("the output file must have a .pdf extension")


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