# T084, agent B: which minors of R10 give its negative coefficients at pair (0,1)? For each distinct negative polynomial,
# one monomial: |S|, the minor M' = (M/D)\Z on S + {e,f} (rank, bases, simple? e,f parallel/series?), and its column vectors.
import json, itertools
MARK = chr(10) + 'if __name__ =='
exec(open('minor_check.py').read().split("check('AG(3,2)'")[0])
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
e, f = 0, 1; C = Npoly(colsR10, e, f); free = [i for i in range(10) if i not in (e, f)]; seen = {}
for m, c in C.items():
    if nonneg01(c): continue
    key = str(sp.factor(c))
    if key in seen: seen[key]['count'] += 1; continue
    D = [free[k] for k, a in enumerate(m) if a == 2]; S = [free[k] for k, a in enumerate(m) if a == 1]
    red = contract(colsR10, D); sub = [red[i] for i in S] + [red[e], red[f]]; n = len(sub); r = rank(sub)
    bases = sum(1 for B in itertools.combinations(range(n), r) if rank([sub[i] for i in B]) == r)
    loops = sum(v == 0 for v in sub); par = sum(1 for i, j in itertools.combinations(range(n), 2) if sub[i] == sub[j] and sub[i])
    seen[key] = dict(count=1, size_S=len(S), minor_elements=n, rank=r, bases=bases, loops=loops, parallel_pairs=par,
                     e_f_in_3circuit=any(rank([sub[n-2], sub[n-1], sub[k]]) == 2 for k in range(n - 2)))
for k, v in seen.items(): print(json.dumps(dict(poly=k, **v)))
