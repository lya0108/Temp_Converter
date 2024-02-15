def to_celsius(to_convert):
    answer = (to_convert - 32) * 5/9
    return answer

def to_fahrenheit(to_convert):
    answer = (to_convert * 9/5) + 32
    return answer

to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    print("{} C is {:.0f} F\n".format(item, to_fahrenheit(item)))

for item in to_c_test:
    print("{} f is {:.0f} c\n".format(item, to_celsius(item)))