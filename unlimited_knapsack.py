def unlimited_knapsack_partial(items, W, weight_max_value):
    if weight_max_value.__contains__(W):
        return  weight_max_value[W]
    maxValue = items[0]
    for item in items:
        tmp = unlimited_knapsack_partial(items,W - item.getWeiht(), weight_max_value)
        if tmp.getValue() > maxValue.getValue():
            maxValue = tmp
    weight_max_value[W] = maxValue
    return maxValue

def unlimited_knapsack(items, W):
    # a dictionary to keep track of what the maximum value is for a certain amount of weight.
    weight_max_value = {}
    return unlimited_knapsack_partial(items, W, weight_max_value)


