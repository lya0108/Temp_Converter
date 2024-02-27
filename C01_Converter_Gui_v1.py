# imports
import tkinter as tk
from tkinter import *
import math
from functools import partial # prevents unwanted windows

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

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter", font=("Arial", "30", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Please Enter a Temperature Below and Then Press One of The Buttons to Convert it From Centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame, text=instructions, font=("Arial", "12"), wrap=300, justify="left")
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

        self.temp_help_button = Button(self.button_frame, text="Help / Info", font=button_font, bg="#a30000", fg=button_fg, width=14, command=self.to_help)
        self.temp_help_button.grid(row=1, column=0, pady=5)

        self.temp_history_button = Button(self.button_frame, text="History / Export", font=button_font, bg="#00a300", fg=button_fg, width=14, state=DISABLED, command=lambda: self.to_history(self.all_calcs))
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
 
    def to_help(self):
        DisplayHelp(self)

    def to_history(self):
        HistoryExport(self)

class DisplayHelp:
    def __init__(self, partner):
        background = "#ffe6cc"

        # setup dialogue box
        self.help_box = Toplevel()

        # diasble help button
        partner.temp_help_button.config(state=DISABLED)

        # if user closes the help frame 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW", partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame, text="Help / Info", font=("Arial", "30", "bold"), bg=background)
        self.help_heading.grid(row=0)

        helpinfo = "In Box Enter Number.\n\nClick Celsius to Convert From Fahrenheit to Celsius and Vice Versa\n\nCelsius Cannot be Below -459 and Fahrenheit Cannot be Below -273\n\nTo See Your Calculation History and Export it to Text Press the History Button"

        self.help_info = Label(self.help_frame, text=helpinfo, font=("Arial", "12"), bg=background, wrap=300, justify=CENTER)
        self.help_info.grid(row=1, padx=10, pady=10)

        self.return_button = Button(self.help_frame, text="Return", font=("Arial", "15", "bold"), bg="#a30000", fg="white", width=10, command=partial(self.close_help, partner))
        self.return_button.grid(row=2, pady=10)

    # closes help dialogue
    def close_help(self, partner):
        # set help button back to normal
        partner.temp_help_button.config(state=NORMAL)
        self.help_box.destroy()

class HistoryExport:
    def __init__(self, partner, calc_list):

        # set max # of calcs to 5
        # can be changed to show more or less if we want
        max_calcs = 5
        self.var_max_calcs = IntVar()
        self.var_max_calcs.set(max_calcs)

        calc_string_text = self.get_calc_string(calc_list)

        # setup dialogue box
        self.history_box = Toplevel()

        # disable history button
        partner.temp_history_button.config(state=DISABLED)

        # if user closes the history frame 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, height=200)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, text="History / Export", font=("Arial", "30", "bold"))
        self.history_heading_label.grid(row=0)

        histinstructions = "Below are Your Recent Calculations\nShowing 3/3 Calculations.\nAll Calculations are Shown to The Nearest Degree"
        self.hist_instructions = Label(self.history_frame, text=histinstructions, font=("Arial", "12"), wraplength=300, justify=CENTER)
        self.hist_instructions.grid(row=1)

        self.all_calcs = Label(self.history_frame, text="Calculations Go here", font=("Arial", "12"), bg="#ffe6cc", padx=10, pady=10, justify=CENTER)
        self.all_calcs.grid(row=2)

        savetext = "Either Choose a Custom File Name (and push\n<Export>) or Simply Push <Export> to Save Your\nCalculations in a Text File. If the\n Filename Already Exists, it Will be Overwritten"
        self.save_text = Label(self.history_frame, text=savetext, font=("Arial", "12"), wrap=300, padx=10, pady=10, justify=CENTER)
        self.save_text.grid(row=3)

        self.filename_entry = Entry(self.history_frame, font=("Arial", "14"), bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)

        self.filename_error = Label(self.history_frame, text="Filename Error Goes Here", font=("Arial", "12", "bold"), fg="#9c0000")
        self.filename_error.grid(row=5)

        self.returbut_frame = Frame(self.history_frame)
        self.returbut_frame.grid(row=6)
        
        self.export_button = Button(self.returbut_frame, font=("Arial", "15", "bold"), bg="#004c99", fg="white", width=12, state=DISABLED, command=lambda: setiojtigigweiugfwhgiuwfhwiufwhiufhiuwhiuf)
        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.return_button = Button(self.returbut_frame, text="Return", font=("Arial", "15", "bold"), bg="#666666", fg="white", command=partial(self.close_history, partner)) 
        self.return_button.grid(row=0, column=1, padx=10, pady=10)

    # closes history dialogue
    def close_history(self, partner):
        # put history button back to normal
        partner.temp_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temperature Converter")
    root.geometry("540x512")
    converter()
    root.mainloop()