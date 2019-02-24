# Emergency Minutemen Hackathon Project - 2/23/19
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# Commands
def start():
    emergency = situation.get()
    if emergency == "Hurricane":
        Hurricane()
        destroy_option()
        destroy_start_button()
    elif emergency == "Earthquake":
        Earthquake()
    elif emergency == "Terrorist Attack":
        Terrorist()
    elif emergency == "Fire":
        Fire()
    elif emergency == "AMBER":
        AMBER()
        destroy_start_button()
        destroy_option()


def go_back():
    for widget in frame.winfo_children():
        widget.destroy()
    Reset()


def destroy_start_button():
    start_button.destroy()


def destroy_option():
    option.destroy()


def amber_preview():
    window = Toplevel(root)


# Hurricane
class Hurricane:
    def __init__(self):
        self.header = ttk.Label(frame, text="Hurricane Emergency", font=("Arial", 30))
        self.header.grid(column=3, row=0)

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


# AMBER
class AMBER:
    def __init__(self):
        self.header = ttk.Label(frame, text="AMBER Emergency", font=("Arial", 30))
        self.header.grid(row=0, column=4, columnspan=4)

        self.go_back = ttk.Button(frame, text="← Go Back", command=go_back).grid(row=0, column=0)

        self.name_label = ttk.Label(frame, text="Name:")
        self.name_label.grid(row=2, column=2)
        self.name_entry = ttk.Entry(frame).grid(row=2, column=3)

        self.age_label = ttk.Label(frame, text="Age:")
        self.age_label.grid(row=2, column=4)
        self.age_entry = ttk.Entry(frame).grid(row=2, column=5)

        self.gender_label = ttk.Label(frame, text="Gender:")
        self.gender_label.grid(row=2, column=6)
        self.gender_entry = ttk.Entry(frame).grid(row=2, column=7)

        self.height_label = ttk.Label(frame, text="Height:")
        self.height_label.grid(row=2, column=8)
        self.height_entry = ttk.Entry(frame).grid(row=2, column=9)

        self.hair_label = ttk.Label(frame, text="Hair Color:")
        self.hair_label.grid(row=3, column=2)
        self.hair_entry = ttk.Entry(frame).grid(row=3, column=3)

        self.eye_label = ttk.Label(frame, text="Eye Color:")
        self.eye_label.grid(row=3, column=4)
        self.eye_entry = ttk.Entry(frame).grid(row=3, column=5)

        self.clothes_label = ttk.Label(frame, text="Clothes:")
        self.clothes_label.grid(row=3, column=6)
        self.clothes_entry = ttk.Entry(frame).grid(row=3, column=7)

        self.area_label = ttk.Label(frame, text="Location:")
        self.area_label.grid(row=3, column=8)
        self.area_entry = ttk.Entry(frame).grid(row=3, column=9)

        self.make_label = ttk.Label(frame, text="Car Make:")
        self.make_label.grid(row=4, column=2)
        self.make_entry = ttk.Entry(frame).grid(row=4, column=3)

        self.model_label = ttk.Label(frame, text="Car Model:")
        self.model_label.grid(row=4, column=4)
        self.model_entry = ttk.Entry(frame).grid(row=4, column=5)

        self.car_year_label = ttk.Label(frame, text="Car Year:")
        self.car_year_label.grid(row=4, column=6)
        self.car_year_entry = ttk.Entry(frame).grid(row=4, column=7)

        self.car_color_label = ttk.Label(frame, text="Car Color:")
        self.car_color_label.grid(row=4, column=8)
        self.car_color_entry = ttk.Entry(frame).grid(row=4, column=9)

        self.preview = ttk.Button(frame, text="Preview", command=amber_preview)
        self.preview.grid(row=5, column=4, columnspan=2)

        self.send = ttk.Button(frame, text="Send Message")
        self.send.grid(row=5, column=6, columnspan=2)


# Earthquake
class Earthquake:
    def __init__(self):
        self.blank = ttk.Label(frame)


# Terrorist Attack
class Terrorist:
    def __init__(self):
        self.blank = ttk.Label(frame)


# Fire
class Fire:
    def __init__(self):
        self.blank = ttk.Label(frame)


# Reset
class Reset:
    choices = ["What Is The Emergency?", "Hurricane", "AMBER", "Earthquake", "Terrorist Attack",
               "Fire"]

    def __init__(self):
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
choices = ["What Is The Emergency?", "Hurricane", "AMBER", "Earthquake", "Terrorist Attack", "Fire"]
option = ttk.OptionMenu(frame, situation, *choices)
option.grid(column=2, columnspan=2, pady=10)

# Start Button
start_button = ttk.Button(frame, text="Start", command=start)
start_button.grid(row=1, column=2, columnspan=2)

# Map
PIL_map = Image.open("nycmap.png")
nyc_map = ImageTk.PhotoImage(PIL_map)

root.mainloop()
