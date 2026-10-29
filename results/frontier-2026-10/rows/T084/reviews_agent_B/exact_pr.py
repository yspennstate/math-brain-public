# T084, agent B: exact Potts-Rayleigh test on a binary matroid at one pair (e,f).
# Z(A) = q^{corank(A)} y^A. N = Z10*Z01 - Z11*Z00 (subscripts: e in A, f in A), summed over A in E-{e,f}.
# Collect N by monomial in the free y (exponents 0..2) -> polynomial in q with integer coefficients.
# Sufficient check: after q = s/(1+s), times (1+s)^d, all coefficients in s >= 0  (=> >= 0 on (0,1)).
# If that fails, count real roots in (0,1) exactly with sympy and test sign at midpoints.
import itertools, sys, json
from collections import defaultdict
import sympy as sp

def rank(vecs):
    piv = {}
    for v in vecs:
        while v:
            h = v.bit_length() - 1
            if h in piv: v ^= piv[h]
            else: piv[h] = v; break
    return len(piv)

def run(name, cols, e, f):
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
    q, s = sp.symbols('q s')
    nz = bad = polya_fail = 0; worst = None
    for key, poly in N.items():
        P = sp.Poly(sum(c * q**k for k, c in poly.items()), q)
        if P.is_zero: continue
        nz += 1
        d = P.degree(); S = sp.Poly(sum(c * s**k * (1+s)**(d-k) for k, c in poly.items() if c), s)
        if min(S.all_coeffs()) >= 0: continue
        polya_fail += 1
        roots = sorted(r for r in sp.real_roots(P) if 0 < r < 1)
        pts = [sp.Rational(1, 2)] if not roots else [(a + b) / 2 for a, b in zip([0] + roots, roots + [1])]
        vals = [P.eval(x) for x in pts]
        if min(vals) < 0:
            bad += 1; worst = (key, str(P.as_expr()), [float(x) for x in pts], [float(v) for v in vals])
    out = dict(matroid=name, pair=(e, f), monomials=nz, polya_inconclusive=polya_fail, negative_somewhere=bad, example=worst)
    print(json.dumps(out)); sys.stdout.flush(); return out

F7 = [1, 2, 4, 3, 5, 6, 7]
AG32 = [8 | v for v in range(8)]   # affine 3-space over GF(2): points (1, v), v in GF(2)^3
F7d = None
if __name__ == '__main__':
    run('F7', F7, 0, 1)
    run('AG(3,2)', AG32, 0, 1)
    # control: the unbalanced rank-4 binary matroid [I4|A], A rows 0111/1011/1101/1111; its basis-failing pair is (3,7) (s8_bases.txt); (0,4) and (0,7) below are balanced pairs
    A = [0b0111, 0b1011, 0b1101, 0b1111]
    cols = [1, 2, 4, 8] + [sum(((A[r] >> (3 - c)) & 1) << r for r in range(4)) for c in range(4)]
    for e, f in [(0, 4), (0, 7)]:
        run('control', cols, e, f)
