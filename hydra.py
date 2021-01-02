import tkinter as tk
import random

def create_window():
    window = tk.Toplevel(root)
    window.protocol("WM_DELETE_WINDOW", create_window)
    text = tk.Label(window, text = "Cut off a head, two more grow in its place.")
    text.pack()
    canvas = tk.Canvas(window, width = 200, height = 200)
    canvas.pack()
    x_cordinate = round(random.uniform(0, 900))
    y_cordinate = round(random.uniform(0, 1440))
    window.geometry("{}x{}+{}+{}".format(300, 300, x_cordinate, y_cordinate))

    window = tk.Toplevel(root)
    window.protocol("WM_DELETE_WINDOW", create_window)
    text = tk.Label(window, text = "Cut off a head, two more grow in its place.")
    text.pack()
    canvas = tk.Canvas(window, width = 200, height = 200)
    canvas.pack()
    x_cordinate = round(random.uniform(0, 900))
    y_cordinate = round(random.uniform(0, 1440))
    window.geometry("{}x{}+{}+{}".format(300, 300, x_cordinate, y_cordinate))

root = tk.Tk()
root.title("Hydra Virus")
text = tk.Label(root, text = "Cut off a head, two more grow in its place.")
text.pack()
canvas = tk.Canvas(root, width = 250, height = 250)      
canvas.pack()

root.protocol("WM_DELETE_WINDOW", create_window)
root.mainloop()