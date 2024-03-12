from datetime import date
import re

# if filename is blank, returns default name else checks filename and returns an error or the filename (with .txt extension)
def filename_maker(filename):

    # default filename
    # YYYY_MM_DD_temperature_calculations
    if filename == "":
        
        filename_ok = ""
        date_part = get_date()
        filename = f"{date_part}_temperature_calculations"

    # checks filename only has letters/underscores
    else:
        filename_ok = check_filename(filename)

    if filename_ok == "":
        filename += ".txt"
    
    else:
        filename = filename_ok
    
    return filename

def get_date():
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    return f"{day}_{month}_{year}"

# checks filename only has letters, numbers, underscores. returns either "" if ok or the problem if error
def check_filename(filename):
    problem = ""

    # regular expression to check if filename is valid
    valid_char = "[A-Za-z0-9]"

    # iterates through filename and checks each letter
    for letter in filename:
        if re.match(valid_char, letter):
            continue
    
        elif letter == "":
            problem = "Sorry, no spaces allowed"

        else:
            problem = f"Sorry, no {letter}'s allowed"
        
        break
        
    if problem != "":
        problem = f"{problem}. use letters / numbers / underscores only"

    return problem
