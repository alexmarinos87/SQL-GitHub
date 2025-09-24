import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('Select folder to convert pdfs to txt for reconcilliation and analysis.')
root.geometry('800x449+300+130')
root.configure(bg ='#072462')

# def variable and store based on selection
def comboclick(event):
    global select_folder # Setting select _folder to global, so it can be modified
    select_folder = cb.get()

# I am setting here the same value of cb.currrent(), so if the user doesnt change it, you still get an output
select_folder = 'inventory_report'

# create combobox
cb = ttk.Combobox(root, value=('inventory_report', 'invoices', 'purchase_orders', 'shipping_orders'))
cb. current(0)
cb.bind('<<ComboboxSelected>>' , comboclick)
cb.pack()

# set close window button
button_close = tkinter.Button(root, width = 35, text = 'Close Programme', command=root.quit, fg='#C51E42', bg='#B4B5B4', borderwidth =1).pack()
root.mainloop()

print(select_folder)

    # set directory path from user combobox selection
if select_folder == 'inventory_report':
    directory = "src/company_docs_pdf/" + select_folder +"/monthly/monthly"
else: directory = "src/company_docs_pdf/" + select_folder

if select_folder == 'inventory_report':
    dest_directory = "src/company_docs_txt/" + select_folder 
else: dest_directory = "src/company_docs_txt/" + select_folder

def main():

    from pathlib import Path

    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfdevice import PDFDevice
    from pdfminer.layout import LAParams, LTTextBox, LTTextLine
    from pdfminer.converter import PDFPageAggregator

    for path in Path(directory).glob('*.pdf'):
        with path.open('rb') as file:
            parser = PDFParser(file)
            document = PDFDocument(parser, "")
            if not document.is_extractable:
                continue
            
            manager = PDFResourceManager()
            params = LAParams()

            device = PDFPageAggregator(manager, laparams=params)
            interpreter = PDFPageInterpreter(manager, device)

            text = ""
            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
                for obj in device.get_result():
                    if isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine):
                        text += obj.get_text()
        with open(dest_directory +'/{}.txt'.format(path.stem), 'w') as file:
            file.write(text)
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())