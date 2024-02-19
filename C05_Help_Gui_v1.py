import tkinter as tk
from tkinter import *

class help:
    def __init__(self):

        # font for all buttons: Arial size 20 bold, with white text
        button_font = ("Arial", "20", "bold")
        button_fg = "#FFFFFF"

        # GUi frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=30, pady=30)
        self.button_frame.grid(row=0)

        self.to_help_button = Button(self.button_frame, text="Help / Info", font=button_font, bg="#a30000", fg=button_fg, width=12, command=self.to_help)
        self.to_help_button.grid(row=1, column=0,padx=5, pady=5)

    @staticmethod
    def to_help():
        DisplayHelp()

class DisplayHelp:
    def __init__(self):
        background = "#ffe6cc"

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text="Help / Info", font=("Arial", "30", "bold"), bg=background)
        self.help_heading.grid(row=0)

        helpinfo = "In Box Enter Number.\n\nClick Celsius to Convert From Fahrenheit to Celsius and Vice Versa\n\nCelsius Cannot be Below -459 and Fahrenheit Cannot be Below -273"

        self.help_info = Label(self.help_frame, text=helpinfo, font=("Arial", "12"), bg=background, wrap=300, justify=CENTER)
        self.help_info.grid(row=1, padx=10, pady=10)

        self.return_button = Button(self.help_frame, text="Return", font=("Arial", "15", "bold"), bg="#a30000", fg="white", width=10)
        self.return_button.grid(row=2, pady=10)


# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Help / Info")
    help()
    root.mainloop()