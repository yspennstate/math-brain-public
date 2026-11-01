"""Independent exact source-review fixtures; no author checker imported."""
import json
import time
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from check import walsh, spectrum, influence_edges, entropy, ck, embed, bitdot
import check

start = time.monotonic()
parents = terminal_count = states = moments = 0
for m in [1, 2, 3, 4]:
    parents += 1
    g = [(-1 if ((y & 1) and ((y >> 1).bit_count() % 2)) else 1) for y in range(1 << m)]
    root = [(-1 if bitdot(x,y) else 1)*g[y] for y in range(1 << m) for x in range(1 << m)]
    ck(all(p == F(1, len(root)) for p in spectrum(root)), 'A032 parent flat')
    for k in range(m):
        for K0 in combinations(range(1,m), k):
            K = list(K0); J = [j for j in range(m) if j not in K]
            for t in range(1 << k):
                states += 1
                v = [(-1 if bitdot(embed(u,J)|embed(t,K),y) else 1)*g[y]
                     for y in range(1 << m) for u in range(1 << len(J))]
                p = spectrum(v)
                ck(entropy(p) == {2:F(2*(m-k))}, 'A032 every intermediate entropy')
                ck(all(influence_edges(v,j) == F(1,2) for j in range(2*m-k)), 'A032 every intermediate influence')
                if k == m-1:
                    terminal_count += 1
                    expect = [F(0)]*len(v)
                    R = [F(0)]*len(v)
                    for A in [0,1]:
                        for B in [0,1]:
                            label = A | (B << 1)
                            for j in range(1,m):
                                label |= (A ^ ((t >> (j-1)) & 1)) << (j+1)
                            expect[label] = F(1,4)
                            if A: R[label] = F(1,2)
                    ck(p == expect, 'A032 exact four atoms ALL terminals')
                    ck(entropy(R) == {2:F(1)}, 'A032 extremizer full KL=1')
                    deterministic = 0
                    for j in range(m+1):
                        q = sum(R[s] for s in range(len(R)) if (s >> j)&1)
                        deterministic += int(q in [0,1])
                    ck(deterministic == m, 'A032 sum marginal KL=m')
for n in [4,6,8]:
    M = 1 << n; k = n-1; epsilon = F(1, 1 << (4*n))
    p = [F(1,M)]*M
    q = p.copy()
    for V in range(1 << k):
        q[(1 << k)|V] *= 1 + (1-epsilon)*(-1 if V.bit_count()%2 else 1)
    ck(sum(q)==1 and min(q)>0, 'A097 normalized covering rational reference')
    ck(q[0]==p[0], 'A097 vacuum')
    ck(1 < 2-epsilon < 2, 'A097 exact strict log bracket')
    counts = {epsilon:0, 2-epsilon:0, F(1):0}
    for z in range(M): counts[q[z]/p[z]] += 1
    ck(counts[epsilon] == M//4 == counts[2-epsilon], 'A097 loss coefficients')
    for U in range(M):
        if U.bit_count() <= n-2:
            moments += 1
            ck(sum(q[s] for s in range(M) if s & U == U) == F(1,1 << U.bit_count()), 'A097 all promised inclusion moments')
    for i in range(k):
        ck(all(q[s]+q[s ^ (1<<i)] == F(2,M) for s in range(M) if not (s >> i)&1), 'A097 all claimed projected fibers')
    actual = [(-1 if sum(((x >> (2*j))&3)==0 for j in range(n//2))%2 else 1) for x in range(M)]
    ck(spectrum(actual)==p, 'A097 actual Boolean tensor')
    ck(all(influence_edges(actual,i)==F(1,2) for i in range(n)), 'A097 physical influences')
out={'status':'PASS','A032_parents':parents,'A032_all_partial_states':states,'A032_full_terminals':terminal_count,
     'A097_dimensions':[4,6,8],'A097_matched_inclusion_moments':moments,'assertions':check.CHECKS,
     'seconds':time.monotonic()-start,'acceptance':'A032 flat-parent@1 and A097 high-moment@1 unchanged named scopes only'}
Path(__file__).resolve().parents[1].joinpath('out/REVIEW.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
