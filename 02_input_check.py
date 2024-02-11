
def temp_check(min_value):
    error = "Please Enter a Number That is More Than {}".format(min_value)

    try:
        response = float(input("Choose a Number: "))

        if response < min_value:
            print(error)

        else:
            return response

    except ValueError:
        print(error)

# main routine

while True:
    to_check = temp_check(-273)
    print("success")
