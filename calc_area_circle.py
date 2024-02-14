import math

#Formula for area of a square: side_legth **2
def calc_area_square(side_length):
    return side_length ** 2

def calc_area_circle(radius):
    if not isinstance(radius, (float, int)):
        raise TypeError(f'Radius is {radius} but should be a number')
    if radius < 0:
        raise ValueError(f'Radius is {radius} but must be positive')
    return math.pi * radius ** 2

def hello_world():
    print('Hello Melissa')
#print(f'calc_area_square(2) = {calc_area_square(2)}')
#input_number = 2
#output_number = calc_area_square(input_number)
#print(f'calc_area_square({input_number}) = {output_number}')
