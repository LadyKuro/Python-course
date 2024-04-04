import os

def find_pdf_size(directory):
    """Find the size of all PDF files in the given directory and its subdirectories."""
    pdf_list = []
    for root, dirs, files in os.walk(directory):
        pdf_list.extend([name for name in files if name.endswith('.pdf')])
    print(sum(os.path.getsize(os.path.join(root, file)) for file in pdf_list))

find_pdf_size(".")