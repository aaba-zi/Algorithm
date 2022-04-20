def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions

def is_solution(candidate, input_data):#whether it is ended
    if len(candidate) == len(input_data):
        return True
    else:
        return False

def children(candidate, input_data): #put all possibilities
    cand = list(candidate)
    ans = []
    for i in input_data:
        temp = [j for j in cand]
        if i not in candidate:
            temp.append(i)
            ans.append(tuple(temp))
    return ans
            

def dfs_backtrack(candidate, input_data, output_data):
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            #print(input_data)
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate): #¼ôÖ¦
    return False



print(sorted(permutations({'a'})))



