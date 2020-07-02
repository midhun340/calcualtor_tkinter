# MIDHUN MOHAN
from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("180x300+100+100")
window.title("calculator")
window.configure(background='#151d05')
window.resizable(0, 0)
my_font = font.Font(family='Helvetica', size=20, weight='bold')
input_field = Entry(window)
input_field.config(background="#20B2AA")
input_field.place(height=104, width=178)


def button_click(number):
    current = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current) + str(number))


def clear_input():
    input_field.delete(0, END)


def button_add():
    first_number = input_field.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    input_field.delete(0, END)


def button_sub():
    first_number = input_field.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    input_field.delete(0, END)


def button_mul():
    first_number = input_field.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    input_field.delete(0, END)


def button_div():
    first_number = input_field.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    input_field.delete(0, END)


def button_equal():
    second_number = input_field.get()
    input_field.delete(0, END)
    if math == "addition":
        input_field.insert(0, f_num + float(second_number))
    if math == "subtraction":
        input_field.insert(0, f_num - float(second_number))
    if math == "multiplication":
        input_field.insert(0, f_num * float(second_number))
    if math == "division":
        input_field.insert(0, f_num / float(second_number))


button1 = Button(window, text="+", command=button_add, bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button2 = Button(window, text="-", command=button_sub, bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button3 = Button(window, text="*", command=button_mul, bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button4 = Button(window, text="/", command=button_div, bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button5 = Button(window, text="=", command=button_equal, bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button6 = Button(window, text="0", command=lambda: button_click(0), bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button7 = Button(window, text="1", command=lambda: button_click(1), bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button8 = Button(window, text="2", command=lambda: button_click(2), bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button9 = Button(window, text="3", command=lambda: button_click(3), bg='#FF4500', fg='#0526fa', width="1", height="1",
                 bd="5")
button10 = Button(window, text="4", command=lambda: button_click(4), bg='#FF4500', fg='#0526fa', width="1", height="1",
                  bd="5")
button11 = Button(window, text="5", command=lambda: button_click(5), bg='#FF4500', fg='#0526fa', width="1", height="1",
                  bd="5")
button12 = Button(window, text="6", command=lambda: button_click(6), bg='#FF4500', fg='#0526fa', width="1", height="1",
                  bd="5")
button13 = Button(window, text="7", command=lambda: button_click(7), bg='#FF4500', fg='#0526fa', width="1", height="1",
                  bd="5")
button14 = Button(window, text="8", command=lambda: button_click(8), bg='#FF4500', fg='#0526fa', width="1", height="1",
                  bd="5")
button15 = Button(window, text="9", command=lambda: button_click(9), bg='#FF4500', fg='#0526fa', width="1", height="1",
                  bd="5")
button16 = Button(window, text=".", command=lambda: button_click("."), bg='#FF4500', fg='#0526fa', width="1",
                  height="1",
                  bd="5")
button17 = Button(window, text="c", command=clear_input, bg='#FF4500', fg='#0526fa', width=18, height="1",
                  bd="5")

button16.place(x=44.5, y=260)
button6.place(x=1, y=260)
button5.place(x=89, y=260)
button1.place(x=132.5, y=260)
button7.place(x=1, y=220.5)
button8.place(x=44.5, y=220.5)
button9.place(x=89, y=220.5)
button2.place(x=132.5, y=220.5)
button10.place(x=1, y=183)
button11.place(x=44.5, y=183)
button12.place(x=89, y=183)
button3.place(x=132.5, y=183)
button13.place(x=1, y=144)
button14.place(x=44.5, y=144)
button15.place(x=89, y=144)
button4.place(x=132.5, y=144)
button17.place(x=.5, y=105)
window.mainloop()
