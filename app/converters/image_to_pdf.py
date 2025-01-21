from PIL import Image
from fpdf import FPDF
import os

from app.utils import check_file_exists, get_file_extension

def image_to_pdf(input_path, output_path):
   
    check_file_exists(input_path)
    
    if get_file_extension(output_path).lower() != ".pdf":
        raise ValueError("The output file must have a .pdf extension")
    
    image = Image.open(input_path)

    if image.mode == 'RGBA':
        image = image.convert('RGB')

    image_width, image_height = image.size
    is_landscape = image_width > image_height
    
    pdf = FPDF(orientation="L" if is_landscape else "P", unit="mm", format=(210, 297))
    pdf.add_page()

    pdf_width = 297 if is_landscape else 210
    pdf_height = 210 if is_landscape else 297
    
    scale = min(pdf_width / image_width, pdf_height / image_height)

    new_width = int(image_width * scale)
    new_height = int(image_height * scale)
    
    
    x_offset = (pdf_width - new_width) / 2
    y_offset = (pdf_height - new_height) / 2

    temp_image_path = "temp_image.jpg"
    image = image.resize((new_width, new_height), Image.LANCZOS)
    image.save(temp_image_path, format="JPEG", quality=95, optimize=True)

    pdf.image(temp_image_path, x=x_offset, y=y_offset, w=new_width, h=new_height)

    pdf.output(output_path)

    os.remove(temp_image_path)

    return output_path
