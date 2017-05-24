from pprint import pprint as pp

def test_comprehensions():
    values = [x / (x - y) for x in range(100) if x > 50
              for y in range(100) if x-y != 0]
    pp(values)
    return values

def test_comprehensions_loop():
    values = []
    for x in range(100):
        if x > 50:
            for y in range(100):
                if x-y != 0:
                    values.append(x/(x-y))
    pp(values)
    # assert test_comprehensions() == values, 'Not equal'

def main():
    test_comprehensions_loop()
    # test_comprehensions()


if __name__ == '__main__':
    main()
    exit(0)