def combine_position_value_lists(list1, list2):
    merged = sorted(list1 + list2, key=lambda x: x["positions"][0])
    result = []
    for current in merged:
        l2, r2 = current["positions"]
        added = False
        for existing in result:
            l1, r1 = existing["positions"]
            overlap = max(0, min(r1, r2) - max(l1, l2))
            length = r2 - l2
            if overlap > length / 2:
                existing["values"] += current["values"]
                added = True
                break
        if not added:
            result.append(current)
    return result
