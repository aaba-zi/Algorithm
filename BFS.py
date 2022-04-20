import collections
def bfs_tree(adj_list, start):
    length_of_list = len(adj_list)
    state = ['U' for i in range(length_of_list)]
    parent = [None for i in range(length_of_list)]
    Q = collections.deque()
    state[start] == "D"
    Q.append(start)
    return bfs_loop(adj_list, Q, state, parent)

def bfs_loop(adj_list, Q, state, parent):
    while Q:
        u = Q.popleft()
        for edge in adj_list[u]:
            v = edge[0]
            if state[v] == "U":
                state[v] = "D"
                parent[v] = u
                Q.append(v)
        state[u] = "P"
    return parent