# T084, agent B: independent audit of the AM-GM certificates. (1) N rebuilt from Z by direct evaluation at random rational
# (q, y) and compared with the monomial expansion; (2) every assigned triple: 4 c1 c2 - c^2 factored, sign on (0,1) read from the
# factors and on a 1/1000 grid; (3) every unassigned monomial: coefficient >= 0 on the grid and factored.
import sympy as sp, random, itertools, json
from fractions import Fraction as Fr
exec(open('amgm_cert.py').read().split("if __name__")[0])
src = open('exact_pr_k4.py').read(); exec(src[:src.index("K4 = ")])
def direct_N(cols, e, f, qv, yv):
    n = len(cols); R = rank(cols); free = [i for i in range(n) if i not in (e, f)]
    def Zs(ie, jf):
        t = Fr(0)
        for m in range(1 << len(free)):
            A = [free[k] for k in range(len(free)) if m >> k & 1] + ([e] if ie else []) + ([f] if jf else [])
            w = Fr(1)
            for k in range(len(free)):
                if m >> k & 1: w *= yv[k]
            t += w * qv ** (R - rank([cols[i] for i in A]))
        return t
    return Zs(1, 0) * Zs(0, 1) - Zs(1, 1) * Zs(0, 0)
grid = [sp.Rational(i, 1000) for i in range(1, 1000)]
def audit(name, cols, e, f, assign):
    C = Npoly(cols, e, f); random.seed(1); errs = 0
    for _ in range(5):
        qv = Fr(random.randint(1, 99), 100); yv = [Fr(random.randint(1, 50), 7) for _ in range(len(cols) - 2)]
        val = Fr(0)
        for m, c in C.items():
            cv = sp.Poly(c, q).eval(sp.Rational(qv.numerator, qv.denominator)); w = Fr(int(cv.p), int(cv.q))
            for k, a in enumerate(m): w *= yv[k] ** a
            val += w
        errs += val != direct_N(cols, e, f, qv, yv)
    used = set(); ok = True; disc = {}
    for m, (m1, m2) in assign.items():
        m, m1, m2 = eval(m), eval(m1), eval(m2); used |= {m, m1, m2}
        assert tuple(a + b for a, b in zip(m1, m2)) == tuple(2 * a for a in m)
        D = sp.factor(4 * C[m1] * C[m2] - C[m] ** 2); disc[str(m)] = str(D)
        ok &= all(C[m1].subs(q, x) >= 0 and C[m2].subs(q, x) >= 0 and (C[m].subs(q, x) >= 0 or D.subs(q, x) >= 0) for x in grid)
    rest = [m for m in C if m not in used]; ok_rest = all(C[m].subs(q, x) >= 0 for m in rest for x in grid[::10])
    print(json.dumps(dict(matroid=name, pair=(e, f), expansion_mismatches=errs, triples_ok=bool(ok), rest_ok=bool(ok_rest),
                          rest_factors=sorted(set(str(sp.factor(C[m])) for m in rest)), discriminants=disc)), flush=True)
K4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for line in open('amgm_cert.txt').read().splitlines() + open('amgm_more.txt').read().splitlines():
    r = json.loads(line); cols = {'M(K4) disjoint': graphic(K4, 4), 'F7': [1, 2, 4, 3, 5, 6, 7], 'AG(3,2)': [8 | v for v in range(8)]}[r['matroid']]
    audit(r['matroid'], cols, *r['pair'], r['assignment'])
