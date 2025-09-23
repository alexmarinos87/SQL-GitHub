import pathlib
import pypdfium2
import tkinter
from tkinter import ttk
import os
import glob
import glob2

# function to convert all pdf stored in one file in another as txt files from the selection made by the user
def listfiles(directory, select_folder):
    for root, dirs, files in os.walk(directory):
        for f in files:
            print(f)
        newpath =   'src/company_docs_txt/' + select_folder
        p = f.replace("pdf", "")
        newpath = newpath + p
        if not os.path.exists(newpath): os.makedirs(newpath)
        os.system('pdftotext {0} {1}/{0}/txt'.format(f,newpath))

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

listfiles(directory, select_folder)