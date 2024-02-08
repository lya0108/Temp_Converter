# imports
import tkinter as tk
from tkinter import *

class converter:
    def __init__(self):

        # GUi frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "18", "bold"))
        self.temp_heading.grid(row=0, column=0)

        instructions = "Please Enter a Temperature Below and Then Press One of The Buttons to Convert it From Centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left")
        self.temp_instructions.grid(row=1, column=0)

# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("310x512")
    converter()
    root.mainloop()