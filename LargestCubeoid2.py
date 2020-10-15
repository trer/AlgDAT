#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import base64
import sys
import collections

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(34)

# Minimalisert kode for å verifisere at svaret er riktig. Kan ignoreres.
exec(
    base64.b64decode(
        "ZGVmIGExMjMoeCx4MCx5MCx4MSx5MSk6Cg"
        + "lBPWZsb2F0KCdpbmYnKQoJZm9yIEIgaW4g"
        + "cmFuZ2UoeDAseDErMSk6CgkJZm9yIEMgaW"
        + "4gcmFuZ2UoeTAseTErMSk6QT1taW4oQSx4"
        + "W0JdW0NdKQoJcmV0dXJuIEEKZGVmIGJydX"
        + "RlZm9yY2UoeCk6CglBPTAKCWZvciBCIGlu"
        + "IHJhbmdlKGxlbih4KSk6CgkJZm9yIEMgaW"
        + "4gcmFuZ2UobGVuKHhbMF0pKToKCQkJZm9y"
        + "IEQgaW4gcmFuZ2UoQixsZW4oeCkpOgoJCQ"
        + "kJZm9yIEUgaW4gcmFuZ2UoQyxsZW4oeFsw"
        + "XSkpOkE9bWF4KEEsKEQtQisxKSooRS1DKz"
        + "EpKmExMjMoeCxCLEMsRCxFKSkKCXJldHVybiBB"
    )
)


def myFunk(e):
    return e[-1]


def largest_area(x, i, j, down, right, depth):
    print("depth", depth, "down", down, "right", right)
    largestArea = 0
    check_areas = []
    if down and right:
        for k in range(i, len(x)):
            for l in range(j, len(x)):
                kl = (k, l, (k + 1 - i) * (l + 1 - j))
                check_areas.append(kl)
    if down and not right:
        for k in range(i, len(x)):
            for l in range(0, j):
                kl = (k, l, (k + 1 - i) * (j-l+1))
                check_areas.append(kl)
    if not down and right:
        for k in range(0, i):
            for l in range(j, len(x)):
                kl = (k, l, (i-k+1) * (l + 1 - j))
                check_areas.append(kl)
    if not down and not right:
        for k in range(0, i):
            for l in range(0, j):
                kl = (k, l, (i-k+1) * (j-l+1))
                check_areas.append(kl)
    check_areas.sort(reverse=True, key=myFunk)

    for area in check_areas:
        print(area)
        if area[-1] <= largestArea:
            print("breaking because area is to small", area[-1])
            break
        all_above = True
        if down and right:
            for m in range(i, area[0]+1):
                for n in range(j, area[1]+1):
                    if x[m][n] < depth:
                        print("Breaking at:", x[m][n])
                        all_above = False
                        break
                if not all_above:
                    break
            if all_above:
                largestArea = area[-1]
        if down and not right:
            for m in range(i, area[0] + 1):
                for n in range(area[1], j):
                    if x[m][n] < depth:
                        print("Breaking at:", x[m][n])
                        all_above = False
                        break
                if not all_above:
                    break
            if all_above:
                largestArea = area[-1]
        if not down and right:
            for m in range(area[0], i):
                for n in range(j, area[1]+1):
                    if x[m][n] < depth:
                        print("Breaking at:", x[m][n])
                        all_above = False
                        break
                if not all_above:
                    break
            if all_above:
                largestArea = area[-1]
        if not down and not right:
            for m in range(area[0], i):
                for n in range(area[1], j):
                    if x[m][n] < depth:
                        print("Breaking at:", x[m][n])
                        all_above = False
                        break
                if not all_above:
                    break
            if all_above:
                largestArea = area[-1]
    print("returning:", largestArea, "for depth:", depth)
    return largestArea

def largest_cuboid(x):
    print("start")
    length = len(x)
    if length == 1:
        return x[0][0]

    largest = 0

    for i in range(length):
        for j in range(length):
            area = [[largest_area(x, i, j, True, True, x[i][j]),
                       largest_area(x, i, j, True, False, x[i][j])],
                       [largest_area(x, i, j, False, True, x[i][j]),
                       largest_area(x, i, j, False, False, x[i][j])]]
            print("area", area)
            area = largest_area(area,0,0,True,True, x[i][j])
            if area * x[i][j] > largest:
                largest = area * x[i][j]
    return largest



def search():
    pass

# Some håndskrevne tester
tests = [
    ([[1]], 1),
    ([[1, 1], [2, 1]], 4),
    ([[1, 1], [5, 1]], 5),
    ([[0, 0], [0, 0]], 0),
    ([[10, 0], [0, 10]], 10),
    ([[10, 6], [5, 10]], 20),
    ([[100, 100], [40, 55]], 200),
]


def generate_random_test_case(length, max_value):
    test_case = [
        [random.randint(0, max_value) for i in range(length)]
        for j in range(length)
    ]
    return test_case, bruteforce(test_case)


def test_student_algorithm(test_case, answer):
    student = largest_cuboid(test_case)
    if student != answer:
        if len(test_case) < 5:
            response = "Koden feilet for følgende input: (x={:}).".format(
                test_case
            ) + " Din output: {:}. Riktig output: {:}".format(student, answer)
        else:
            response = "Koden feilet på input som er for langt til å vises her"
        print(response)
        sys.exit()


# Tester funksjonen på håndskrevne tester
for test_case, answer in tests:
    test_student_algorithm(test_case, answer)

# Tester funksjonen på tilfeldig genererte tester
for i in range(1000):
    test_case, answer = generate_random_test_case(random.randint(1, 3), 20)
    test_student_algorithm(test_case, answer)
for i in range(00):
    test_case, answer = generate_random_test_case(
        random.randint(1, 20), 10000
    )
    test_student_algorithm(test_case, answer)

