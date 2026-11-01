from fractions import Fraction
from itertools import product, permutations, combinations

F = Fraction

def det_elim(M):
    n = len(M)
    A = [row[:] for row in M]
    ans = F(1)
    for c in range(n):
        p = next((r for r in range(c,n) if A[r][c]), None)
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            ans = -ans
        pivot = A[c][c]
        ans *= pivot
        for j in range(c,n):
            A[c][j] /= pivot
        for r in range(c+1,n):
            q = A[r][c]
            if q:
                for j in range(c,n):
                    A[r][j] -= q*A[c][j]
    return ans

def parity(perm):
    inv = 0
    for i in range(len(perm)):
        for j in range(i+1,len(perm)):
            inv += perm[i] > perm[j]
    return -1 if inv % 2 else 1

def det_matching(M):
    n = len(M)
    s = F(0)
    for perm in permutations(range(n)):
        t = F(parity(perm))
        for i,j in enumerate(perm):
            t *= M[i][j]
        s += t
    return s

def inv(M):
    n = len(M)
    A = [row[:] + [F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for c in range(n):
        p = next((r for r in range(c,n) if A[r][c]), None)
        assert p is not None
        A[c], A[p] = A[p], A[c]
        q = A[c][c]
        A[c] = [x/q for x in A[c]]
        for r in range(n):
            if r == c:
                continue
            q = A[r][c]
            if q:
                A[r] = [A[r][j]-q*A[c][j] for j in range(2*n)]
    return [row[n:] for row in A]

def stationary(P):
    n = len(P)
    A = [[F(int(i==j))-P[j][i] for j in range(n)] for i in range(n)]
    b = [F(0)]*n
    A[-1] = [F(1)]*n
    b[-1] = F(1)
    Ainv = inv(A)
    return [sum(Ainv[i][j]*b[j] for j in range(n)) for i in range(n)]

def fundamental(P,pi):
    n = len(P)
    M = [[F(int(i==j))-P[i][j]+pi[j] for j in range(n)] for i in range(n)]
    Minv = inv(M)
    return [[Minv[i][j]-pi[j] for j in range(n)] for i in range(n)]

def forest_sum(P, roots, link_i=None, link_root=None):
    n = len(P)
    roots = set(roots)
    nonroots = [v for v in range(n) if v not in roots]
    choices = [[w for w in range(n) if w != v and P[v][w] != 0] for v in nonroots]
    total = F(0)
    number = 0
    for pars in product(*choices):
        parent = dict(zip(nonroots, pars))
        good = True
        for v in nonroots:
            seen = set()
            u = v
            while u not in roots:
                if u in seen or u not in parent:
                    good = False
                    break
                seen.add(u)
                u = parent[u]
            if not good:
                break
        if not good:
            continue
        if link_i is not None:
            u = link_i
            while u not in roots:
                u = parent[u]
            if u != link_root:
                continue
        wt = F(1)
        for v,w in parent.items():
            wt *= P[v][w]
        total += wt
        number += 1
    return total, number

def killed_green(P,A):
    n = len(P)
    B = [v for v in range(n) if v not in A]
    L = [[F(int(i==j))-P[i][j] for j in B] for i in B]
    return B, L, inv(L)

def c3_matrices(P,A,i,j):
    pi = stationary(P)
    Z = fundamental(P,pi)
    A = list(A)
    m = len(A)
    M = [[Z[b][a] for b in A]+[-pi[a]] for a in A]
    M.append([F(1)]*m+[F(0)])
    b = [Z[i][a] for a in A]+[F(1)]
    r = [Z[b0][j] for b0 in A]+[-pi[j]]
    N = [M[k]+[b[k]] for k in range(m+1)]
    N.append(r+[Z[i][j]])
    return M,N

chains = [
    [
        [F(1,2),F(1,2),0,0],
        [F(1,3),F(1,3),F(1,3),0],
        [0,F(1,4),F(1,2),F(1,4)],
        [0,0,F(1,2),F(1,2)]
    ],
    [
        [0,F(1),0,0],
        [0,0,F(1),0],
        [0,0,0,F(1)],
        [F(1),0,0,0],
    ],
    [
        [0,F(2,3),F(1,3),0],
        [F(1,2),0,0,F(1,2)],
        [0,F(1),0,0],
        [F(1,3),0,F(2,3),0],
    ]
]

forest_den_cases = 0
forest_num_cases = 0
c3_ratio_cases = 0
matching_det_cases = 0
source_four_mark_cases = 0
forest_objects_examined = 0

for P in chains:
    n = len(P)
    pi = stationary(P)
    assert sum(pi) == 1
    Z = fundamental(P,pi)
    for i in range(n):
        assert sum(Z[i]) == 0
    for j in range(n):
        assert sum(pi[i]*Z[i][j] for i in range(n)) == 0
    for r in (1,2):
        for A0 in combinations(range(n),r):
            A = set(A0)
            B,L,G = killed_green(P,A)
            den_f,cden = forest_sum(P,A)
            forest_objects_examined += cden
            assert den_f == det_elim(L)
            forest_den_cases += 1
            for i in B:
                for j in B:
                    num_f,cnum = forest_sum(P,A|{j},link_i=i,link_root=j)
                    forest_objects_examined += cnum
                    g = G[B.index(i)][B.index(j)]
                    assert num_f/den_f == g
                    forest_num_cases += 1

                    M,N = c3_matrices(P,A,i,j)
                    d0 = det_elim(M)
                    n0 = det_elim(N)
                    assert d0 != 0
                    assert n0/d0 == g
                    c3_ratio_cases += 1

                    assert det_matching(M) == d0
                    assert det_matching(N) == n0
                    matching_det_cases += 2

                    if len(A)==2 and len({i,j,*A})==4:
                        source_four_mark_cases += 1

print("P26-P02-FOREST-COMPILER-EXACT-CHECK")
print("arithmetic=fractions.Fraction")
print(f"chains={len(chains)}")
print(f"forest_denominator_cases={forest_den_cases}")
print(f"forest_numerator_cases={forest_num_cases}")
print(f"c3_ratio_cases={c3_ratio_cases}")
print(f"matching_determinant_cases={matching_det_cases}")
print(f"source_four_distinct_marks_cases={source_four_mark_cases}")
print(f"accepted_forest_objects_summed={forest_objects_examined}")
print("ALL_EXACT_CHECKS_PASS")
