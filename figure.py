import math
class Line:
    __length=1
    def __init__(self, length_input):
        if isinstance(length_input, (int, float)) and length_input>0:
            self.__length=length_input
        else:
            self.__length=1
    def set_length(self, length_input):
        if isinstance(length_input, (int, float)) and length_input>0:
            self.__length=length_input
    def get_length(self):
        return self.__length
def area_square(line):
    if isinstance(line, Line):
        return line.get_length() ** 2
    else:
        return 0
def area_circle(line):
    if isinstance(line, Line):
        return math.pi * line.get_length() ** 2 
    else:
        return 0
def area_regular_triangle(line):
    if isinstance(line, Line):
        return line.get_length() ** 2 * math.sqrt(3) / 4
    else:
        return 0