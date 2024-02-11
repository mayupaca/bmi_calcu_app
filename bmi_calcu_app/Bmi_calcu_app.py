# BMI Calculator App
# Create an application/program for a BMI Calculator.
# You can use the tkinter library for the interface, store a few users' data in a file and use matplotlib to display the BMI chart.
# You may choose to display it as a pie chart(percentage of people overweight/underweight/normal/obese)or bar chart.
# BMI ＝ 体重kg ÷ (身長m)2

import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title('BMI Calculator')
frame = tkinter.Frame(window)
frame.pack()

# ---------- User info ----------
user_info = tkinter.LabelFrame(frame, text='User Information')
user_info.grid(row=0, column=0)

height_label = tkinter.Label(user_info, text='Height: ')
height_label.grid(row=0, column=0, padx=10, pady=10)
height_txt = tkinter.Entry(user_info)
height_txt.grid(row=0, column=1, padx=10, pady=10)

weight_label = tkinter.Label(user_info, text='weight: ')
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_txt = tkinter.Entry(user_info)
weight_txt.grid(row=1, column=1, padx=10, pady=10)


window.mainloop()