import tkinter as tk
from tkinter import ttk

window = tk.Tk()

number = 0

def increment():
    global number
    number += 1
    label.config(text=number)

def decrement():
    global number
    number -= 1
    label.config(text=number)

if __name__ == '__main__':
    window.title('Increment using Tkinter')

    # Setting size of window 
    window_width = 200
    window_height = 200

    # Get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # Set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.resizable(False, False)

    window.columnconfigure(0, weight=1)

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)

    # Styles
    style = ttk.Style()
    style.theme_use("alt")
    style.configure('inc.TButton', background="#8DDBFF", font=('Helvetica', 15), relief="flat")
    style.map('inc.TButton', background=[('active', '#8DDBFF')])
    style.configure('dec.TButton', background="#FFA18D", font=('Helvetica', 15), relief="flat")
    style.map('dec.TButton', background=[('active', '#FFA18D')])
    style.configure('num.TLabel', background="#FFFFFF", font=('Helvetica', 15))

    button_increment = ttk.Button(window, text="Increment", style='inc.TButton', command=increment)
    button_increment.grid(column=0, row=0, sticky='nsew')

    label = ttk.Label(window, text=number, anchor="center", style="num.TLabel")
    label.grid(column=0, row=1, sticky='nsew')

    button_decrement = ttk.Button(window, text="Decrement", style='dec.TButton', command=decrement)
    button_decrement.grid(column=0, row=2, sticky='nsew')

    window.mainloop()