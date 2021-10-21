from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root)
e.grid(row=1, columnspan=4, sticky=N+S+E+W)


def myClick(number):
    # Tao bien lay gia tri tu entry
    current = e.get()
    e.delete(0, END)
    e.delete(0,)
    # Cong voi gia tri tiep theo
    e.insert(0, str(current) + str(number))


def equal():
    pass
    # Lay gia tri tu` entry
    #s = e.get()
    # Tach chuoi~ so' truoc va sau dau '+'
    #s1 = s[0:s.index("+")]
    #s2 = s[s.index("+")+1:]
    # Tong 2 so'
    #s3 = int(s1) + int(s2)
    # second_num = e.get()
    # # Xoa
    # e.delete(0, END)
    # # Hien thi ket qua
    # e.insert(0, first_number + int(second_num))


def button_adds():
    pass
    #first_num = e.get()
    # global first_number
    # first_number = int(first_num)
    # e.delete(0, END)


def clear():
    e.delete(0, END)


# Dung lambda de tao ham lay gia tri tu button
Button(root, text="9", command=lambda: myClick(9)).grid(
    row=2, column=2, sticky=N+S+E+W)
Button(root, text="8", command=lambda: myClick(8)).grid(
    row=2, column=1, sticky=N+S+E+W)
Button(root, text="7", command=lambda: myClick(7)).grid(
    row=2, column=0, sticky=N+S+E+W)
Button(root, text="+", command=lambda: myClick(6)
       ).grid(row=2, column=3, sticky=N+S+E+W)

Button(root, text="6", command=lambda: myClick(5)).grid(
    row=3, column=2, sticky=N+S+E+W)
Button(root, text="5", command=lambda: myClick(4)).grid(
    row=3, column=1, sticky=N+S+E+W)
Button(root, text="4", command=lambda: myClick(3)).grid(
    row=3, column=0, sticky=N+S+E+W)
Button(root, text="-", command=lambda: myClick(3)
       ).grid(row=3, column=3, sticky=N+S+E+W)

Button(root, text="3", command=lambda: myClick(2)).grid(
    row=4, column=2, sticky=N+S+E+W)
Button(root, text="2", command=lambda: myClick(1)).grid(
    row=4, column=1, sticky=N+S+E+W)
Button(root, text="1", command=lambda: myClick(0)).grid(
    row=4, column=0, sticky=N+S+E+W)
Button(root, text="*", command=lambda: myClick(0)
       ).grid(row=4, column=3, sticky=N+S+E+W)

Button(root, text="C", command=button_adds).grid(
    row=5, column=0, sticky=N+S+E+W)
Button(root, text="0", command=equal).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text="=", command=clear).grid(row=5, column=2, sticky=N+S+E+W)
Button(root, text="/", command=clear).grid(row=5, column=3, sticky=N+S+E+W)

root.mainloop()
