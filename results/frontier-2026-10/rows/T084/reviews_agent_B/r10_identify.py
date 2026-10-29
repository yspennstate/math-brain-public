# T084, agent B: identify R10's 8-element rank-4 minor with 45 bases: circuit-size counts and series/parallel pairs,
# compared with M(W4) and with K4 with one edge doubled and another subdivided (graphic, built directly).
import itertools, json
from collections import Counter
exec(open('minor_check.py').read().split("check('AG(3,2)'")[0])
src = open('exact_pr_k4.py').read(); exec(src[:src.index("K4 = ")])
def profile(cols):
    n = len(cols); r = rank(cols); circ = Counter()
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            if rank([cols[i] for i in S]) == k - 1 and all(rank([cols[i] for i in T]) == k - 1 for T in itertools.combinations(S, k - 1)): circ[k] += 1
    bases = sum(1 for B in itertools.combinations(range(n), r) if rank([cols[i] for i in B]) == r)
    return dict(n=n, rank=r, bases=bases, circuits=dict(sorted(circ.items())))
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
e, f = 0, 1; C = Npoly(colsR10, e, f); free = [i for i in range(10) if i not in (e, f)]
for m, c in C.items():
    if str(sp.factor(c)) == '-(q - 1)*(q**3 + 5*q**2 + 3*q - 2)':
        D = [free[k] for k, a in enumerate(m) if a == 2]; S = [free[k] for k, a in enumerate(m) if a == 1]
        red = contract(colsR10, D); sub = [red[i] for i in S] + [red[e], red[f]]
        print(json.dumps(dict(which='R10 minor', **profile(sub)))); break
W4 = [(0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(4,1)]
print(json.dumps(dict(which='M(W4)', **profile(graphic(W4, 5)))))
K4ds = [(0,1),(0,1),(0,2),(0,3),(1,2),(1,4),(4,3),(2,3)]  # K4, edge 01 doubled, edge 13 subdivided by vertex 4
print(json.dumps(dict(which='K4 doubled+subdivided', **profile(graphic(K4ds, 5)))))
cw = graphic(W4, 5)
for e2, f2 in itertools.combinations(range(8), 2):
    Cw = Npoly(cw, e2, f2); top = Cw.get(tuple([1] * 6), 0)
    print('W4 pair', W4[e2], W4[f2], 'top coefficient', sp.factor(top))
