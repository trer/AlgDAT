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




def largest_cuboid(x):
    #print("start")
    length = len(x)
    if length == 1:
        return x[0][0]

    largest = 0
    depths: set = set()
    for line in x:
        for point in line:
            depths.add(point)

    d = []
    for depth in depths:
        d.append(depth)
    d.sort(reverse=True)
    depths = d

    #Check all depths sorted in decending order
    for depth in depths:
        #print("depth: ", depth)
        check_areas = []
        for i in range(length):
            for j in range(length):
                # if check_depths[]:
                ij = (i, j, (length - i) * (length - j) * depth)
                check_areas.append(ij)
        check_areas.sort(reverse=False, key=myFunk)
        #print("starting to check a new area")
        #check all areas for this depth in decending order (based on size)
        while True:
            if len(check_areas) > 0:
                area = check_areas.pop()
                #print(area)
                i = area[0]
                j = area[1]
            else:
                break
            if x[i][j] >= depth:
                k = i
                l = j
                for k in range(i, length):
                    if x[k][j] < depth:
                        k -= 1
                        break
                for l in range(j, length):
                    if x[i][l] < depth:
                        l -= 1
                        break

                #Find all the scores this depth and area, find the score it could yield and sort them
                #They will be checked in desending order, so that once the posible score gets lower than
                #current max it will stop searching
                check_depths: set = set()
                for a in range(i, k+1):
                    for b in range(j, l+1):
                        ab = (a, b, (a-i+1)*(b-j+1)*depth)
                        check_depths.add(ab)

                d = []
                for dep in check_depths:
                    d.append(dep)
                d.sort(reverse=True)
                check_depths = d
                check_depths.sort(reverse=False, key=myFunk)

                tmp = check_depths.pop()
                k = tmp[0]
                l = tmp[1]
                #Testing all squares that could lead to a new largest
                while (k-i+1)*(l-j+1)*depth > largest:
                    allabove = True
                    for n in range(i, k+1):
                        for m in range(j, l+1):
                            if x[n][m] < depth:
                                allabove = False
                                break
                        if not allabove:
                            break

                    if allabove:
                        largest = (k-i+1)*(l-j+1)*depth
                        #print("largest",depths[0])
                        while len(depths) > 0 and largest >= depths[-1]*length*length:
                            #print("removing", depths[-1])
                            depths.pop()
                    #decreacing
                    if len(check_depths) > 0:
                        tmp = check_depths.pop()
                        k = tmp[0]
                        l = tmp[1]
                    else:
                        break
            if area[-1] <= largest:
                #print("removing area: ", area)
                break


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
    test_case, answer = generate_random_test_case(random.randint(1, 4), 20)
    test_student_algorithm(test_case, answer)
for i in range(100):
    test_case, answer = generate_random_test_case(
        random.randint(1, 20), 10000
    )
    test_student_algorithm(test_case, answer)

