def transpose(adj_list):
    ans = [[] for i in range(len(adj_list))]
    for i , edges in enumerate(adj_list):
        for edge in edges:#i is the index, edge is every edge in edges
            start = i
            end = edge[0]
            tuples = (start, edge[1])
            ans[end].append(tuples)
    return ans