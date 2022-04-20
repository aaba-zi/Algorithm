import copy

def is_solution(candidate):#check whether is it  finished
    n = len(candidate)
    for i, row in enumerate(candidate):
        col = []
        for j in range(n):
            col.append(candidate[j][i])
            if candidate[i][j] == None:#如果candidate里面有None则肯定还需要进行下一步
                return False
            if row.count(i) > 1:#每一行不能出现相同的数字
                return False
        if col.count(i) > 1:#每一列不能出现相同的数字
            return False
    return True

def children(candidate):#所有的可能性
    n = len(candidate)
    ans = []#最后的答案
    for i in range(n):#行
        k = 0
        for j in range(n):#列
            if candidate[i][j] == None:
                for k in range(n):#要填的数
                    temp = copy.deepcopy(candidate)
                    col = [row[j] for row in candidate]
                    if k not in candidate[i] and k not in col:#比较k不在行和列中
                        temp[i][j] = k #可填
                        ans.append(temp)
            if k == n-1:#由于每次只填一个None所以 需要break
                break
        if k == n-1:#break
            break
    return ans
                    
                

def should_prune(candidate):#剪枝
    pass

def latin_squares(square):
    """Given a square (matrix) computes and returns Latin squares
    that can be obtained by replacing Nones with digits."""
    solutions = []
    dfs_backtrack(square, solutions)
    return solutions


def dfs_backtrack(candidate, output_data):
    #if should_prune(candidate):       
        #return
    if is_solution(candidate):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate):
            dfs_backtrack(child_candidate, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(copy.deepcopy(candidate))


def square_from_str(square_str):
    """Takes a string representation of a square and returns a matrix                                                                                                              
    (list of lists) representation where blanks are replaced with None."""
    return [[None if c == '-' else int(c) for c in line.strip()] for
            line in square_str.splitlines()]

def square_to_str(square):
    """Returns the string representation of the given square matrix."""
    return '\n'.join(''.join(str(c) for c in row) for row in square)

square_str = """\
01
-1
"""

square = [
    [0,    1],
    [None, 0],
]


solutions = latin_squares(square)
print("Number of solutions:", len(solutions))
for solution in solutions:
    print(square_to_str(solution))
