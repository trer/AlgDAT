#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
import math

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(1222)


def find_maximum(x):
    n = len(x)
    if n == 1:
        return x[0]
    check_13 = math.floor(n / 3)
    check_23 = math.floor(2*n / 3)
    first = x[0]
    check_13x = x[check_13]
    check_23x = x[check_23]

    if first > check_13x:
        if first > check_23x:
            p = check_23
            q = check_13
            b = maxMidle(x, p, q, check_23x, first, n)
        else:
            p = check_13
            q = 0
            b = maxMidle(x, p, q, check_13x, check_23x, n)
    else:
        if check_13x > check_23x:
            p = 0
            q = check_23
            b = maxMidle(x, p, q, first, check_13x, n)
        else:
            p = check_13
            q = 0
            b = maxMidle(x, p, q, check_13x, check_23x, n)
    return b


def maxMidle(x, p, q, p_value, current_max, n):
    if p > q:
        q += n
    check_13 = math.floor(p + ((q-p) / 3))
    check_23 = math.floor(p + ((q-p)*2 / 3))
    if q > n - 1:
        q -= n
    if check_13 > n - 1:
        check_13 -= n
    if check_23 > n - 1:
        check_23 -= n

    check_13x = x[check_13]
    check_23x = x[check_23]

    if p == check_13 or p == check_23 or check_13 == check_23:
        return current_max
    if p_value >= check_13x:
        if p_value >= check_23x:
            p = check_23
            q = check_13
            b = maxMidle(x, p, q, check_23x, p_value, n)
        else:
            p = check_13
            q = q
            b = maxMidle(x, p, q, check_13x, check_23x, n)
    else:
        if check_13x >= check_23x:
            p = p
            q = check_23
            b = maxMidle(x, p, q, p_value, check_13x, n)
        else:
            p = check_13
            q = q
            b = maxMidle(x, p, q, check_13x, check_23x, n)
    return b



# Noen håndskrevne tester
tests = [
    ([1], 1),
    ([1, 3], 3),
    ([3, 1], 3),
    ([1, 2, 1], 2),
    ([1, 0, 2], 2),
    ([2, 0, 1], 2),
    ([0, 2, 1], 2),
    ([0, 1, 2], 2),
    ([2, 1, 0], 2),
    ([2, 3, 1, 0], 3),
    ([2, 3, 4, 1], 4),
    ([2, 1, 3, 4], 4),
    ([4, 2, 1, 3], 4),
]


def generate_random_test_case(length, max_value):
    print(length)
    test = random.sample(range(max_value), k=length)
    m = max(test)
    test.remove(m)
    t = random.randint(0, len(test))
    test = sorted(test[:t]) + [m] + sorted(test[t:], reverse=True)
    t = random.randint(0, len(test))
    test = test[t:] + test[:t]
    return (test, m)


def test_student_maximum(test_case, answer):
    student = find_maximum(test_case)
    if student != answer:
        if len(test_case) < 20:
            response = (
                    "'Find maximum' feilet for følgende input: "
                    + "(x={:}). Din output: {:}. ".format(test_case, student)
                    + "Riktig output: {:}".format(answer)
            )
        else:
            response = (
                    "Find maximum' feilet på input som er "
                    + "for langt til å vises her"
            )
        print(response)
        sys.exit()


# Testing student maximum on custom made tests
for test_case, answer in tests:
    test_student_maximum(test_case, answer)

# Testing student maximum on random test cases
for i in range(40):
    test_case, answer = generate_random_test_case(random.randint(1, 1000), 2000)
    test_student_maximum(test_case, answer)
