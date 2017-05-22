store = []


def sort_by_last_letter(stringList):
    """
     Task: define a function that takes a list of strings as input parameter.
     Defines a local function that returns the last letter of a string.
    :param stringList: A list of strings
    :return: sorted list based on last letter
    """
    def get_last_letter(string):
        return string[-1] #slice last letter off

    #Hint: use the local function as lambda to sorted built in function
    store.append(get_last_letter)
    print(store)

    return sorted(stringList, key=get_last_letter)

def main():
    names = ["Hugo", "Maria", "Peter", "El Chapo",
             "Mario", "Juan"]
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
if __name__ == '__main__':
    main()
    exit(0)