# !/usr/bin/python3
# coding=utf-8

def longest_decreasing_subsequence(s):
    n = len(s)
    return bottom_up_longest_decreasing_subsequence(s, [[s[i]] for i in range(n)], n)


def bottom_up_longest_decreasing_subsequence(s, sequences, n):
    if n == 1:
        return s
    for i in range(1, n):
        for j in range(i):
            if s[i] < s[j] and len(sequences[i]) < len(sequences[j]) + 1:
                sequences[i] = sequences[j][:]
                sequences[i].append(s[i])
    current_longest = [0, []]
    for sequence in sequences:
        if current_longest[0] < len(sequence):
            current_longest[1], current_longest[0] = sequence, len(sequence)
    return current_longest[1]


def is_decreasing(s):
    if len(s) == 1:
        return True
    decreasing = True
    bigger = s[0]
    for i in range(1, len(s)):
        if s[i] < bigger:
            bigger = s[i]
        else:
            decreasing = False
            break
    return decreasing


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
    ([5, 4, 2, 10, 3, 3, 3, 2], 4),
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
            "Delfølgen har ikke riktig lengde. Riktig lengde er"
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
