# BMI Calculator App
# Create an application/program for a BMI Calculator.
# You can use the tkinter library for the interface, store a few users' data in a file and use matplotlib to display the BMI chart.
# You may choose to display it as a pie chart(percentage of people overweight/underweight/normal/obese)or bar chart.
# BMI ＝ 体重kg ÷ (身長m)2

import csv
import tkinter
from tkinter import messagebox

def calculator():
    usr_height = int(height_txt.get())
    usr_weight = int(weight_txt.get())
    if usr_height == "" or usr_weight == "":
        tkinter.messagebox.showwarning(title="Error", message="Height and weight cannot be blank.")
    else:
        with open("bmilist.csv", "a") as bmi_file:
            bmi = usr_weight / (usr_height * usr_height)
            bmi_file.write(str(bmi))
        tkinter.messagebox.showinfo(title="Success", message="Saved")


window = tkinter.Tk()
window.title('BMI Calculator')
frame = tkinter.Frame(window)
frame.pack()

# ---------- User info ----------
user_info = tkinter.LabelFrame(frame, text='User Information', foreground="white", background="black")
user_info.grid(row=0, column=0)

height_label = tkinter.Label(user_info, text='Height (m): ', foreground="white", background="black")
height_label.grid(row=0, column=0, padx=10, pady=10)
height_txt = tkinter.Entry(user_info)
height_txt.grid(row=0, column=1, padx=10, pady=10)

weight_label = tkinter.Label(user_info, text='weight (kg): ', foreground="white", background="black")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_txt = tkinter.Entry(user_info)
weight_txt.grid(row=1, column=1, padx=10, pady=10)

calcu_button = tkinter.Button(frame, text="Calculate", command=calculator, foreground="white", background="black")
calcu_button.grid(row=2,column=0)

window.mainloop()