from app.converters.image_to_pdf import image_to_pdf
import os


def test_img_to_pdf():

    image_path = os.path.join('uploads', 'my.jpeg')
    output_pdf_path = os.path.join('converted', 'output.pdf')

    try:
        result = image_to_pdf(image_path, output_pdf_path)

        return print(f"Test Passed: PDF created successfully at {result}")
    
    except FileNotFoundError as e:
        print(f"Test Failed: {e}")
    except Exception as e:
        print(f"Test Failed: An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_img_to_pdf()