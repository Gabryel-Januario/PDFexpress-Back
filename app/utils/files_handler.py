import os 

def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]