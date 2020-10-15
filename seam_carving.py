#!/usr/bin/python3
# coding=utf-8


def addWeights(weights):
    for i in range(len(weights) - 2, -1, -1):
        for j in range(len(weights[0])):
            a = c = float('inf')
            if j > 0:
                a = weights[i + 1][j - 1]
            b = weights[i + 1][j]
            if j < len(weights[0]) - 1:
                c = weights[i + 1][j + 1]
            weights[i][j] += min(a, b, c)
    return weights


def find_min_index(weights, i, j):
    a = c = float('inf')
    if j > 0:
        a = weights[i][j-1]
    b = weights[i][j]
    if j < len(weights[0]) - 1:
        c = weights[i][j+1]
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    return c


def find_shortest_path(weights, i, j, previous_paths, current_weight, path, current_best):
    if i == len(weights):
        return [], 0
    if (i, j) in previous_paths:
        print("found at level:", "i:", i, "j:", j)
        return previous_paths[(i, j)]

    path.append((j, i))
    current_weight += weights[i][j]
    #if current_weight >= current_best:
    #    print("current weight", current_weight, i, j)
    #    return path, current_weight
    weight_a = weight_c = float('inf')
    if j > 0:
        path_a, weight_a = find_shortest_path(weights, i+1, j-1, previous_paths, current_weight, path, current_best)
    path_b, weight_b = find_shortest_path(weights, i+1, j, previous_paths, current_weight, path, current_best)
    if j < len(weights[0]) - 1:
        path_c, weight_c = find_shortest_path(weights, i + 1, j + 1, previous_paths, current_weight, path, current_best)

    # move to lowest of (i, j-1), (i,j) and (i, j+1)
    if weight_a <= weight_b and weight_a <= weight_c:
        path_up, weight_up = path_a, weight_a
    elif weight_c <= weight_a and weight_c <= weight_b:
        path_up, weight_up = path_c, weight_c
    else:
        path_up, weight_up = path_b, weight_b
    path_up.insert(0, (j, i))
    weight_up += weights[i][j]
    print(path_up)
    previous_paths[(i, j)] = [path_up, weight_up]
    return path_up, weight_up


def find_path(weights):
    if len(weights) == 0:
        return []
    paths = []
    current_best = float('inf')
    previous_paths = {}
    for j in range(len(weights[0])):
        path, weight = find_shortest_path(weights, 1, j, previous_paths, weights[0][j], [(j, 0)], current_best)
        path.insert(0, (j, 0))
        weight += weights[0][j]
        if weight < current_best:
            current_best = weight
        print(path)
        paths.append((path, weight))
    shortest_path = paths[0]
    for i in range(1, len(paths)):
        if shortest_path[1] > paths[i][1]:
            shortest_path = paths[i]

    return shortest_path[0]


# Tester på formatet (vekter, minste mulige vekt på sti).
tests = [
    ([[1]], 1),
    ([[1, 1]], 1),
    ([[1], [1]], 2),
    ([[2, 1], [2, 1]], 2),
    ([[1, 1], [1, 1]], 2),
    ([[2, 1], [1, 2]], 2),
    ([[3, 2, 1], [1, 3, 2], [2, 1, 3]], 4),
    ([[1, 10, 3, 3], [1, 10, 3, 3], [10, 10, 3, 3]], 9),
    ([[1, 2, 7, 4], [9, 3, 2, 5], [5, 7, 8, 3], [1, 3, 4, 6]], 10),
]


# Verifiserer at en løsning er riktig gitt vektene, stien og den minst
# mulige vekten man kan ha på en sti.
def verify(weights, path, optimal):
    if len(path) != len(weights):
        return False, "Stien er enten for lang eller for kort."

    last = -1
    for index, element in enumerate(path):
        if type(element) != tuple:
            return False, "Stien består ikke av tupler."
        if len(element) != 2:
            return False, "Stien består ikke av tupler på formatet (x,y)."
        if index != element[1]:
            return False, "Stien er ikke vertikal."
        if element[0] < 0 or element[0] >= len(weights[0]):
            return False, "Stien går utenfor bildet."
        if last != -1 and not last - 1 <= element[0] <= last + 1:
            return False, "Stien hopper mer enn en piksel per rad."
        last = element[0]

    weight = sum(weights[y][x] for x, y in path)
    if weight != optimal:
        return (
            False,
            "Stien er ikke optimal. En optimal sti ville hatt"
            + "vekten {:}, mens din hadde vekten {:}".format(optimal, weight),
        )

    return True, ""


failed = False

for test, optimal_weight in tests:
    answer = find_path([row[:] for row in test])
    correct, error_message = verify(test, answer, optimal_weight)
    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")
