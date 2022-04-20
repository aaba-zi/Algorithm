import copy

def is_solution(candidate):#check whether is it  finished
    n = len(candidate)
    for i, row in enumerate(candidate):
        col = []
        for j in range(n):
            col.append(candidate[j][i])
            if candidate[i][j] == None:#���candidate������None��϶�����Ҫ������һ��
                return False
            if row.count(i) > 1:#ÿһ�в��ܳ�����ͬ������
                return False
        if col.count(i) > 1:#ÿһ�в��ܳ�����ͬ������
            return False
    return True

def children(candidate):#���еĿ�����
    n = len(candidate)
    ans = []#���Ĵ�
    for i in range(n):#��
        k = 0
        for j in range(n):#��
            if candidate[i][j] == None:
                for k in range(n):#Ҫ�����
                    temp = copy.deepcopy(candidate)
                    col = [row[j] for row in candidate]
                    if k not in candidate[i] and k not in col:#�Ƚ�k�����к�����
                        temp[i][j] = k #����
                        ans.append(temp)
            if k == n-1:#����ÿ��ֻ��һ��None���� ��Ҫbreak
                break
        if k == n-1:#break
            break
    return ans
                    
                

def should_prune(candidate):#��֦
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
