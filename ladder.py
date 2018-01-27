# https://www.coursera.org/learn/programming-in-python/programming/Lg9Hb/risuiem-liestnitsu
import sys

def print_ladder(size):
    if not size.isdigit():
        print("Bad input size")
        return

    size = int(size) + 1
    
    for i in range(1, size, 1):
        spaces = " " * (size - i)
        step = "#" * i
        print(spaces + step)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        size = sys.argv[1]
        print_ladder(size)
    else:
        print("Expected 1 input number as parameter")
     
    
