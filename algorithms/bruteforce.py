def bruteforce(items, weight_limit: int):
    if len(items) == 0:
        return 0, []

    max_value = 0
    max_valued_packed = []
    for i, item in enumerate(items):
        if item.weight > weight_limit:
            continue

        value, packed = bruteforce(items[i + 1:], weight_limit - item.weight)
        if value + item.value >= max_value:
            max_value = value + item.value
            max_valued_packed = [item] + packed

    return max_value, max_valued_packed
