# import modules
import os
import pdfplumber
import dotenv
import glob

# helpers
from tkinter import *
from tkinter.ttk import *

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

class Gui:

    def __init__(self):
        self.root = Tk()

        # Set up the Combobox
        self.selections = Combobox(self.root)
        self.selections['values'] = ['invoices', 'inventory_report', 'purchase_orders', 'shipping_orders']
        self.selections.pack()

        # The Entry to be shown if "Custom" is selected
        self.custom_field = Entry(self.root)
        self.show_custom_field = False

        # Check the selection in 100 ms
        self.root.after(100, self.check_for_selection)

    def check_for_selection(self):
        '''Checks if the value of the Combobox equals "Custom".'''


        # Get the value of the Combobox
        value = self.selections.get()

        # If the value is equal to "Custom" and show_field is set to False
        if value == 'Custom' and not self.show_custom_field:

            # Set show_field to True and pack() the custom entry field
            self.show_custom_field = True
            self.custom_field.pack()


        # If the value DOESNT equal "Custom"
        elif value != 'Custom':

            # Set show_field to False
            self.show_custom_field = False

            # Destroy the custom input
            self.custom_field.destroy()

            # Set up a new Entry object to pack() if we need it later.
            # Without this line, tkinter was raising an error for me.
            # This fixed it, but I don't promise that this is the
            # most efficient method to do this.
            self.custom_field = Entry(self.root)

        # If the value IS "Custom" and we're showing the custom_feild
        elif value == 'Custom' and self.show_custom_field:
            pass


        # Call this method again to keep checking the selection box
        self.root.after(100, self.check_for_selection)

    btn_convert = self.Button(
    master=self,
    text="\N{RIGHTWARDS BLACK ARROW}"
)
    

app = Gui()
app.root.mainloop()
'''dotenv.load_dotenv() # load.env file into enviroment
# assign directories
directory_invoices = os.environ.get("SRC_INVOICE_FILE_PATH")
directory_invoices_txt = os.environ.get("SRC_INVOICE_TXT_FILE_PATH")

# get file name from invoices directory
invoices_file_name = os.path.basename(directory_invoices)'''
# Using os.walk()
for dirpath, dirs, files in os.walk('src/company_docs_pdf/' + self.selections.get()): 
  for filenamWWWe in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.pdf'):
        
    #  using pdfplumber to extract text from pdf invoices files
        with pdfplumber.open() as pdf, open( fname + ".txt", "w",encoding="utf-8") as f:
            for page in pdf.pages:
                 t = page.extract_text()
            if t:
                f.write(t + '\n')
