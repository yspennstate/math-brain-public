# T084, agent B: R12 (Oxley's reduced matrix), checked regular by a totally unimodular signing, then the adversarial search.
import numpy as np, itertools
A = np.array([[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,1,0],[0,1,0,0,0,1],[0,0,1,0,1,1],[0,0,0,1,1,1]])
ones = [tuple(x) for x in np.argwhere(A)]
def tu(S):
    for k in range(1, 7):
        for r in itertools.combinations(range(6), k):
            for c in itertools.combinations(range(6), k):
                if abs(round(np.linalg.det(S[np.ix_(r, c)]))) > 1: return False
    return True
# spanning forest of the bipartite row-column graph gets +1; try every sign on the remaining entries
par = list(range(12)); f = lambda x: x if par[x] == x else f(par[x]); tree = []
for (i, j) in ones:
    a, b = f(i), f(6 + j)
    if a != b: par[a] = b; tree.append((i, j))
free = [e for e in ones if e not in tree]; ok = None
for sg in itertools.product((1, -1), repeat=len(free)):
    S = A.astype(float).copy()
    for e, s in zip(free, sg): S[e] = s
    if tu(S): ok = S; break
print("ones", len(ones), "free signs", len(free), "TU signing found:", ok is not None)
src = open('adversarial_weights.py').read(); exec(src.split("\nK5 = ")[0])
cols = [1 << i for i in range(6)] + [int(sum(int(A[i, j]) << i for i in range(6))) for j in range(6)]
rk = ranks(cols, 12); print("rank", rk[-1], "bases", sum(1 for s in range(1 << 12) if bin(s).count('1') == 6 and rk[s] == 6))
search('R12', rk, 12, starts=12)
