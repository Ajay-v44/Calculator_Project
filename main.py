from tkinter import *

window = Tk()
window.geometry("500x400")
window.title("Calculator")
window.config(background="grey")

x = ""  # Initialize x as an empty string
operator = ""  # Initialize operation as an empty string
result = 0  # Initialize result as 0


def clear():
    global x
    x = ""
    text.config(text=x)


def act(num):
    global x, operator, result
    if num == "=":
        if operator == "+":
            result += float(x)  # Perform addition
        elif operator == "-":
            result -= float(x)  # Perform subtraction
        elif operator == "x":
            result *= float(x)  # Perform multiplication
        elif operator == "/":
            result /= float(x)  # Perform division
        x = str(result)  # Update x with the result
        operator = ""
    elif str(num) in ("+", "-", "x", "/"):
        result = float(x) if x else 0  # Use 0 as default value if x is empty
        x = ""  # Clear x for the next number input
        operator = str(num)  # Set the selected operator
    else:
        x += str(num)  # Append the button name to the existing text
    if operator:
        text.config(text=operator + " " + x)  # Update the text of the Label widget with operator and x
    else:
        text.config(text=x)


text = Label(window, text=x, fg="Red", font=("sans-serif", 18), width=34)
text.place(x=10, y=20)

# first_row_buttons
seven = Button(text="7", command=lambda: act(7), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
seven.place(x=20, y=65)
eig = Button(text="8", command=lambda: act(8), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
eig.place(x=120, y=65)
nine = Button(text="9", command=lambda: act(9), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
nine.place(x=220, y=65)
sub = Button(text="-", command=lambda: act("-"), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
sub.place(x=320, y=65)
div = Button(text="/", command=lambda: act("/"), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
div.place(x=420, y=65)

# second_row_buttons

four = Button(text="4", command=lambda: act(4), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
four.place(x=20, y=120)
five = Button(text="5", command=lambda: act(5), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
five.place(x=120, y=120)
six = Button(text="6", command=lambda: act(6), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
six.place(x=220, y=120)
add = Button(text="+", command=lambda: act("+"), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
add.place(x=320, y=120)

# third_row_buttons

one = Button(text="1", command=lambda: act(1), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
one.place(x=20, y=180)
two = Button(text="2", command=lambda: act(2), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
two.place(x=120, y=180)
three = Button(text="3", command=lambda: act(3), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
three.place(x=220, y=180)
mul = Button(text="x", command=lambda: act("x"), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
mul.place(x=320, y=180)

# fourth_row_buttons

zero = Button(text="0", command=lambda: act(0), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
zero.place(x=20, y=240)
dot = Button(text=".", command=lambda: act("."), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
dot.place(x=120, y=240)
clear_button = Button(text="C", command=lambda: clear(), width=10, height=2, bg="red", fg="white",
                      font=("sans-serif", 10))
clear_button.place(x=220, y=240)
equal = Button(text="=", command=lambda: act("="), width=10, height=2, bg="black", fg="white", font=("sans-serif", 10))
equal.place(x=320, y=240)

window.mainloop()
