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
        bmi = float(usr_weight) / (float(usr_height) * float(usr_height))
        bmi_label.config(text=f"BMI: {bmi:.2f}")  # show BMI
        with open("bmilist.csv", "a") as bmi_file:
            bmi_file.write(f"{bmi:.2f}\n")  # two decimal places
        tkinter.messagebox.showinfo(title="Success", message="Saved")

# function to show BMI category pie chart
def show_bmi_chart():
    numbers = list(num_status.values())
    labels = list(num_status.keys())

    fig, ax = plt.subplots()
    ax.pie(numbers, labels=labels, autopct='%1.1f%%')
    plt.show()

# read data from a CSV file and store it in a list
bmi_list = []
with open("bmilist.csv", "r") as read_file:
    reader = csv.reader(read_file)
    for row in reader:
        bmi_list.append(float(row[0]))

num_status = {"Obese": 0, "Overweight": 0, "Normal": 0, "Underweight": 0}

for bmi in bmi_list:
    if bmi > 30.0:
        num_status["Obese"] += 1
    elif bmi > 25.0:
        num_status["Overweight"] += 1
    elif bmi > 18.5:
        num_status["Normal"] += 1
    elif bmi <= 18.5:
        num_status["Underweight"] += 1

################## GUI ##############################################
window = tkinter.Tk()
window.title('BMI Calculator')
frame = tkinter.Frame(window)
frame.pack()

# ---------- User info ----------
user_info = tkinter.LabelFrame(frame, text='User Information')
user_info.grid(row=0, column=0, padx=10, pady=10)

height_label = tkinter.Label(user_info, text='Height (m): ')
height_label.grid(row=0, column=0, padx=10, pady=10)
height_txt = tkinter.Entry(user_info)
height_txt.grid(row=0, column=1, padx=10, pady=10)

weight_label = tkinter.Label(user_info, text='weight (kg): ')
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_txt = tkinter.Entry(user_info)
weight_txt.grid(row=1, column=1, padx=10, pady=10)

# ---------- Calculate button ----------
calcu_button = tkinter.Button(frame, text="Calculate", command=calculator)
calcu_button.grid(row=2,column=0)

# ---------- Show BMI ----------
bmi_label = tkinter.Label(frame, text="", foreground="black")
bmi_label.grid(row=3, column=0, pady=10)

# ---------- Chart button ---------
show_bmi_button = tkinter.Button(frame, text="Show BMI Chart", command=show_bmi_chart)
show_bmi_button.grid(row=4, column=0, pady=10)

window.mainloop()
