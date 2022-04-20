from math import inf

def adjacency_list(graph_str):
    lis = graph_str.split('\n')
    lis.pop()
    info = lis[0].split()
    #info[0]shows the type the grpah, info[1] shows the number of vertex
    ans = [[] for i in range(int(info[1]))]
    if len(info) == 2:   #no weight
        if info[0] == 'D':   #directed  graph
            for i in range(1, len(lis)):
                start, end = map(lambda x:int(x), lis[i].split())
                tup = (end, 1)
                ans[start].append(tup)
        elif info[0] == 'U': # undirected graph
            for i in range(1, len(lis)):
                start, end = map(lambda x:int(x), lis[i].split())
                tup1 = (end, 1)
                tup2 = (start, 1)
                ans[start].append(tup1)
                ans[end].append(tup2)
    elif len(info) == 3: # have weight
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

def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False for i in range(n)]
    distance = [inf for i in range(n)]
    parent = [None for i in range(n)]
    indegree = [0 for i in range(n)]
    for edges in adj_list:
        for end, weight in edges:
            indegree[end] = indegree[end]+1
    distance[start] = 0
    while check(in_tree, indegree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        if adj_list[u] == []:
            break
        for v, weight in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u]+weight
                parent[v] = u
    return distance, parent

def format_sequence(converters_info_str, start, end):
    """the shortest sequence of formats (and therefore converters)
    required in order to convert a video from the source format to the
    destination format. The details of input and output follow."""        
    if start == end:
        return [end]
    adj_list = adjacency_list(converters_info_str)
    distance, parent = dijkstra(adj_list, start)
    ans = [end]
    now = parent[end]
    if now == None:
        return "No solution!"
    while now != None:
        ans.append(now)
        now = parent[now]
    ans = ans[::-1]
    return ans


 	

converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(format_sequence(converters_info_str, 1, 2))