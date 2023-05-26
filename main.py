from tkinter import *

window = Tk()
window.geometry("500x400")
#Title_Added
window.title("Calculator")
window.config(background="grey")


def act():
    print("Clicked")

#textfield_added
text = Label(window, text="Welcome", fg="Red", font=("sans-serif", 18), width=34)
text.place(x=10, y=20)

#first_row_buttons
seven = Button(text="7", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
seven.place(x=20, y=65)
eig = Button(text="8", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
eig.place(x=120, y=65)
nine = Button(text="9", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
nine.place(x=220, y=65)
sub = Button(text="-", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
sub.place(x=320, y=65)

#second_row_buttons

four = Button(text="4", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
four.place(x=20, y=120)
five = Button(text="5", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
five.place(x=120, y=120)
six = Button(text="6", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
six.place(x=220, y=120)
add = Button(text="+", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
add.place(x=320, y=120)

#third_row_buttons

one = Button(text="1", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
one.place(x=20, y=180)
two = Button(text="2", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
two.place(x=120, y=180)
three = Button(text="3", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
three.place(x=220, y=180)
equal = Button(text="=", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
equal.place(x=320, y=180)

#fourth_row_buttons

zero = Button(text="0", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
zero.place(x=20, y=240)
dot = Button(text=".", command=act, width=10, height=2, bg="black", fg="white",font=("sans-serif", 10))
dot.place(x=120, y=240)
clear = Button(text="C", command=act, width=10, height=2, bg="red", fg="white",font=("sans-serif", 10))
clear.place(x=220, y=240)


window.mainloop()
