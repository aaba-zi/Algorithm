def dfs_tree(adj_list, start):
    length = len(adj_list)
    state = ["U" for i in range(length)]
    parent = [None for i in range(length)]
    state[start] = "D"
    dfs_loop(adj_list, start, state, parent)
    return parent

def dfs_loop(adj_list, start, state, parent):
    for edge in adj_list[start]:
        v = edge[0]
        if state[v] == "U":
            state[v] = "D"
            parent[v] = start
            dfs_loop(adj_list, v, state, parent)
    state[start] = "P"
