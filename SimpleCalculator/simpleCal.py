from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, pady=10, padx=10)


def myClick(number):
    # Tao bien lay gia tri tu entry
    current = e.get()
    e.delete(0, END)
    e.delete(0,)
    # Cong voi gia tri tiep theo
    e.insert(0, str(current) + str(number))


def equal():
    # Lay gia tri tu` entry
    #s = e.get()
    # Tach chuoi~ so' truoc va sau dau '+'
    #s1 = s[0:s.index("+")]
    #s2 = s[s.index("+")+1:]
    # Tong 2 so'
    #s3 = int(s1) + int(s2)
    second_num = e.get()
    # Xoa
    e.delete(0, END)
    # Hien thi ket qua
    e.insert(0, first_number + int(second_num))


def button_adds():
    #first_num = e.get()
    global first_number
    first_number = int(first_num)
    e.delete(0, END)


def clear():
    e.delete(0, END)


button9 = Button(root, text="9", padx=40,
                 # Dung lambda de tao ham lay gia tri tu button
                 pady=20, command=lambda: myClick(9))
button8 = Button(root, text="8", padx=40,
                 pady=20, command=lambda: myClick(8))
button7 = Button(root, text="7", padx=40,
                 pady=20, command=lambda: myClick(7))
button6 = Button(root, text="6", padx=40,
                 pady=20, command=lambda: myClick(6))
button5 = Button(root, text="5", padx=40,
                 pady=20, command=lambda: myClick(5))
button4 = Button(root, text="4", padx=40,
                 pady=20, command=lambda: myClick(4))
button3 = Button(root, text="3", padx=40,
                 pady=20, command=lambda: myClick(3))
button2 = Button(root, text="2", padx=40,
                 pady=20, command=lambda: myClick(2))
button1 = Button(root, text="1", padx=40,
                 pady=20, command=lambda: myClick(1))
button0 = Button(root, text="0", padx=40,
                 pady=20, command=lambda: myClick(0))
button_add = Button(root, text="+", padx=39,
                    pady=20, command=button_adds)
button_equal = Button(root, text="=", padx=89,
                      pady=20, command=equal)
button_clear = Button(root, text="clear", padx=79,
                      pady=20, command=clear)
button9.grid(row=1, column=0)
button8.grid(row=1, column=1)
button7.grid(row=1, column=2)

button6.grid(row=2, column=2)
button5.grid(row=2, column=1)
button4.grid(row=2, column=0)

button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
