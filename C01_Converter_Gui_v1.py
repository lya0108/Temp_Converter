# imports
import tkinter as tk
from tkinter import *
import math

class converter:
    def __init__(self):

        # initialise variables (like feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # font for all buttons: Arial size 20 bold, with white text
        button_font = ("Arial", "20", "bold")
        button_fg = "#FFFFFF"

        # GUi frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "18", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Please Enter a Temperature Below and Then Press One of The Buttons to Convert it From Centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame, text=instructions, wrap=250, width=40, justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "15"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        self.output_label = Label(self.temp_frame, text="")
        self.output_label.grid(row=3, padx=5, pady=5)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4, padx=10, pady=10)

        self.temp_celsius_button = Button(self.button_frame, text="To Celsius °C", font=button_font, bg="#00b0b0", fg=button_fg, width=14, command=lambda: self.temp_convert(-459))
        self.temp_celsius_button.grid(row=0, column=0)

        self.temp_fahrenheit_button = Button(self.button_frame, text="To Fahrenheit °F", font=button_font, bg="#d98a00", fg=button_fg, width=14, command=lambda: self.temp_convert(-273))
        self.temp_fahrenheit_button.grid(row=0, column=1)

        self.temp_help_button = Button(self.button_frame, text="Help / Info", font=button_font, bg="#a30000", fg=button_fg, width=14)
        self.temp_help_button.grid(row=1, column=0, pady=5)

        self.temp_history_button = Button(self.button_frame, text="History / Export", font=button_font, bg="#00a300", fg=button_fg, width=14, state=DISABLED)
        self.temp_history_button.grid(row=1, column=1, pady=5)

    # checks user input is valid and converts temperature
    def check_temp(self, min_value):

        has_error = "no"
        error = "Please Enter a Number That is More Than {}".format(min_value)

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # set var_has_error so that entry box and labels can be correctly formatted by formatting function
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        else:
            # set to "no" in case of previous errors
            self.var_has_error.set("no")

            # return number to be converted and enable history button
            self.temp_history_button.config(state=NORMAL)
            return response

    @staticmethod
    def round_temp(n):
        n = math.floor(n + 0.5)
        return n

    # check temperature is valid and convert it
    def temp_convert(self, min_value):
        to_convert = self.check_temp(min_value)

        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        # convert to celsius
        elif min_value == -459:
            # do calculation
            answer = (to_convert - 32) * 5/9
            from_to = "{} F° is {} C°"

        # convert to fahrenheit
        else:
            answer = (to_convert * 9/5) + 32
            from_to = "{} C° is {} F°"

        if set_feedback == "yes":
            to_convert = self.round_temp(to_convert)
            answer = self.round_temp(answer)

            # create user output and add to calculation history
            feedback = from_to.format(to_convert, answer)
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

        self.output_answer()   

    # shows user output and clears entry widget ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red rext, pink entry box
            self.output_label.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")
        
        else:
            self.output_label.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)


# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("540x512")
    converter()
    root.mainloop()