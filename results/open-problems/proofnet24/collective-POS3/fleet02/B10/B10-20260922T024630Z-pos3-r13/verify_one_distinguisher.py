from itertools import permutations


def gap_counts(m, d, e):
    # I=[0,m-1], J=[d,m-1+e], with d>=0, e>=0 and d<=m-1+e.
    I = range(m)
    J = range(d, m + e)
    C = D = B = 0
    for ia in I:
        for ib in I:
            for iz in J:
                if ia <= ib <= iz:
                    C += 1   # a<b<z
                if ib <= ia <= iz:
                    B += 1   # b<a<z
                if ia <= iz <= ib:
                    D += 1   # a<z<b
    return C, D, B


tested = 0
for m in range(1, 13):
    for e in range(0, 7):
        for d in range(0, m + e):
            C, D, B = gap_counts(m, d, e)
            assert B == C
            assert D <= C
            tested += 1
print("gap_parameter_cases", tested)

# Tight one-distinguisher three-element poset: a<z, b incomparable to both.
orders = [p for p in permutations(range(3)) if p.index(0) < p.index(2)]
A = sum(p.index(0) < p.index(1) for p in orders)
print("one_distinguisher_tight", len(orders), A, f"{A}/{len(orders)}")
assert (len(orders), A) == (3, 2)

# fleet03/B11 121-extension witness.
n = 8
edges = [(0, 2), (0, 5), (1, 2), (1, 3), (1, 6),
         (2, 4), (3, 4), (3, 5), (5, 7), (6, 7)]
R = [[False] * n for _ in range(n)]
for a, b in edges:
    R[a][b] = True
for k in range(n):
    for i in range(n):
        if R[i][k]:
            for j in range(n):
                if R[k][j]:
                    R[i][j] = True


def is_extension(p):
    pos = [0] * n
    for i, v in enumerate(p):
        pos[v] = i
    return all((not R[i][j]) or pos[i] < pos[j]
               for i in range(n) for j in range(n))


L = [p for p in permutations(range(n)) if is_extension(p)]
num = sum(p.index(3) < p.index(6) for p in L)
dist = []
for z in range(n):
    if z in (3, 6):
        continue
    if (R[z][3], R[3][z]) != (R[z][6], R[6][z]):
        dist.append(z)
print("partner_witness", len(L), num, f"{num}/{len(L)}", "distinguishers", dist)
assert len(L) == 121 and num == 82 and dist == [4, 5]
assert 3 * num > 2 * len(L)
print("POS3_ONE_DISTINGUISHER_BALANCE_REGRESSION_PASS")
