"""Used to play with the code in order to learn the basics of Tkinter.

"""

# Import the library tkinter
import tkinter as tk
# Import the ttk widgets of tkinter
from tkinter import ttk
# Import the function configure_style
from gui_config import configure_style


###################### You'll copy here the code to play with ######################

# Jusqu'à la question 17 

"""
window = tk.Tk()
window.title("Playground")
configure_style()

first_frm = ttk.Frame(window, style="Sample.TFrame")
ttk.Label(first_frm, text="Grid (0, 0)", style="Sample.TLabel").grid(row=0, column=0, padx=10, pady=10, sticky='ew')
ttk.Label(first_frm, text="Grid (0, 1)", style="Sample.TLabel").grid(row=0, column=1, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (1, 0)", style="Sample.TLabel").grid(row=1, column=0, padx=10, pady=10)
ttk.Label(first_frm, text="Grid (1, 1)", style="Sample.TLabel").grid(row=1, column=1, padx=10, pady=10)
first_frm.columnconfigure(0, weight=1)
first_frm.columnconfigure(1, weight=1)
first_frm.pack(fill=tk.BOTH, expand=True)

second_frm = ttk.Frame(window, style="SampleBottom.TFrame")
ttk.Label(second_frm, text="Grid (0, 0)", style="Sample.TLabel").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(second_frm, text="Grid (0, 1)", style="Sample.TLabel").grid(row=0, column=1, padx=10, pady=10)
ttk.Label(second_frm, text="Grid (0, 2)", style="Sample.TLabel").grid(row=0, column=2, padx=10, pady=10)
second_frm.pack()

window.mainloop()
"""

entries = {}
buttons = {}

def click_ok_handler():
    print("The user clicked OK")

def check_first_ent(*args):
    text_field_content = entries["first_ent"][1].get().strip()
    print("The user typed {}".format(text_field_content) )
    if text_field_content[-1] == "#":
        ok_enabled_state()
    else:
        ok_disabled_state()

def ok_enabled_state():
    buttons["OK"].configure(state=["!disabled"])
    print("The button is now enabled")

def ok_disabled_state():
    buttons["OK"].configure(state=["disabled"])
    print("The button is now disabled")

window = tk.Tk()
window.title("Playground")
configure_style()
first_frm = ttk.Frame(window, style="Tab.TFrame")

first_ent_var = tk.StringVar(value="")
first_ent = ttk.Entry(first_frm, textvariable=first_ent_var)
first_ent_var.trace("w", check_first_ent)
entries["first_ent"] = (first_ent, first_ent_var)
first_ent.pack()

button = ttk.Button(first_frm, state="disabled", text="OK", command=click_ok_handler)
buttons["OK"] = button
button.pack()
first_frm.pack()
window.mainloop()



#####################################################################################
