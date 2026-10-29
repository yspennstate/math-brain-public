# T084, agent B: exact AM-GM certificate search for N = Z10 Z01 - Z11 Z00 >= 0 (all y > 0, q in (0,1)).
# For every monomial whose coefficient c_m(q) goes negative on (0,1), find a pair m1 + m2 = 2m of monomials with c >= 0 on (0,1) and
# 4 c_m1 c_m2 >= c_m^2 wherever c_m < 0 (exact: the difference factored, sign checked on every interval between its real roots).
# Each positive monomial may serve one negative (a disjoint assignment); report whether one exists.
import sympy as sp, sys, json
from collections import defaultdict
exec(open('exact_pr.py').read().split("\nF7 = ")[0])
q = sp.symbols('q')
def nonneg01(P, where=None):
    P = sp.Poly(P, q)
    if P.is_zero: return True
    rts = sorted(set([0] + [r for r in sp.real_roots(P) if 0 < r < 1] + [1]))
    for a, b in zip(rts, rts[1:]):
        x = (a + b) / 2
        if where is not None and where.subs(q, x) >= 0: continue
        if P.eval(x) < 0: return False
    return True
def Npoly(cols, e, f):
    n = len(cols); R = rank(cols); free = [i for i in range(n) if i not in (e, f)]; Z = {}
    for ie in (0, 1):
        for jf in (0, 1):
            d = defaultdict(int)
            for m in range(1 << len(free)):
                A = [free[k] for k in range(len(free)) if m >> k & 1] + ([e] if ie else []) + ([f] if jf else [])
                d[(m, R - rank([cols[i] for i in A]))] += 1
            Z[(ie, jf)] = d
    N = defaultdict(lambda: defaultdict(int))
    for (P, Q, sg) in ((Z[(1, 0)], Z[(0, 1)], 1), (Z[(1, 1)], Z[(0, 0)], -1)):
        for (m1, c1), a in P.items():
            for (m2, c2), b in Q.items():
                N[tuple(((m1 >> k) & 1) + ((m2 >> k) & 1) for k in range(len(free)))][c1 + c2] += sg * a * b
    C = {k: sp.expand(sum(c * q**j for j, c in v.items())) for k, v in N.items()}
    return {k: v for k, v in C.items() if v != 0}
def certify(name, cols, e, f):
    C = Npoly(cols, e, f); neg = [m for m in C if not nonneg01(C[m])]; pos = set(m for m in C if m not in neg)
    cand = {}
    for m in neg:
        cand[m] = []
        for m1 in pos:
            m2 = tuple(2 * a - b for a, b in zip(m, m1))
            if m1 < m2 and m2 in pos and nonneg01(4 * C[m1] * C[m2] - C[m] ** 2, where=C[m]): cand[m].append((m1, m2))
    # disjoint assignment by backtracking
    order = sorted(neg, key=lambda m: len(cand[m])); used = set(); pick = {}
    def bt(i):
        if i == len(order): return True
        m = order[i]
        for (m1, m2) in cand[m]:
            if m1 in used or m2 in used: continue
            used.update((m1, m2)); pick[m] = (m1, m2)
            if bt(i + 1): return True
            used.difference_update((m1, m2)); del pick[m]
        return False
    ok = bt(0)
    out = dict(matroid=name, pair=(e, f), monomials=len(C), negative=len(neg), with_candidates=sum(1 for m in neg if cand[m]),
               certificate=ok, assignment={str(m): [str(a), str(b)] for m, (a, b) in pick.items()} if ok else None,
               uncovered=[(str(m), str(sp.factor(C[m]))) for m in neg if not cand[m]][:6])
    print(json.dumps(out)); sys.stdout.flush(); return out
if __name__ == '__main__':
    src = open('exact_pr_k4.py').read(); exec(src[:src.index("K4 = ")])
    K4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    certify('M(K4) disjoint', graphic(K4, 4), 0, 5)
    certify('F7', [1, 2, 4, 3, 5, 6, 7], 0, 1)
    certify('F7', [1, 2, 4, 3, 5, 6, 7], 0, 3)
