from PIL import Image
from fpdf import FPDF
import os

def image_to_pdf(image_path, output_pdf_path):
   
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} not found")
    
    image = Image.open(image_path)
    
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

    pdf.output(output_pdf_path)

    os.remove(temp_image_path)

    return output_pdf_path
