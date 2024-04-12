import math


def calculate_power(num):
    square=math.pow(num,2)
    cube=math.pow(num,3)
    return square,cube


number=float(input("Enter the number:"))

square_result,cube_result=calculate_power(number)



print(f"The result is :{square_result} and {cube_result}")