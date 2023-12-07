""" ----------------------------------SYSTEMS ENGINEERING 2024  - Turing Machine ------------------------------------"""
"""-----------------------------------------------ALI BDEIR----------------------------------------------------------"""
"""-----------------------------------Interface Code for automating the machine--------------------------------------"""

from tkinter import *
from tkinter import IntVar
import time
from tkinter import messagebox

# *********************************************************************************************************************
""" Define Constants"""
BACKGROUND_COLOR = "#B1DDC6"
timer_running = False
start_time = 0

# *********************************************************************************************************************
"""Define the main window"""
window = Tk()
window.title("TuringAFIS Interface")
window.configure(padx=15, pady=15, background=BACKGROUND_COLOR)

# *********************************************************************************************************************
"""Set up the introductory statement"""
welcome_label = Label(text="Welcome to TuringAFIS machine INTERFACE.\n In order "
                           "to control the machine , please press on the buttons below.\n\n"
                           "In order to run your robot please make sure to check the conditions below!",
                      font=("Helvetica", 12, "bold"),
                      highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
welcome_label.grid(row=0, column=0, columnspan=7, pady=40)
# *********************************************************************************************************************
"""Set up the check boxes"""
checkbox_var = IntVar()
checkbox = Checkbutton(text="Check for Batteries", font=("Helvetica", 12, "bold"), variable=checkbox_var, pady=10,
                       highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
checkbox.grid(row=1, column=0, columnspan=3)

checkbox_var1 = IntVar()
checkbox1 = Checkbutton(text="Check for the Code", font=("Helvetica", 12, "bold"), variable=checkbox_var1, pady=10,
                        highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
checkbox1.grid(row=1, column=3, columnspan=6)

checkbox_var2 = IntVar()
checkbox2 = Checkbutton(text="Place the robot at the needed position", font=("Helvetica", 12, "bold"),
                        variable=checkbox_var2, pady=10,
                        highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
checkbox2.grid(row=2, column=0, columnspan=3)

checkbox_var3 = IntVar()
checkbox3 = Checkbutton(text="Tokens are placed", font=("Helvetica", 12, "bold"), variable=checkbox_var3,
                        highlightthickness=0, borderwidth=0, background=BACKGROUND_COLOR)
checkbox3.grid(row=2, column=3, columnspan=6)


# ***********************************************************************************************************************

def open_dialog():
    root = Toplevel()
    root.title("TuringAFIS Interface")
    root.configure(pady=10, padx=10, background="green")

    background_image = PhotoImage(file="bg.png")
    background_label = Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Cover the entire window
    background_label.image = background_image
    # ******************************************************************************************************************
    welcome_label1 = Label(root, text="Welcome to TuringAFIS machine INTERFACE.\n In order "
                                      "to control the machine , please press on the buttons below.\n\n",
                           font=("Helvetica", 12, "bold"), highlightthickness=0, borderwidth=0, background="green",
                           pady=15)
    welcome_label1.grid(row=1, column=0, columnspan=7)

    status = Label(root, text="Robot Status ", font=("Helvetica", 12, "bold"), background="white")
    status.grid(row=5, column=6)
    # ******************************************************************************************************************
    """Create the status Indicator"""

    def update_circle_color(robot_status):
        global timer_running, start_time

        if robot_status == "on":
            canvas.itemconfig(circle, fill="green")
            if not timer_running:
                timer_running = True
                start_time = time.time()
        elif robot_status == "off":
            canvas.itemconfig(circle, fill="red")
            if timer_running:
                timer_running = False

    def update_timer_label():
        current_time = int(time.time() - start_time)
        timer_label.config(text=f"Timer: {current_time} seconds")
        if timer_running:
            timer_label.after(1000, update_timer_label)

    def turn_robot_on():
        update_circle_color("on")
        update_timer_label()

    def reset_timer():
        global start_time
        start_time = time.time()
        update_timer_label()

    def turn_robot_off():
        update_circle_color("off")

    timer_label = Label(root, text="Timer: 0 seconds", font=("Helvetica", 12, "bold"), background="white")
    timer_label.grid(row=4, column=0, columnspan=1)
    canvas = Canvas(root, width=50, height=50, background="white")
    canvas.grid(row=6, column=6, pady=5)
    circle = canvas.create_oval(5, 5, 50, 50, fill="red")
    reset_image = PhotoImage(file="reset.png")
    reset_button = Button(root, image=reset_image, command=reset_timer, font=("Helvetica", 12, "bold"),
                          highlightthickness=0)
    reset_button.grid(row=5, column=0)
    # ******************************************************************************************************************
    # Set up the buttons
    start_image = PhotoImage(file="right.png")
    start_button = Button(root, image=start_image, highlightthickness=0, command=turn_robot_on,
                          font=("Helvetica", 12, "bold"), borderwidth=0)
    start_button.grid(row=3, column=0, pady=25)

    stop_image = PhotoImage(file="wrong.png")
    stop_button = Button(root, image=stop_image, highlightthickness=0, command=turn_robot_off,
                         font=("Helvetica", 12, "bold"), borderwidth=0)
    stop_button.grid(row=3, column=3, pady=25)

    emergency_icon = PhotoImage(file="emergency.png")
    emergency_button = Button(root, image=emergency_icon, highlightthickness=0, command=turn_robot_off,
                              font=("Helvetica", 12, "bold"), borderwidth=0)
    emergency_button.grid(row=3, column=6, pady=25)
    # ******************************************************************************************************************
    root.mainloop()


# ***********************************************************************************************************************
def get_checkbox_value():
    value1 = checkbox_var.get()
    value2 = checkbox_var1.get()
    value3 = checkbox_var2.get()
    value4 = checkbox_var3.get()

    if value1 == 1 and value2 == 1 and value3 == 1 and value4 == 1:
        checkbox_var.set(0)
        checkbox_var1.set(0)
        checkbox_var2.set(0)
        checkbox_var3.set(0)
        open_dialog()
    else:
        messagebox.showerror(message="Unchecked Box!", title="Warning!")
        print("Checkbox is unchecked")


# ***********************************************************************************************************************
next_image = PhotoImage(file="next.png")
next_button = Button(image=next_image, highlightthickness=0, borderwidth=0, command=get_checkbox_value,
                     bg=BACKGROUND_COLOR)
next_button.grid(row=4, column=5, pady=40)
# ***********************************************************************************************************************
window.mainloop()
