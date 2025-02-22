def k_largest(A, k):
    print(A)
    if k < 1:
        return []
    if len(A) <= 1:
        return A
    A, index = find_kth_largest(A, 0, len(A), k)
    A, q, r = partition(A, 0, A[index], len(A), k)
    return A[(len(A)-k):]


def find_kth_largest(A, p, r, k):
    med_of_med = find_good_split(A, p, r, k)
    A, low, high = partition(A, p, med_of_med, r, k)
    if low <= len(A)-k <= high:
        return A, low
    elif low > len(A) - k:
        return find_kth_largest(A, p, low, k)
    else:
        return find_kth_largest(A, high, r, k)


def partition(A, p, x, r, k):
    low, high = p, p
    for i in range(p, r):
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
    #print("Before: A[low]", A[low], "A[high]", A[high], "A[i]",A[i])



def find_good_split(A, p, r, k):
    n = r-p
    medians = []
    i = 0
    while i < n//5:
        medians.append(find_median(A, p+i*5, 5))
        i += 1
    if n%5 != 0:
        medians.append(find_median(A, p+i*5, n%5))
    if len(medians) == 1:
        return medians[0]
    else:
        return find_good_split(medians, 0, len(medians)-1, k)


def find_median(A, p, r):
    #insertion sort
    for i in range(p+1, p+r):
        tmp = A[i]
        j = i-1
        while A[j] > tmp and j >= p:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = tmp
    return A[p + r//2]

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
    (([-93958, -86777, -85623, -85326, -84773, -78330, -69375, -66359, -62640, -60942, -60890, -57025, -55999, -55456, -55330, -49945, -44564, -42938, -42402, -42375, -40117, -39976, -37861, -35532, -33067, -33062, -28684, -27905, -27286, -26887, -26679, -25797, -22283, -21993, -16054, -60795, -39349, -14495, -13540, -11996, -11901, -11058, -9862, -9047, -7584, -6312, -5228, -2592, -1975, 402, -10002, 526, 4687, 4759, 6613, 8772, 11872, 20532, 20831, 3318, 13982, 19546, 21927, 22303, 22303, 27597, 27916, 29245, 36009, 41477, 41587, 41688, 30206, 30094, 39433, 44505, 47224, 90521, 47644, 48295, 52889, 53914, 54033, 58871, 60561, 63792, 64142, 66324, 67626, 69399, 72442, 73337, 90500, 91833, 92125, 76806, 77087, 80734, 99670, 47600], 37),
    [22303, 23674, 27597, 27916, 29245, 30094, 30206, 36009, 39433, 41477, 41587, 41688, 44505, 47224, 47600, 47644, 48295, 52889, 53914, 54033, 58871, 60561, 63792, 64142, 66324, 67626, 69399, 72442, 73337, 76806, 77087, 80734, 90500, 90521, 91833, 92125, 99670])
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