#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
import math

# De tilfeldig generete testene er like for hver gang du kjører koden.
# Hvis du vil ha andre tilfeldig genererte tester, så endre dette nummeret.
random.seed(12)


def find_maximum(x):
    n = len(x)
    if n == 1:
        return x[0]
    mid = math.floor(n / 2)
    first = x[0]
    last = x[-1]
    midx = x[mid]
    midx_1 = x[mid-1]

    if first > last:
        if first > midx:
            return maxMidle(x, 0, mid, first, midx, first)
        else: # midx > first
            if midx > midx_1:
                print(x,"går opp")
                return maxMidle(x, mid, n-1, midx, last, midx)
            else: # midx_1 > midx
                return maxMidle(x, 0, mid-1, first, midx_1, midx_1)
    else: #last > first
        if last > midx:
            return maxMidle(x, mid, n-1, midx, last, last)
        else: #midx > last
            if midx > midx_1:
                return maxMidle(x, mid, n - 1, midx, last, midx)
            else:  # midx_1 > midx
                return maxMidle(x, 0, mid - 1, first, midx_1, midx_1)




def maxMidle(x, p, q, p_value, q_value, current_max):
    if p + 1 < q:
        mid = math.floor((p+q)/2)
        midx = x[mid]
        midx_1 = x[mid-1]
        print(p,mid,q)
        if p_value > q_value:
            if p_value > midx:
                return maxMidle(x, p, mid, p_value, midx, p_value)
            else:  # midx > first
                if midx > midx_1:
                    return maxMidle(x, mid, q, midx, q_value, midx)
                else:  # midx_1 > midx
                    return maxMidle(x, p, mid - 1, p_value, midx_1, midx_1)
        else:  # last > first
            if q_value > midx:
                return maxMidle(x, mid, q, midx, q_value, q_value)
            else:  # midx > last
                if midx > midx_1:
                    return maxMidle(x, mid, q, midx, q_value, midx)
                else:  # midx_1 > midx
                    return maxMidle(x, p, mid - 1, p_value, midx_1, midx_1)
    return current_max


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
for i in range(400):
    test_case, answer = generate_random_test_case(random.randint(1, 1000), 2000)
    test_student_maximum(test_case, answer)
