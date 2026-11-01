# T084, agent B: M(K4), disjoint pair (0,5). Dump N by y-monomial and look for an AM-GM certificate for the negative ones:
# a coefficient c_m(q) < 0 is covered by m1 + m2 = 2m with c_m1, c_m2 >= 0 and 4 c_m1 c_m2 >= c_m^2 on (0,1).
import sympy as sp, itertools
from collections import defaultdict
exec(open('exact_pr.py').read().split("\nF7 = ")[0])
exec(open('exact_pr_k4.py').read().split("\nK4 = ")[0].split("import")[0] if False else "")
src = open('exact_pr_k4.py').read(); exec(src[:src.index("K4 = ")])
K4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]; cols = graphic(K4, 4); e, f = 0, 5
n = len(cols); R = rank(cols); free = [i for i in range(n) if i not in (e, f)]
Z = {}
for ie in (0, 1):
    for jf in (0, 1):
        d = defaultdict(int)
        for m in range(1 << len(free)):
            A = [free[k] for k in range(len(free)) if m >> k & 1] + ([e] if ie else []) + ([f] if jf else [])
            d[(m, R - rank([cols[i] for i in A]))] += 1
        Z[(ie, jf)] = d
N = defaultdict(lambda: defaultdict(int))
def acc(P, Q, sgn):
    for (m1, c1), a in P.items():
        for (m2, c2), b in Q.items():
            key = tuple(((m1 >> k) & 1) + ((m2 >> k) & 1) for k in range(len(free)))
            N[key][c1 + c2] += sgn * a * b
acc(Z[(1, 0)], Z[(0, 1)], 1); acc(Z[(1, 1)], Z[(0, 0)], -1)
q = sp.symbols('q'); C = {k: sp.expand(sum(c * q**j for j, c in v.items())) for k, v in N.items()}
C = {k: v for k, v in C.items() if v != 0}
def neg_somewhere(P):
    xs = [sp.Rational(i, 200) for i in range(1, 200)]; return min(P.subs(q, x) for x in xs) < 0
print("free edges", [K4[i] for i in free])
for k in sorted(C): print(k, sp.factor(C[k]), "NEG" if neg_somewhere(C[k]) else "")
bad = [k for k in C if neg_somewhere(C[k])]
for m in bad:
    opts = []
    for m1 in C:
        m2 = tuple(2 * a - b for a, b in zip(m, m1))
        if m1 < m2 and m2 in C and not neg_somewhere(C[m1]) and not neg_somewhere(C[m2]):
            D = sp.expand(4 * C[m1] * C[m2] - C[m] ** 2)
            ok = all(D.subs(q, sp.Rational(i, 400)) >= 0 for i in range(1, 400) if C[m].subs(q, sp.Rational(i, 400)) < 0)
            opts.append((m1, m2, ok))
    print("negative", m, "pairings:", opts)
