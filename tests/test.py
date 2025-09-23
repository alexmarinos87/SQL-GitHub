import os
# Using os.walk()
for dirpath, dirs, files in os.walk('src/CompanyDocuments/invoices'): 
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.pdf'):
      print(fname)



"""import  tkinter
import tkinter.ttk 

class Gui:

    def __init__(self):
        self.root = tkinter.Tk()

        # Set up the Combobox
        self.selections = tkinter.Combobox(self.root)
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


app = Gui()
app.root.mainloop()"""


import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()



import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Great Britain Basketball')
root.geometry('800x449+300+130')
root.configure(bg='#072462')

#def variable and store based on selection
def comboclick(event):
    global select_sheet # Setting select_sheet to global, so it can be modified
    select_sheet = cb.get()

# I am setting here the same value of cb.current(), so if the user doesn't change it, you still get an output.
select_sheet = 'Mon'

#create combobox
cb = ttk.Combobox(root, value=('Mon', 'Tues', 'Wed', 'Thurs'))
cb.current(0)
cb.bind('<<ComboboxSelected>>', comboclick)
cb.pack()

#set close window button
button_close = tk.Button(root, width=35, text='Close Programme', command=root.quit, 
                      fg='#C51E42', bg='#B4B5B4', borderwidth=1).pack()

root.mainloop()

print(select_sheet)