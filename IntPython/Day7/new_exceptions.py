import math
import traceback
import sys


class TriangleError(Exception):
    """
    Everything is inherited from Exception class
        dunder-init()
        dunder-str()
        dunder-repr()
        ...
    """
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)  # tuples cannot be changed once defined

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

def triangle_area(a, b, c):
    sides = sorted((a, b, c)) #sorted takes a tuple or list of arguments
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    p = (a + b + c)/2
    a = math.sqrt(p * (p-a) * (p-b) * (p-c))

    return a




def main():

    #try this
    try:
        a = triangle_area(3,4,10)
        print(a)
    except TriangleError as e:
        # you cannot print to stdin, so this causes another exception to occur during the previous exception handling
        # cause an unsupported operation experience by trying to print to the standard in stream instead of stdout.
        print(e, file=sys.stdin)  #Implicit Chaining
    # this will work well for side lengths that represent a legitimate triangle
    # print(triangle_area(3, 4, 5))
    # print(triangle_area(3, 4, 10)) # valueError: math domain error

class InclinationError(Exception):
    pass


def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy/dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e

def test_inclination():
    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)
        # traceback.print_tb(e.__traceback__)
        
        # Don't keep a reference to dunder-traceback
        # beyond the scope of the except block
        s = traceback.format_tb(e.__traceback__)
        print(s)


if __name__ == '__main__':
    #main()
    #print(inclination(3,5))
    #print(inclination(0, 5))
    test_inclination()

    exit(0)


    #icarus.cs.weber.edu/~hvalle/interPython/Day5.zip