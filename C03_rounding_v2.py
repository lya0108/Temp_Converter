import math

def round_temp(n):
     n = math.floor(n + 0.5)
     return n

while True:
    question = float(input("num: "))
    question = round_temp(question)
    print(question)