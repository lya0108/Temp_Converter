import math

def round_temp(n):
     if n - math.floor(n)< 0.5:
        return math.floor(n)
     return math.ceil(n)

while True:
    question = float(input("num: "))
    question = round_temp(question)
    print(question)