def in_map(p, n, m):
    return p[0] >= 0 and p[1] >= 0 and p[0] < n and p[1] < m

def sum_mat(M, function=(lambda x:x)):
    s = 0
    for line in M:
        for cell in line:
            s += function(cell)
    return s