import math

class Point:
    """
    Represents a point in 2-D geometric space
    """
    def __init__(self, x=0, y=0):
        """
        Initializes the position of a new point.
        If they are not specified, the point defaults to the origin
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the point to the origin in 2D space
        """
        self.move(0,0)

    def move(self, x, y):
        """
        Move a Point to a new location in 2D space
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def calc_dist(self, point2):
        """
        Calculate the distance from current point to a second point passed as parameter.
        This function uses Pythagorean Theorem to calculate the distance between the two points
        :param point2: second point to calculate distance
        :return: The distance between two points(float)
        """
        print(math.sqrt((point2.x - self.x)**2+(point2.y - self.y)**2))




def main():
    """

    """
    p1 = Point()
    print(p1.x, p1.y)
    p2 = Point(5, 8)
    print(p2.x, p2.y)
    p2.move(9, 10)
    print(p2.x, p2.y)

    print(p1.calc_dist(p2))
    assert(p2.calc_dist(p1) == p1.calc_dist(p2))

    # p2.reset()
    # print(p2.x, p2.y)


if __name__ == '__main__':
    main()
    exit(0)