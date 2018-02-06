# https://www.coursera.org/learn/programming-in-python/programming/Mcs6i/summa-tsifr-v-strokie
import sys
from functools import reduce

def get_string_digit_sum(digit_string):
    digit_string = str(digit_string)
    if not digit_string.isdigit():
        print("Bad input number")
        return

    return reduce(lambda x,y: int(x) + int(y), digit_string)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        digit_string = sys.argv[1]
        print(get_string_digit_sum(digit_string))
    else:
        print("Expected 1 input number as parameter")
     
    
