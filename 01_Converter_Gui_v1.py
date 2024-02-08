# imports
import tkinter as tk
from tkinter import *

def num_check():
    rafa

class converter:
    def __init__(self):

        # font for all buttons: Arial size 20 bold, with white text
        button_font = ("Arial", "20", "bold")
        button_fg = "#FFFFFF"

        # GUi frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "18", "bold"))
        self.temp_heading.grid(row=0, column=0)

        instructions = "Please Enter a Temperature Below and Then Press One of The Buttons to Convert it From Centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left")
        self.temp_instructions.grid(row=1, column=0)

        self.temp_entry = Entry(self.temp_frame)
        self.temp_entry.grid(row=2, column=0, padx=10, pady=10)

        self.temp_error = Label(self.temp_frame, text="Please enter a number", fg="#9C0000")
        self.temp_error.grid(row=3, column=0, padx=10, pady=10)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4, column=0, padx=10, pady=10)

        self.temp_celsius_button = Button(self.button_frame, text="To Celsius °C", font=button_font, bg="#00b0b0", fg=button_fg, width=14)
        self.temp_celsius_button.grid(row=0, column=0)

        self.temp_fahrenheit_button = Button(self.button_frame, text="To Fahrenheit °F", font=button_font, bg="#d98a00", fg=button_fg, width=14)
        self.temp_fahrenheit_button.grid(row=0, column=1)

        self.temp_Help_button = Button(self.button_frame, text="Help / Info", font=button_font, bg="#a30000", fg=button_fg, width=14)
        self.temp_Help_button.grid(row=1, column=0)

        self.temp_History_button = Button(self.button_frame, text="History / Export", font=button_font, bg="#00a300", fg=button_fg, width=14, state=DISABLED)
        self.temp_History_button.grid(row=1, column=1)

# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("540x512")
    converter()
    root.mainloop()