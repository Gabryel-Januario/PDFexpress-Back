from PIL import Image
from fpdf import FPDF
import os

from app.utils import check_file_exists, get_file_extension

def image_to_pdf(input_path, output_path):
   
    check_file_exists(input_path)
    
    if get_file_extension(output_path).lower() != ".pdf":
        raise ValueError("The output file must have a .pdf extension")
    
    image = Image.open(input_path)
    
    pdf = FPDF()

    pdf.add_page()

    image_width, image_height = image.size
    pdf_width = 210  
    pdf_height = 297  
    
    scale = min(pdf_width / image_width, pdf_height / image_height)

    image = image.resize((int(image_width * scale), int(image_height * scale)))

    temp_image_path = "temp_image.jpg"
    image.save(temp_image_path)

    pdf.image(temp_image_path, 0, 0, pdf_width, pdf_height)

    pdf.output(output_path)

    os.remove(temp_image_path)

    return output_path
