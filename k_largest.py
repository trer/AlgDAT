import random

def k_largest(A, k):
    if k < 1:
        return []
    if len(A) <= 1:
        return A
    return find_kth_largest(A, k)


def find_kth_largest(A, k):
    split = A[random.randint(0, len(A)-1)]
    A, low, high = partition(A, split)

    if low <= len(A) - k <= high:
        return A[len(A) - k:]
    elif low > len(A) - k:
        tmp = A[low:]
        return tmp + find_kth_largest(A[0:low], k-len(A)+low)
    else:
        return find_kth_largest(A[high:], k)


def partition(A, x):
    low, high = 0, 0
    for i in range(len(A)):
        a = A[i]
        if a == x:
            A[high], A[i] = A[i], A[high]
            high += 1
        elif a < x:
            A[high], A[i] = A[i], A[high]
            A[high], A[low] = A[low], A[high]
            #A[low], A[high], A[i] = A[i], A[low], A[high]
            low += 1
            high += 1
    return A, low, high
    # print("Before: A[low]", A[low], "A[high]", A[high], "A[i]",A[i])


def find_good_split(A):
    n = len(A)
    medians = []
    i = 0
    while i < n // 5:
        medians.append(find_median(A[i * 5: (i+1)*5]))
        i += 1
    if n % 5 != 0:
        medians.append(find_median(A[i * 5: len(A)]))
    if len(medians) == 1:
        return medians[0]
    else:
        return find_good_split(medians)


def find_median(A):
    # insertion sort
    for i in range(1, len(A)):
        tmp = A[i]
        j = i - 1
        while A[j] > tmp and j >= 0:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = tmp
    return A[len(A)//2]


# Sett med tester.
tests = [
    (([], 0), []),
    (([1], 0), []),
    (([1], 1), [1]),
    (([1, 2], 1), [2]),
    (([-1, -2], 1), [-1]),
    (([-1, -2, 3], 2), [-1, 3]),
    (([1, 2, 3], 2), [2, 3]),
    (([3, 2, 1], 2), [2, 3]),
    (([3, 3, 3, 3], 2), [3, 3]),
    (([4, 1, 3, 2, 3], 2), [3, 4]),
    (([4, 5, 1, 3, 2, 3], 4), [3, 3, 4, 5]),
    (([9, 3, 6, 1, 7, 3, 4, 5], 4), [5, 6, 7, 9]),
    (([9, 3, 6, 1, 7, 3, 4, 5], 8), [1, 3, 3, 4, 5, 6, 7, 9]),
    (([9, 3, 6, 1, 7, 3, 4, 5], 2), [7, 9]),
    (([52106, 57734, -76815, 17339, -97824, -41720, 14874, -77568, 61037, 8798, 72077, 87661, 79888, -163, -73583,
       -69942, -7898, 80523, -56827, -5343, -22260, -11939, 48176, -26956, 8957, 31736, 46250, 72339, -93716, -28137,
       72840, -68421, -15439, 20552, 13957, 61686, -83660, 49449, 52795, -45224, 1693, 11022, 24240, 42506, 2103,
       -86160, 44045, 55966, 11840, 8382, 50435, 79164, 37585, 54118, 43341, -78941, -61086, 39374, 84373, 61919, 3631,
       -69536, -69838, 45213, 49365, -46300, 11027, 29841, 32513, -93154, 29355, -47870, -86765, -49626, -66973, 48252,
       62926, -98212, -42488, 86619, 47227, 52955, 6493, 40382, 80325, 53672, 31238, 49603, 61132, -30489, 73740,
       -42008, 76313, -74805, 72316, 62687, -50005], 10),
     [72840, 73740, 76313, 79164, 79888, 80325, 80523, 84373, 86619, 87661]),
]

for test, solution in tests:
    student_answer = k_largest(*test)
    if type(student_answer) != list:
        print("Metoden må returnere en liste")
    else:
        student_answer.sort()
        if student_answer != solution:
            print(
                "Feilet for testen {:}, resulterte i listen ".format(test)
                + "{:} i stedet for {:}.".format(student_answer, solution)
            )
