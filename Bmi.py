from cProfile import label
import tkinter as tk

#Create the GUI window
window = tk.Tk()
#Adds a name to the window frame
window.title("BMI Calculator")
#Creates a Secection for the standard input
frame = tk.Frame()

#header
label_header = tk.Label(text='Standard')
#User's Height
user_Height = tk.Label(text="Height in inches")
user_height_input = tk.Entry()
#user's Weight
user_weight_input = tk.Entry()
user_Weight = tk.Label(text="Weight")
#Creates the button
button = tk.Button(
    text="Convert",
    width=8,
    height=1,
    bg="white",
    fg="black",
)
#converts to BMI after button click, and prints to screen
def handle_click(event):
    height = user_height_input.get()
    weight = user_weight_input.get()
    sq = int(pow(int(height),2))
    BMI = int(weight)/int(sq)*703
    bmi = "{:.01f}".format(BMI)
    bmi_output = tk.Label(text=bmi)
    bmi_output.pack()

button.bind("<Button-1>", handle_click)
#Activates the code into GUI format
label_header.pack()

user_Height.pack()
user_height_input.pack()

user_Weight.pack()
user_weight_input.pack()
button.pack()
frame.pack()

#Metric bmi
frame1 = tk.Frame()

#header
label_header = tk.Label(text='Metric')

#User's Height
user_Height = tk.Label(text="Height in meters")
user_height_input = tk.Entry()

#user's Weight
user_weight_input = tk.Entry()
user_Weight = tk.Label(text="Weight")

#Creates the button
button = tk.Button(
    text="Convert",
    width=8,
    height=1,
    bg="white",
    fg="black",
)

#converts to BMI after button click, and prints to screen
def handle_click(event):
    height = user_height_input.get()
    weight = user_weight_input.get()
    sq = float(pow(float(height),2))
    BMI = float(weight)/float(sq)
    bmi = "{:.01f}".format(BMI)
    bmi_output = tk.Label(text=bmi)
    bmi_output.pack()

button.bind("<Button-1>", handle_click)

#Activates the code into GUI format
label_header.pack()

user_Height.pack()
user_height_input.pack()

user_Weight.pack()
user_weight_input.pack()
button.pack()
frame1.pack()


window.mainloop()
