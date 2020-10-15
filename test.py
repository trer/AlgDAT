if (end[0] - i) ** 2 > (end[1] - j) ** 2:
    mini_queue[1], mini_queue[3] = mini_queue[3], mini_queue[1]
    if end[0] > i:
        mini_queue[0], mini_queue[3] = mini_queue[0], mini_queue[3]
        if end[1] > j:
            mini_queue[1], mini_queue[2] = mini_queue[2], mini_queue[1]
else:
    mini_queue[0], mini_queue[1] = mini_queue[1], mini_queue[0]
    if end[0] > i:
        mini_queue[1], mini_queue[2] = mini_queue[2], mini_queue[1]
        if end[1] > j:
            mini_queue[0], mini_queue[3] = mini_queue[3], mini_queue[0]