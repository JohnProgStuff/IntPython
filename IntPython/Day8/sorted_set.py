from bisect import bisect_left


class SortedSet():
    def __init__(self, items=None):
        """
        Return a sorted set
        :param items: sequence of values
        :returns: sorted sequence of values
        # we use None because it's not good convention to pass a mutable object into items.
        """
        # sorted(): returns a list, regardless of which iterable object you pass.
        self._items = sorted(set(items)) if items is not None else []
        # set() only allows unique items.

    def __contains__(self, item):
        index = bisect_left(self._items, item)
        return (index != len(self._items)) and self._items[index] == item

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)



if __name__ == '__main__':
    exit(0)