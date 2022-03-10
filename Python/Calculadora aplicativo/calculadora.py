#Importando tinker
from ast import Delete
from codecs import BOM_UTF8
from distutils.command.clean import clean
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from turtle import width
from unittest import result

#Colors

color1 = '#b4b8b7' #blue
color2 = '#d4d1c7' #grey
color3 = '#487a38' #'dark green'
color4 = '#637551' #dark grey
color5 = '#000000' #black



calc = Tk()
calc.title('Calculator')
calc.geometry('263x425')
calc.config(bg=color1)

#creating frames
frame_display = Frame(calc, width =263, height=75, bg=color2)
frame_display.grid(row=0, column=0)

frame_body = Frame(calc, width=263, height=350)
frame_body.grid(row=1, column=0)



#var all values
all_values = ''

#creating label
value_text = StringVar()

#creating functions

def enter_values(event):

    global all_values
    all_values = all_values + str(event)

    #putting the value on the screen
    value_text.set(all_values)


#to calculate

def calculate():
    global all_values
    result = eval(all_values)
    value_text.set(str(result))

#clean the screen

def clean_screen():
    global all_values
    all_values = ''
    value_text.set('')


calc_label = Label(frame_display, textvariable=value_text, width=16, height=3, padx=9, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 19'), fg=color5)
calc_label.place(x=0, y=0)

#Creating buttons
b_1 = Button(frame_body, command= clean_screen, text='C', width=17 , height=4)
b_1.place(x=1, y=0)

b_2 = Button(frame_body, command=lambda: enter_values('%'), text='%',width=8, height=4)
b_2.place(x=131, y=0)

b_3 = Button(frame_body, command=lambda: enter_values('/'), text='/',width=8, height=4, bg=color3)
b_3.place(x=196, y=0)

b_4 = Button(frame_body, command=lambda: enter_values('*'), text='X',width=8, height=4, bg=color3)
b_4.place(x=196, y=71)

b_5 = Button(frame_body, command=lambda: enter_values('9'), text='9',width=8, height=4)
b_5.place(x=130, y=71)

b_6 = Button(frame_body, command=lambda: enter_values('8'), text='8',width=8, height=4)
b_6.place(x=65, y=71)

b_7 = Button(frame_body, command=lambda: enter_values('7'), text='7',width=8, height=4)
b_7.place(x=0, y=71)

b_9 = Button(frame_body, command=lambda: enter_values('-'), text='-',width=8, height=4, bg=color3)
b_9.place(x=196, y=142)

b_10 = Button(frame_body, command=lambda: enter_values('6'), text='6',width=8, height=4)
b_10.place(x=130, y=142)

b_11 = Button(frame_body, command=lambda: enter_values('5'), text='5',width=8, height=4)
b_11.place(x=65, y=142)

b_12 = Button(frame_body, command=lambda: enter_values('4'), text='4',width=8, height=4)
b_12.place(x=0, y=142)

b_13 = Button(frame_body, command=lambda: enter_values('+'), text='+',width=8, height=4)
b_13.place(x=259, y=213)

b_14 = Button(frame_body, command=lambda: enter_values('3'), text='3',width=8, height=4)
b_14.place(x=130, y=213)

b_15 = Button(frame_body, command=lambda: enter_values('2'), text='2',width=8, height=4)
b_15.place(x=65, y=213)

b_16 = Button(frame_body, command=lambda: enter_values('1'), text='1',width=8, height=4)
b_16.place(x=0, y=213)

b_17 = Button(frame_body, command=lambda: enter_values('+'), text='+',width=8, height=4, bg=color3)
b_17.place(x=196, y=213)

b_18 = Button(frame_body, command= calculate, text='=',width=8, height=4, bg=color4)
b_18.place(x=196, y=284)

b_20 = Button(frame_body, command=lambda: enter_values('0'), text='0',width=17, height=4)
b_20.place(x=0, y=284)

b_19 = Button(frame_body, command=lambda: enter_values(',') , text=',',width=8, height=4)
b_19.place(x=130, y=284)



calc.mainloop()