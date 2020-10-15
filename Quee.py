import math

k = 2048
k_1 = k
k_2 = k
i = 0
while k_1 >= 2:
    k_1 = math.sqrt(k_1)
    i += 1

k_2 = math.log(k_2, 2)

print(i, k_2, math.log(k_2, 2))