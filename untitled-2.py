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

def check(in_tree, indegree):
    for i, flag in enumerate(in_tree):
        if flag == False and indegree[i] > 0:
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

def prim(adj_list, start, indegree):
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [inf for i in range(n)]
    parent = [None for i in range(n)]
    distance[start] = 0
    while check(in_tree, indegree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance

def dijkstra(adj_list, start):
    adj_list = adjacency_list(city_map)
    n = len(adj_list)
    parent, distance = dijakstra(adj_list, start)
    for i in range(len(distance)):
        if distance[i] == inf:
            distance[i] = -1
    return max(distance)*2

def maximum_energy(city_map, start):
    adj_list = adjacency_list(city_map)
    n = len(adj_list)
    indegree = [0 for i in range(n)]
    for edges in adj_list:
        for end, weight in edges:
            indegree[end] = indegree[end]+1
    if indegree[start]==0:
        return 0
    parent, distance = prim(adj_list, start, indegree)
    #find minimum spanning tree by prim algorithm
    ans1 = 0 #go
    for dis in distance:
        if dis != inf:
            ans1 += dis
    end = 0
    while 1:#find destination
        if end in parent:
            end = parent.index(end)
        else:
            break
    ans2 = 0 #back
    parent, distance = dijkstra(adj_list, end)
    #find shotest path to go back by dijkstra    
    ans2 = distance[start]
    return ans1+ans2


 	

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(maximum_energy(city_map, 0))
print(maximum_energy(city_map, 1))
print(maximum_energy(city_map, 2))