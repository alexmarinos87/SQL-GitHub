def main():

    import pathlib
    import pdfminer

    for path in pathlib.Path("pdfs").glob("*.pdf"):
        with path.open("rb") as file:
            parser = pdfminer.pdfparser.PDFParser(file)
            document = pdfminer.pdfdocument.PDFDocument(parser, "")
            if not document.is_extracable:
                continue
                
                manager =  pdfminer.pdfinterp.PDFResourceManager()
                params = pdfminer.layout. LAParams()

                device = pdfminer.converter.PDFPageAggregator(manager, laparams = params)
                interpreter = pdfminer.pdfinterp.PDFPageInterpreter

                text = ""

                for page in pdfminer.pdfpage.PDFPage.create_pages(document):
                    interpreter.process_page(page)
                    for obj in device.get_result():
                        if isinstance(obj.pdfminer.layout.LTTextbox) or isinstance(obj.pdfminer.layout.LTTextLine):
                            text += obj.get_text()

        with open( "/{}.txt.".format(path.stem), "w") as file:
            file.write(text)
    return 0

if __name__ ==  "__main__":
    import sys
    sys.exit(main())

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