from math import inf

def adjacency_list(graph_str):
    lis = graph_str.split('\n')
    lis.pop()
    info = lis[0].split()
    #info[0]shows the type the grpah, info[1] shows the number of vertex
    ans = [[] for i in range(int(info[1]))]
    if len(info) == 2:   # no weight
        if info[0] == 'D':   #directed
            for i in range(1, len(lis)):
                start, end = map(lambda x:int(x), lis[i].split())
                tup = (end, None)
                ans[start].append(tup)
        elif info[0] == 'U': #undirected
            for i in range(1, len(lis)):
                start, end = map(lambda x:int(x), lis[i].split())
                tup1 = (end, None)
                tup2 = (start, None)
                ans[start].append(tup1)
                ans[end].append(tup2)
    elif len(info) == 3: #has weight
        if info[0] == 'D':   #directed
            for i in range(1, len(lis)):
                start, end, weight = map(lambda x:int(x), lis[i].split())
                tup = (end, weight)
                ans[start].append(tup)
        elif info[0] == 'U': #undirected
            for i in range(1, len(lis)):
                start, end, weight= map(lambda x:int(x), lis[i].split())
                tup1 = (end, weight)
                tup2 = (start, weight)
                ans[start].append(tup1)
                ans[end].append(tup2)
    return ans    

def check(in_tree):
    for flag in in_tree:
        if flag == False:
            return True
    return False

def next_vertex(in_tree, distance):
    temp_distance = [i for i in distance]
    for i in range(len(temp_distance)):
        m = min(temp_distance)
        pos = temp_distance.index(m)
        if in_tree[pos] == True:
            temp_distance[pos] = inf
        else:
            return pos
    return False

def which_walkways(campus_map):
    start = 0
    adj_list = adjacency_list(campus_map)
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [inf for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while check(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    ans = []
    for i, j in enumerate(parent):
        if j != None:
            tup = (min(i, j), max(i,j))
            ans.append(tup)
    return ans

campus_map = """\
U 1 W
"""

print(sorted(which_walkways(campus_map)))
