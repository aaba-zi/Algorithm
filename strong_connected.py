def adjacency_list(graph_str):
    lis = graph_str.split("\n")
    lis.pop() # remove tha last line of "\n"
    info = lis[0].split() #first line shows info
    result = [[] for i in range(int(info[1]))]
    if len(info) == 2: # does not have weight
        if info[0] == "D": # directed
            for i in range(1, len(lis)):
                start, end = map(lambda x:int(x), lis[i].split())
                temp = (end, None)
                result[start].append(temp)
        elif info[0] == "U": # undirected
            for i in range(1, len(lis)):
                start, end = map(lambda x:int(x), lis[i].split())
                temp1 = (end, None)
                temp2 = (start, None)
                result[start].append(temp1)   
                result[end].append(temp2) 
        
    elif len(info) == 3:#has weight
        if info[0] == "D": # directed
            for i in range(1, len(lis)):
                start, end, weight = map(lambda x:int(x), lis[i].split())
                temp = (end, weight)
                result[start].append(temp)            
        elif info[0] == "U": # undirected        
            for i in range(1, len(lis)):
                start, end, weight = map(lambda x:int(x), lis[i].split())
                temp1 = (end, weight)
                temp2 = (start, weight)
                result[start].append(temp1)   
                result[end].append(temp2)             
    return result

def dfs_tree(adj_list, start):
    n = len(adj_list)
    state = ['U' for i in range(n)]
    parent = [None for i in range(n)]
    state[start] = 'D'
    dfs_loop(adj_list, start, state, parent)
    return state

def dfs_loop(adj_list, u, state, parent):
    for edge in adj_list[u]:
        v = edge[0]
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = u
            dfs_loop(adj_list, v, state, parent)
    state[u] = 'P'
    
def transpose(graph_adj_list):
    ans = [[] for i in range(len(graph_adj_list))]
    for i, edges in enumerate(graph_adj_list):
        for edge in edges:# i mean index, edge mean every edge in edges
            start = i
            end = edge[0]
            tup = (start, edge[1])
            ans[end].append(tup)
    return ans

def is_strongly_connected(adj_list):
    state1 = dfs_tree(adj_list, 0) #step 1  
    for state in state1:     
        if state != 'P':
            return False           #step 2
    adj_list1 = transpose(adj_list)    
    state2 = dfs_tree(adj_list1, 0)#step 3
    for state in state2:     
        if state != 'P':
            return False           #step 4.1
    return True  