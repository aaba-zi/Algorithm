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

def check(state):
    for ss in state:
        if ss == 'U':
            return True
    return False

def next_connected(state):
    for i, ss in enumerate(state):
        if ss == 'U':
            return i
    
def bubbles(physical_contact_info):
    adj_list = adjacency_list(physical_contact_info)
    n = len(adj_list)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    ans = []#all connected
    while check(state):
        start = next_connected(state)
        #print(start)
        state[start] = 'D'     
        dfs_loop(adj_list, start, state, parent)
        temp = []#ocnnected for now
        for i in range(n):
            if state[i] == 'P':
                temp.append(i)
                state[i] = 'F'#as we add connected vertices in the ans, we are not add again, change state
        #print(state)
        ans.append(temp)
    return ans

def dfs_loop(adj_list, u, state, parent):
    for edge in adj_list[u]:
        v = edge[0]
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = u
            dfs_loop(adj_list, v, state, parent)
    state[u] = 'P'

physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

                