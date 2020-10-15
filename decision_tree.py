from math import floor
from heapq import heappush, heappop


class Node:
    def __init__(self, chance, name="", ):
        self.name = name
        self.chance = chance
        self.rightNode = None
        self.leftNode = None

    def __str__(self):
        return f"chance: {self.chance}"

    def __lt__(self, other):
        return self.chance < other.chance



def build_decision_tree(decisions):
    heap = []
    for decision in decisions:
        heappush(heap, Node(decision[1], decision[0]))
    while len(heap) > 1:
        lowest, nlowest = heappop(heap), heappop(heap)
        node = Node(lowest.chance + nlowest.chance)
        node.rightNode = nlowest
        node.leftNode = lowest
        heappush(heap, node)
    return encoding(heap[0])


def encode_node(node, endcoded, dict):
    if node.leftNode is not None:
        encode_node(node.leftNode, endcoded + ["0"], dict)
        encode_node(node.rightNode, endcoded + ["1"], dict)
    else:
        dict[node.name] = "".join(endcoded)


def encoding(node):
    dict = {}
    encode_node(node, [], dict)
    return dict


tests = [
    ([("a", 0.5), ("b", 0.5)], 1),
    ([("a", 0.99), ("b", 0.01)], 1),
    ([("a", 0.5), ("b", 0.25), ("c", 0.25)], 1.5),
    ([("a", 0.33), ("b", 0.33), ("c", 0.34)], 1.66),
    ([("a", 0.25), ("b", 0.25), ("c", 0.25), ("d", 0.25)], 2),
    ([("a", 0.4), ("b", 0.2), ("c", 0.2), ("d", 0.2)], 2),
    ([("a", 0.3), ("b", 0.25), ("c", 0.25), ("d", 0.2)], 2),
    ([("a", 0.3), ("b", 0.2), ("c", 0.2), ("d", 0.2), ("e", 0.1)], 2.3),
]


def check_overlap_and_add_to_tree(tree, value):
    is_valid = len(tree) == 0
    for v in value:
        if v in tree:
            tree = tree[v]
        else:
            if len(tree) == 0 and not is_valid:
                return False
            tree[v] = {}
            tree = tree[v]
            is_valid = True

    return is_valid


def test_answer(student, test_case, correct_answer):
    if len(test_case) <= 20:
        feedback = "Feilet for tilfellet {:}.".format(
            test_case
        ) + " Ditt svar var {:}.\n".format(student)
    else:
        feedback = "Koden returnerte et galt svar:\n"

    if not isinstance(student, dict):
        feedback += "Funksjonen skal returnere en oppslagstabell (dictionary)."
        print(feedback)
        return False

    tree = {}
    expectance = 0
    for value, prob in test_case:
        if value not in student:
            feedback += "Beslutningen {:} er ikke med i treet.".format(value)
            print(feedback)
            return False

        encoding = student[value]
        if not isinstance(encoding, str) or not set(encoding) <= {"1", "0"}:
            feedback += (
                    "Hver beslutning skal ha en streng av nuller og "
                    + "enere knyttet til seg. "
            )
            print(feedback)
            return False

        if not check_overlap_and_add_to_tree(tree, encoding):
            feedback += "En av beslutningene er en internnode."
            print(feedback)
            return False

        expectance += prob * len(encoding)

    if expectance > correct_answer + 0.0000001:
        feedback += (
                "Beslutningstreet ditt er ikke optimalt. Det skulle "
                + "hatt en forventning på {:}".format(correct_answer)
                + " spørsmål, men har en forventning på "
                + str(expectance)
        )
        print(feedback)
        return False

    return True


passed = True
for test_case, answer in tests:
    student = build_decision_tree(test_case)
    passed &= test_answer(student, test_case, answer)

if passed:
    print("Passerte alle testene")
