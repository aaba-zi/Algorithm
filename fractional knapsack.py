num_calls = 0  # Global counter of mat_mul calls

def mat_mul(m1, m2):
    """Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       as lists of lists.
    """
    global num_calls # Counter of calls (for marking)
    num_calls += 1   # Increment the count of calls
    n = len(m1)    # Size of the matrix
    assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)]
    return mprod

def mat_power(m, n):
    """returns the result of raising the matrix m to an integer power p"""
    res =  [[0 for i in range(len(m))]for j in range(len(m))]
    flag = True
    for i in range(len(m)):
        res[i][i] = 1
    while (n):
        if n % 2 != 0: #变成二进制
            if flag: 
                res = m
                flag = False
            else:
                res = mat_mul(res, m)
        if n != 1:
            m = mat_mul(m, m)
        n >>= 1 #*2 二进制的右移
    return res
# Simple case of squaring a matrix
m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
print(mat_power(m, 2))