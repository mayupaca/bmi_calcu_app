# BMI Calculator App
# Create an application/program for a BMI Calculator.
# You can use the tkinter library for the interface, store a few users' data in a file and use matplotlib to display the BMI chart.
# You may choose to display it as a pie chart(percentage of people overweight/underweight/normal/obese)or bar chart.
import csv
import matplotlib.pyplot as plt
import tkinter
from tkinter import messagebox

# function calculate BMI
def calculator():
    usr_height = height_txt.get()
    usr_weight = weight_txt.get()
    if usr_height == "" or usr_weight == "":
        tkinter.messagebox.showwarning(title="Error", message="Height and weight cannot be blank.")
    else:
        with open("bmilist.csv", "a") as bmi_file:
            bmi = float(usr_weight) / (float(usr_height) * float(usr_height))
            bmi_file.write(f"{bmi:.2f}\n")
        tkinter.messagebox.showinfo(title="Success", message="Saved")

# read data from a CSV file and store it in a list
bmi_list = []
with open("bmilist.csv", "r") as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        bmi_list.append(row)

num_status = {"Obese": 0, "Overweight": 0, "Normal": 0, "Underweight": 0}

for bmi_data in bmi_list:
    bmi = float(bmi_data[0])
    if bmi > 30.0:
        num_status["Obese"] += 1
    elif bmi > 25.0:
        num_status["Overweight"] += 1
    elif bmi > 18.5:
        num_status["Normal"] += 1
    elif bmi <= 18.5:
        num_status["Underweight"] += 1

# ---------- Pie Chart ----------
numbers = list(num_status.values())
labels = list(num_status.keys())

fig, ax = plt.subplots()
ax.pie(numbers, labels=labels, autopct='%1.1f%%')
plt.show()

# ---------- GUI ----------
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