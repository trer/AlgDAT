# !/usr/bin/python3
# coding=utf-8
import math


def longest_decreasing_subsequence(s):
    # For storing the previous index in the subsequence
    # So at P[j] you will find the index of the int before s[j]
    P = [float('inf')] * len(s)
    # For storing the last index in a subsequence.
    # So at M[j] you will find the index of the last int in the subsequence of length j.
    M = [float('inf')] * (len(s) + 1)

    L = 0
    for i in range(0, len(s)):
        lo = 1
        hi = L
        while lo <= hi:
            mid = math.ceil((lo + hi) / 2)
            # If the int in the last index of subsequence of length mid is greater than the next int
            if s[M[mid]] > s[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo

        P[i] = M[newL - 1]
        M[newL] = i

        if newL > L:
            L = newL

    S = [0] * L
    # Start at the last int of the longest substring
    k = M[L]
    for i in range(L - 1, -1, -1):
        # add the int
        S[i] = s[k]
        # go to the next index
        k = P[k]
    return S


# Teste på formatet (følge, riktig lengde på svar)
tests = [
    ([1], 1),
    ([1, 2], 1),
    ([1, 2, 3], 1),
    ([2, 1], 2),
    ([3, 2, 1], 3),
    ([1, 3, 2], 2),
    ([3, 1, 2], 2),
    ([1, 1], 1),
    ([1, 2, 1], 2),
    ([8, 7, 3, 6, 2, 6], 4),
    ([10, 4, 2, 1, 7, 5, 3, 2, 1], 6),
    ([3, 7, 2, 10, 3, 3, 3, 9], 2),
]


def verify(sequence, subsequence, optimal_length):
    # Test if the subsequence is actually a subsequence
    index = 0
    for element in sequence:
        if element == subsequence[index]:
            index += 1
            if index == len(subsequence):
                break

    if index < len(subsequence):
        return False, "Svaret er ikke en delfølge av følgen."

    # Test if the subsequence is decreasing
    for index in range(1, len(subsequence)):
        if subsequence[index] >= subsequence[index - 1]:
            return False, "Den gitte delfølgen er ikke synkende."

    # Test if the solution is optimal
    if len(subsequence) != optimal_length:
        return (
            False,
            "Delfølgen har ikke riktig lengde. Riktig lengde er "
            + "{:}, mens delfølgen har lengde ".format(optimal_length)
            + "{:}".format(len(subsequence)),
        )

    return True, ""


failed = False

for test, optimal_length in tests:
    answer = longest_decreasing_subsequence(test[:])
    correct, error_message = verify(test, answer, optimal_length)

    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
