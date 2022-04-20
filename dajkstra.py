def check(in_tree, indegree):
    for  i, flag in enumerate(in_tree):
        if flag == False and indegree[i] > 0:
            return True
    return False

def next_vertex(in_tree, distance):
    temp_distance = [i for i in distance]
    for i in range(len(temp_distance)):
        m = min(temp_distance)
        index = temp_distance.index(m)
        if in_tree[index] == True:
            temp_distance[index] = float("inf")
        else:
            return index
    return False

def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [float("inf") for i in range(n)]
    parent = [None for i in range(n)]
    indegree = [0 for i in range(n)]
    for edges in adj_list:
        for end, weight in edges:
            indegree[end] = indegree[end] + 1
    distance[start] = 0
    while check(in_tree, indegree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        if adj_list[u] == []:
            break
        for v, weight in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
