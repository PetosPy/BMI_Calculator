from tkinter import *
from tkinter import messagebox

#----------- Info -----------
def message():
    messagebox.showinfo(title="BMI info", message= """Body mass index is a value derived from the mass and height of a person. 
\nIt is defined as the body mass divided by the square of the body height,
\nand is universally expressed in units of kg/m², resulting from mass in kilograms and height in metres.""")


#----------- Calculations -----

def bmi_calculate():
    try:
        mass = float(weight_input.get())
        height = float(height_input.get())
    
    except ValueError as error_message:
        pass
        
    else:
        bmi = mass / (height * height)

        if bmi < 18.5:
          messagebox.showinfo(title="Underweight", message=f"You have a BMI of {bmi:.0f}")
        elif bmi <= 25:
          messagebox.showinfo(title="Normal weight", message=f"You have a BMI of {bmi:.0f}")
        elif bmi <= 30:
          messagebox.showinfo(title="Overweight", message=f"You have a BMI of {bmi:.0f}")
        elif bmi <= 35:
          messagebox.showinfo(title="Obese", message=f"You have a BMI of {bmi:.0f}")
        else:
          messagebox.showinfo(title="Clinically Obese", message=f"You have a BMI of {bmi:.0f}")

        height_input.delete(0, END)
        weight_input.delete(0, END)


#---------- UI Setup ----------
window = Tk()
window.title("BMI Calculator")
window.config(padx=120, pady=50, bg="white")

canvas = Canvas(window, width=220, height=220, highlightthickness=0)
bmi_logo = PhotoImage(file="bmi_metre.png")
canvas.create_image(110, 110, image=bmi_logo)
canvas.grid(row=0, column=1, columnspan=2)

########### Labels #############
weight = Label(text="Weight in Kg's:", bg="white", font=("ariel", 10, "bold"))
weight.grid(row=2, column=0)

height = Label(text="Height in metres:", bg="white", font=("ariel", 10, "bold"))
height.grid(row=3, column=0)


########### Inputs #############
weight_input = Entry(width=35)
weight_input.grid(row=2, column=1, columnspan=2)

height_input = Entry(width=35)
height_input.grid(row=3, column=1, columnspan=2)

########### Buttons #############
info_button = Button(width=30, text="Info", font=("ariel", 10, "bold"), command=message)
info_button.grid(row=1, column=1, columnspan=2)

calculate_button = Button(width=15, text="Calculate", font=("ariel", 10, "bold"), command=bmi_calculate)
calculate_button.grid(row=5, column=1, columnspan=2)






window.mainloop()