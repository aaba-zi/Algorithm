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