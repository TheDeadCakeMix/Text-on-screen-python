import tkinter as tk
from random import seed, choice
from string import ascii_letters

seed(42)

colors = ('red', 'green', 'blue', 'yellow', 'cyan', 'purple', 'orange', 'white', 'black')
def do_stuff():
    s = 'heh'
    color = choice(colors)
    l.config(text=":D", fg=color)
    root.after(500, do_stuff)
root = tk.Tk()
root.wm_overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
l = tk.Label(text='', font=("Helvetica", 60))
l.pack(expand=True)
do_stuff()
root.mainloop()
