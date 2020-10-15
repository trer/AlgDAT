import random


# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
# random.seed(123)


def naive_count(dna, segments):
    counter = 0
    for segment in segments:
        for i in range(len(dna) - len(segment) + 1):
            if dna[i: i + len(segment)] == segment:
                counter += 1
    return counter


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

    def __str__(self):
        return (
                f"{{count: {self.count}, children: {{"
                + ", ".join(
            [f"'{c}': {node}" for c, node in self.children.items()]
        )
                + "}"
        )


def searchTree(root, dna, prev_dna):
    if dna in prev_dna:
        return prev_dna[dna]
    count = 0
    # O(d)
    for i in range(len(dna)):
        if dna[i] in root['children']:
            root = root['children'][dna[i]]
            count += root['count']
        else:
            prev_dna[dna] = count
            return count
    prev_dna[dna] = count
    return count


def buildTree(dna_sequences):
    # dicts to update
    root = {'children': {},
            'count': 0}
    longest_subsequence = 0

    # O(k*d)
    # O(k)
    for dna in dna_sequences:
        n = len(dna)
        if n > longest_subsequence:
            longest_subsequence = n
        # O(d)
        place_string_in_tree(root, dna)
    return root, longest_subsequence


# O(d)
def place_string_in_tree(parent, dna):
    n = len(dna)
    k = 0
    # O(d)
    for i in range(n):
        if dna[i] in parent['children']:
            parent = parent['children'][dna[i]]
            k += 1
        else:
            break
    if k < n:
        # O(d-i)
        for j in range(k, n):
            # dicts to update
            parent['children'].update({dna[j]: {'children': {},
                                                     'count': 0}})
            parent = parent['children'][dna[j]]
    parent['count'] += 1


def string_match(dna, segments):
    dict = {}
    counter = 0
    for segment in segments:
        if segment in dict:
            counter += dict[segment]
        else:
            count = 0
            i = dna.find(segment)
            while i != -1:
                count += 1
                i = dna.find(segment, i+1)
            counter += count
            dict[segment] = count
    return counter
    # O(d*k)
    root, longest_subsequence = buildTree(segments)
    # O(n*searchTree)
    # O(n)
    prev_dna = {}
    for i in range(len(dna)):
        # O(d)
        counter += searchTree(root, dna[i:i + min(len(dna) - i, longest_subsequence)], prev_dna)
    return counter


def generate_match_tests():
    # Custom made match tests
    tests = [
        (("A", []), 0),
        (("AAAA", ["A"]), 4),
        (("ACTTACTGG", ["A", "ACT", "GG"]), 5),
        ((20 * "A", ["A"]), 20),
        ((20 * "A", ["AA"]), 19),
        ((20 * "A", ["A", "A"]), 40),
        ((20 * "A", ["A", "AA"]), 39),
        ((10 * "AB", ["AB"]), 10),
        ((10 * "AB", ["A", "AB"]), 20),
        ((10 * "AB", ["A", "B"]), 20),
    ]
    for test in tests:
        yield test

    # Some small random rests
    for i in range(2000):
        d = "".join(
            random.choices(["A", "G", "T", "C"], k=random.randint(0, 200))
        )
        e = [
            "".join(
                random.choices(["A", "G", "T", "C"], k=random.randint(1, 20))
            )
            for i in range(random.randint(0, 200))
        ]
        answer = naive_count(d, e)
        yield ((d, e), answer)


for test_case, answer in generate_match_tests():
    dna, segments = test_case
    student = string_match(dna, segments)
    if student != answer:
        print(
            "Input: (dna={:}, segments={:}) ".format(dna, segments)
            + "Ditt svar: {:} Riktig: {:}".format(student, answer)
        )
        break
