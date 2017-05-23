import math

def triangle_area(a, b, c):
    p = (a + b + c)/2
    a = math.sqrt(p * (p-a) * (p-b) * (p-c))

    return a


def main():
    # this will work well for side lengths that represent a legitimate triangle
    print(triangle_area(3, 4, 5))
    print(triangle_area(3, 4, 10)) # valueError: math domain error

if __name__ == '__main__':
    main()
    exit(0)


    #icarus.cs.weber.edu/~hvalle/interPython/Day5.zip