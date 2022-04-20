def next_vertex(in_tree, distance):
    temp_distance = [i for i in distance]
    false = [i for i in range(len(in_tree)) if in_tree[i] == False]
    if len(false) == 1:
        return false[0]
    for i in range(len(temp_distance)):
        m = min(temp_distance)
        index = temp_distance.index(m)
        if in_tree[index] == True:
            temp_distance[index] = float("inf")
        else:
            return index
    return False