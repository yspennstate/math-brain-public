# T084, agent B: is the R12 matrix in r12_check.py non-graphic and non-cographic? Look for 9-element minors with
# 81 bases and 9 four-circuits: rank 5 = M(K3,3) signature, rank 4 = M*(K3,3) signature (the dual: 9 4-element cocircuits).
import itertools, numpy as np
src = open('adversarial_weights.py').read(); exec(src.split("\nK5 = ")[0])
A = np.array([[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,1,0],[0,1,0,0,0,1],[0,0,1,0,1,1],[0,0,0,1,1,1]])
cols = [1 << i for i in range(6)] + [int(sum(int(A[i, j]) << i for i in range(6))) for j in range(6)]
rk = ranks(cols, 12); found = {}
for rem in itertools.combinations(range(12), 3):
    keep = [e for e in range(12) if e not in rem]
    for cmask in range(8):
        C = sum(1 << rem[i] for i in range(3) if cmask >> i & 1); rc = rk[C]
        def r(X): return rk[sum(1 << keep[i] for i in range(9) if X >> i & 1) | C] - rc
        R = r(511)
        bases = sum(1 for X in range(512) if bin(X).count('1') == R and r(X) == R)
        if bases != 81: continue
        circ4 = sum(1 for X in itertools.combinations(range(9), 4) if r(sum(1 << i for i in X)) == 3 and all(r(sum(1 << i for i in X if i != y)) == 3 for y in X))
        cocirc4 = sum(1 for X in itertools.combinations(range(9), 4) if r(511 & ~sum(1 << i for i in X)) == R - 1 and all(r(511 & ~sum(1 << i for i in X if i != y)) == R for y in X))
        key = (R, circ4, cocirc4); found[key] = found.get(key, 0) + 1
print("9-element minors with 81 bases, by (rank, #4-circuits, #4-cocircuits):", found)
