import random
import uuid
from math import log, ceil
from heapq import heapify, heappush, heappop


class TestNode:
    def __init__(self, i):
        self.function = i
        self.true = None
        self.false = None


class LeafNode:
    def __init__(self, name):
        self.name = name


class BuildNode:
    def __init__(self, test, decisions, total_decisions):
        self.decisions = decisions
        self.total_decisions = total_decisions
        self.chance = sum([decision[1] for decision in decisions])
        if 0 < len(decisions) < total_decisions:
            if self.chance / (1 + log(len(decisions), 2)) \
                    >= (1 - self.chance) / (1 + log((total_decisions - len(decisions)), 2)):
                self.score = 1 - self.chance / (1 + log(len(decisions), 2))
                self.p_score = True
            else:
                self.score = 1 - (1 - self.chance) / (1 + log((total_decisions - len(decisions)), 2))
                self.p_score = False
        else:
            self.score = float('inf')
            self.p_score = True
        self.test = test

    def __str__(self):
        return f"chance: {self.chance} + score: {self.score}"

    def __lt__(self, other):
        return self.score < other.score


def funk(tests, decisions, test):
    decisions_for_test = [tests[test](decision[0]) for decision in decisions]
    dec = []
    for i in range(len(decisions_for_test)):
        if decisions_for_test[i]:
            dec.append(decisions[i])
    return BuildNode(test, dec, len(decisions_for_test))


def buildNextNode(decisions, tests):
    if len(decisions) <= 1:
        return LeafNode(decisions[0][0])

    heap = [funk(tests, decisions, i) for i in range(len(tests))]
    heapify(heap)
    i = heappop(heap).test
    root = TestNode(i)
    decisions_right = [tests[i](decision[0]) for decision in decisions]
    dec = []
    for i in range(len(decisions_right)):
        if decisions_right[i]:
            dec.append(decisions[i])
    root.true = buildNextNode(dec, tests)
    dec = []
    for i in range(len(decisions_right)):
        if not decisions_right[i]:
            dec.append(decisions[i])
    root.false = buildNextNode(dec, tests)

    return root


def build_decision_tree_highscore(decisions, tests):
    if len(decisions) <= 1:
        return LeafNode(decisions[0][0])

    heap = [funk(tests, decisions, i) for i in range(len(tests))]
    heapify(heap)
    i = heappop(heap).test
    root = TestNode(i)
    decisions_right = [tests[i](decision[0]) for decision in decisions]
    dec = []
    for i in range(len(decisions_right)):
        if decisions_right[i]:
            dec.append(decisions[i])
    root.true = buildNextNode(dec, tests)
    dec = []
    for i in range(len(decisions_right)):
        if not decisions_right[i]:
            dec.append(decisions[i])
    root.false = buildNextNode(dec, tests)

    return root

    # Hvis alle testene kun inneholder en besluttning lag løvnode med den besluttningen
    # For hver test: Finn hvilke besluttninger som går igjennom
    # Heap en liste med lister over hvilke besluttninger som går igjennom for hvilke tester
    # Kalkuler score for hver test, samtidig som du putter de inn i heapen
    # Sorter basert på score
    # Velg den testen som har best score
    # Lag en test node og sett den som rot

    # BRANCH1
    # Hvis alle testene kun inneholder en besluttning lag løvnode med den besluttningen
    # Fjern alle tester som ikke inneholder en av besluttningene som gikk igjennom testen
    # Fjern alle beslutningene som ikke kom igjennom testen fra hver test
    # oppdater score og heapify
    # Velg ny test
    # Lag en test node og sett den som høyrebarn til noden over
    # Gå videre ned

    # BRANCH2
    # Hvis alle testene kun inneholder en besluttning lag løvnode med den besluttningen
    # Fjern alle tester som ikke inneholder en av besluttningene som IKKE gikk igjennom
    # Fjern alle beslutningene som kom igjennom testen fra hver test
    # oppdater score og heapify
    # velg ny test
    # Lag en test node og sett den som venstrebarn til noden over
    # Gå videre ned

    # Gi en verdi til hver test
    # velg max(sannsynlighet for at en besluttning kommer igjennom/antall unike beslutninger som kommer igjennom
    #          , sannsynlighet for at en besluttning ikke kommer igjennom/antall unike som ikke kommer igjennom
    # Finn beste test, fjern decisions og test resterende på nytt
    # Skriv koden din her
    pass


def test_answer(student, decisions, functions):
    if not isinstance(student, TestNode):
        print("Rotnoden i svaret er ikke en TestNode")
        return -1

    expectance = 0
    for name, prob in decisions:
        questions = 0
        node = student
        while isinstance(node, TestNode):
            questions += 1
            if functions[node.function](name):
                node = node.true
            else:
                node = node.false

        if not isinstance(node, LeafNode):
            print("Noden som ble nådd for {:} er ikke en løvnode".format(name))
            return -1

        if name != node.name:
            print(
                "Løvnoden som nås av {:} tilhører ikke denne beslutningen".format(
                    name
                )
            )
            return -1

        expectance += prob * questions

    return expectance


# fmt: off
tests = [
    ([("a", 0.5), ("b", 0.5)], [lambda x: x == "a"]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.4)], [lambda x: x == "a", lambda x: x == "b"]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.4)], [lambda x: x in ["a", "b"], lambda x: x == "b"]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.4)], [lambda x: x in ["a", "b"], lambda x: x in ["b", "c"]]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.2), ("d", 0.2)], [lambda x: x in ["a", "b"], lambda x: x in ["b", "c"]]),
    ([("a", 0.3), ("b", 0.3), ("c", 0.2), ("d", 0.2)],
     [lambda x: x in ["a", "b"], lambda x: x in ["b", "c"], lambda x: x == "d"]),
]
# fmt: on

for test_num, test in enumerate(tests):
    student = build_decision_tree_highscore(test[0], test[1])
    result = test_answer(student, test[0], test[1])

    if result == -1:
        print("Feilet for test {:}".format(result, test_num + 1))

    else:
        print(
            "Fikk en forventning på {:} for test {:}".format(
                result, test_num + 1
            )
        )
