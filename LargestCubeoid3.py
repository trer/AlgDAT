#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import base64
import sys

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(123)

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


def largest_cuboid(x):
    n = len(x)
    checked_cubes = {}
    return largest_cube(x, 0, 0, n, n, checked_cubes)


def largest_cube(x, x_0, y_0, x_r, y_r, checked_cubes):
    if (x_0, y_0, x_r, y_r) in checked_cubes:
        return checked_cubes.get((x_0, y_0, x_r, y_r))

    area = (x_r - x_0) * (y_r - y_0)

    if area < 1:
        return 0
    if area == 1:
        return x[x_0][y_0]

    min_depth = [x_0, y_0, x[x_0][y_0]]
    for i in range(x_0, x_r):
        for j in range(y_0, y_r):
            if x[i][j] < min_depth[2]:
                min_depth = [i, j, x[i][j]]

    c_0 = area * min_depth[2]

    c_1 = largest_cube(x, x_0, y_0, x_r, min_depth[1], checked_cubes)
    c_2 = largest_cube(x, x_0, y_0, min_depth[0], y_r, checked_cubes)
    c_3 = largest_cube(x, x_0, min_depth[1] + 1, x_r, y_r, checked_cubes)
    c_4 = largest_cube(x, min_depth[0] + 1, y_0, x_r, y_r, checked_cubes)
    checked_cubes.update({(x_0, y_0, x_r, y_r) : max(c_0, c_1, c_2, c_3, c_4)})
    return max(c_0, c_1, c_2, c_3, c_4)


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
        if len(test_case) < 4:
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
for i in range(20):
    test_case, answer = generate_random_test_case(random.randint(1, 3), 10)
    test_student_algorithm(test_case, answer)
for i in range(10):
    test_case, answer = generate_random_test_case(
        random.randint(1, 20), 100000
    )
    test_student_algorithm(test_case, answer)
