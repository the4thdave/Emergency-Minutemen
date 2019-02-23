# Emergency Minutemen Hackathon Project - 2/23/19
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Commands
def start():
    emergency = situation.get()
    if emergency == "Hurricane":
        Hurricane(root)
    elif emergency == "Earthquake":
        Earthquake(root)
    elif emergency == "Terrorist Attack":
        Terrorist(root)
    elif emergency == "Fire":
        Fire(root)


def go_back():
    for widget in frame.winfo_children():
        widget.destroy()
    Reset(root)


# Hurricane
class Hurricane:
    def __init__(self, root):
        self.category_label = ttk.Label(frame, text="Category:", font=("Arial", 30))
        self.category_label.grid(row=2, column=0)

        self.category = ttk.Entry(frame, width=10)
        self.category.grid(row=2, column=1)

        self.time_label = ttk.Label(frame, text="Time to Arrival:", font=("Arial", 30))
        self.time_label.grid(row=2, column=2)

        self.arrival_time = ttk.Entry(frame, width=10)
        self.arrival_time.grid(row=2, column=3)

        self.map = ttk.Label(frame, image=nyc_map)
        self.map.grid(row=2, column=4, rowspan=3, columnspan=3, padx=5)

        self.msg = ttk.Label(frame, text="Message:", font=("Arial", 30))
        self.msg.grid(row=3, column=0)

        self.message = Text(frame)
        self.message.config(width=30, height=4)
        self.message.grid(row=3, column=1)

        self.preview = ttk.Button(frame, text="Preview")
        self.preview.grid(row=3, column=2)

        self.send_message = ttk.Button(frame, text="Send Message")
        self.send_message.grid(row=3, column=3)

        self.go_back = ttk.Button(frame, text="← Go Back", command=go_back).grid(row=0, column=0)


# Earthquake
class Earthquake:
    def __init__(self, root):
            self.blank = Label(frame)


# Terrorist Attack
class Terrorist:
    def __init__(self, root):
        self.blank = Label(frame)


# Fire
class Fire:
    def __init__(self, root):
        self.blank = Label(frame)


# Reset
class Reset:
    choices = ["What Is The Emergency?", "Hurricane", "Earthquake", "Terrorist Attack", "Fire"]

    def __init__(self, root):
        self.option = ttk.OptionMenu(frame, situation, *choices)
        self.option.grid(column=2, columnspan=2, pady=10)

        self.start_button = ttk.Button(frame, text="Start", command=start)
        self.start_button.grid(row=1, column=2, columnspan=2)


root = Tk()
root.title("Emergency Protocol")

# Frame
frame = ttk.Frame(root, padding="100 100 150 150")
frame.grid(row=0, column=0)

# Option Menu
situation = StringVar()
choices = ["What Is The Emergency?", "Hurricane", "Earthquake", "Terrorist Attack", "Fire"]
option = ttk.OptionMenu(frame, situation, *choices)
option.grid(column=2, columnspan=2, pady=10)

# Start Button
start_button = ttk.Button(frame, text="Start", command=start)
start_button.grid(row=1, column=2, columnspan=2)

PIL_map = Image.open("nycmap.png")
nyc_map = ImageTk.PhotoImage(PIL_map)

root.mainloop()
