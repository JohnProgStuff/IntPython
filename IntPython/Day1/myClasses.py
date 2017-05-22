#  use CamelCase for class names
class MyFirstClass:  # we are going to follow the PEP8 coding style
    pass


class Point:
    def reset(self):
        self.x = 0
        self.y = 0


def main():
    p1 = Point()
    # <object>.<attribute> = <value> (dot notation)
    p1.x = 5
    p1.y = 4
    print("point:",p1.x, p1.y)
    p1.reset()
    print("point:",p1.x, p1.y)


if __name__ == "__main__":
    main()
