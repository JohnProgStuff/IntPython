from functools import reduce
from pprint import pprint as pp

def count_words(doc):
    """
    dounts words in a document
    :param doc: file
    :return: a dictionary mapping words
    """
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)  # make all the uppercase -> lowercase.
    frequencies = {} # empty dict
    for word in normalized_doc.split():
        frequencies[word] = frequencies.get(word,0) + 1
    return frequencies

documents = [
    "It was the best of times. It was the worst of times",
    "I went to the woods because I was hunting",
    "I love to go to the theme park, Lagoon",
    "I really enjoy these wsu classes on programming."
]

counts = map(count_words, documents)

def combine_counts(d1, d2):
    """
    Combine iterable information
    :param d1: First dict
    :param d2: Second dict
    :return: Combine dict
    """
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d

def main():
    # c = count_words("It was the best of times, it was the worst of times.")
    # print(c)
    total_counts = reduce(combine_counts, counts)
    pp(total_counts)

if __name__ == '__main__':
    main()
    exit(0)