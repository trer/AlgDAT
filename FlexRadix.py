#!/usr/bin/python3
# coding=utf-8


def char_to_int(char):
    return ord(char) - 97


def flexradix(A, d):
    A = radix_sort_from_to(A, 0, 0, len(A))
    return A

def radix_sort_from_to(A, index, p, q):
    if p + 1 < q:
        A = counting_sort(A, index, p, q)
        p_0 = p
        q_0 = p
        char_value = A[p][index]
        for i in range(p, q):
            if char_value == A[i][index]:
                q_0 += 1
            else:
                A = radix_sort_from_to(A, index+1, p_0, q_0)
                p_0 = q_0
                q_0 += 1
                char_value = A[i][index]
            if len(A[i]) <= index + 1:
                tmp = A[p_0]
                A[p_0] = A[i]
                A[i] = tmp
                p_0 += 1
        A = radix_sort_from_to(A, index +1, p_0, q_0)
    return A


def counting_sort(A, index, p, q):
    B = [None]*(q-p)
    for i in range(0, q-p):
        B[i] = A[i+p]
    k = 26
    C = [0] * k
    for i in range(p, q):
        C[char_to_int(A[i][index])] += 1
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    for i in range(q-1, p-1, -1):
        B[C[char_to_int(A[i][index])]-1] = A[i]
        C[char_to_int(A[i][index])] -= 1
    for i in range(p, q):
        A[i] = B[i-p]
    return A


tests = (
    (([], 1), []),
    ((["a"], 1), ["a"]),
    ((["a", "b"], 1), ["a", "b"]),
    ((["b", "a"], 1), ["a", "b"]),
    ((["ba", "ab"], 2), ["ab", "ba"]),
    ((["b", "ab"], 2), ["ab", "b"]),
    ((["ab", "a"], 2), ["a", "ab"]),
    ((["abc", "b"], 3), ["abc", "b"]),
    ((["abc", "b"], 4), ["abc", "b"]),
    ((["abc", "b", "bbbb"], 4), ["abc", "b", "bbbb"]),
    ((["abcd", "abcd", "bbbb"], 4), ["abcd", "abcd", "bbbb"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
    ((["a", "b", "c", "babcbababa"], 10), ["a", "b", "babcbababa", "c"]),
    ((['aaaa', 'aaa', 'a', 'aaaaa', 'aa'], 5), ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']),
    ((['aaaa', 'aaa', 'a', 'aaaaa', 'aa', 'assdfwe', 'adawaaww', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'sf', 'efkwk'], 10),
     ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'adawaaww', 'assdfwe', 'efkwk', 'sf']),
)

for test, solution in tests:
    student_answer = flexradix(test[0], test[1])
    if student_answer != solution:
        print(
            "Feilet for testen {:}, resulterte i listen ".format(test)
            + "{:} i stedet for {:}.".format(student_answer, solution)
        )