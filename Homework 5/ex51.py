import os

def find_pdf_size(directory):
    """Find the size of all PDF files in the given directory and its subdirectories."""
    size = 0
    for root, dirs, files in os.walk(directory):
        pdf_list = [name for name in files if name.lower().endswith('.pdf')]
        size+=sum(os.path.getsize(os.path.join(root, file)) for file in pdf_list)
    print(size)

find_pdf_size(".")