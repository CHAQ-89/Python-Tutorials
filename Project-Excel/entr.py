import tkinter as tk
import openpyxl
wb = openpyxl.load_workbook("quyet.xlsx")
ws = wb.active

root = tk.Tk()

en = tk.Entry(root, width=50)
en.pack()
en.get()


def myClick():
    ws.append([en.get()])
    wb.save("quyet.xlsx")


my_button = tk.Button(root, text="Add", command=myClick())
my_button.pack()
root.mainloop()
