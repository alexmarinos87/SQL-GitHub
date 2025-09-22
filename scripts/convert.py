# import modules
import os
import pdfplumber

# assign directories
directory_invoices = 'SRC_INVOICE_FILE_PATH'
directory_invoices_txt = 'SRC_INVOICE_TXT_FILE_PATH'

# get file name from invoices directory
invoices_file_name = os.path.basename(directory_invoices)

# iterate over files in src folder
for invoices_pdf in os.listdir(directory_invoices):
    #  using pdfplumber to extract text from pdf invoices files
    with pdfplumber.open("*.pdf") as pdf, open(  invoices_file_name + ".txt", "w",encoding="utf-8") as f:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                f.write(t + '\n')
