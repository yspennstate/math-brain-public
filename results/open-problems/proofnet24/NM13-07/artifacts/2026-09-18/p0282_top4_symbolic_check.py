#!/usr/bin/env python3
"""Exact symbolic certificate for the P0282 top-four boundary theorem.

All algebra uses SymPy over ZZ/QQ. RSK fixed-defect counts are derived from the
hook-length formula using residual partitions mu |- j. The finite pre-stable
values are recomputed independently from the Young-lattice branching rule.
"""

from math import factorial
import sympy as sp

n, m = sp.symbols('n m', integer=True)


def partitions(t, max_part=None):
    if t == 0:
        yield ()
        return
    if max_part is None or max_part > t:
        max_part = t
    for first in range(max_part, 0, -1):
        for rest in partitions(t-first, min(first, t-first)):
            yield (first,) + rest


def hook_dimension_small(mu):
    j = sum(mu)
    hooks = 1
    for i, row in enumerate(mu):
        for c0 in range(row):
            below = sum(1 for r in range(i+1, len(mu)) if mu[r] > c0)
            hooks *= (row-c0) + below
    return factorial(j) // hooks


def fixed_defect_dimension(j, mu):
    """f^(n-j,mu), valid whenever n-j >= mu_1."""
    fmu = hook_dimension_small(mu)
    expr = (sp.prod(n-r for r in range(j)) / factorial(j)) * fmu
    if mu:
        for c in range(1, mu[0] + 1):
            col_height = sum(1 for a in mu if a >= c)
            a = n - j - c + 1
            expr *= sp.Rational(1, 1) * a / (a + col_height)
    return sp.factor(sp.cancel(expr))


def E(j):
    if j == 0:
        return sp.Integer(1)
    return sp.factor(sp.cancel(sum(fixed_defect_dimension(j, mu)**2 for mu in partitions(j))))

Evals = [sp.expand(E(j)) for j in range(6)]
expected = [
    1,
    (n-1)**2,
    (n**4-6*n**3+11*n**2-6*n+2)/2,
    (n**6-12*n**5+52*n**4-98*n**3+79*n**2-22*n+6)/6,
    (n**8-20*n**7+158*n**6-628*n**5+1329*n**4-1448*n**3+708*n**2-100*n+24)/24,
    (n**10-30*n**9+375*n**8-2540*n**7+10163*n**6-24542*n**5+34945*n**4-27060*n**3+9236*n**2-548*n+120)/120,
]
for j in range(6):
    assert sp.simplify(Evals[j] - expected[j]) == 0, j

# Plancherel coefficient identity behind the fixed-defect asymptotic.
for j in range(1, 9):
    assert sum(hook_dimension_small(mu)**2 for mu in partitions(j)) == factorial(j)
    assert sp.LC(sp.Poly(E(j), n)) == sp.Rational(1, factorial(j))

M3 = sp.factor(Evals[3]**2 - Evals[2]*Evals[4])
M4 = sp.factor(Evals[4]**2 - Evals[3]*Evals[5])
Q3 = sp.expand(144*M3/(n*(n-1)))
Q4 = sp.expand(2880*M4/(n*(n-1)))

Q3_expected = (
    n**10-17*n**9+108*n**8-262*n**7-277*n**6+3149*n**5
    -7708*n**4+9146*n**3-5420*n**2+1136*n+24
)
Q4_expected = (
    n**14-31*n**13+401*n**12-2687*n**11+8375*n**10+6735*n**9
    -173389*n**8+760643*n**7-1844708*n**6+2785348*n**5-2657512*n**4
    +1566312*n**3-538720*n**2+88176*n+288
)
assert sp.expand(Q3-Q3_expected) == 0
assert sp.expand(Q4-Q4_expected) == 0

Q3_shift = sp.Poly(sp.expand(Q3.subs(n, m+8)), m)
Q4_shift = sp.Poly(sp.expand(Q4.subs(n, m+10)), m)
assert all(c > 0 for c in Q3_shift.all_coeffs())
assert all(c > 0 for c in Q4_shift.all_coeffs())

# Independent exact RSK counts in the pre-stable ranges via Young branching.
def predecessor_sum(lam, prev):
    total = 0
    for i, a in enumerate(lam):
        nxt = lam[i+1] if i+1 < len(lam) else 0
        if a > nxt:
            if a == 1 and i == len(lam)-1:
                pred = lam[:-1]
            else:
                pred = lam[:i] + (a-1,) + lam[i+1:]
            total += prev[pred]
    return total

prev = {(): 1}
ells = {}
for nn in range(1, 11):
    cur = {}
    ell = [0]*(nn+1)
    for lam in partitions(nn):
        f = predecessor_sum(lam, prev)
        cur[lam] = f
        ell[lam[0]] += f*f
    assert sum(ell) == factorial(nn)
    ells[nn] = ell
    prev = cur


def margin(nn, defect):
    k = nn-defect
    ell = ells[nn]
    return ell[k]**2 - ell[k-1]*ell[k+1]

small_j3 = {nn: margin(nn, 3) for nn in (5,6,7)}
small_j4 = {nn: margin(nn, 4) for nn in (6,7,8,9)}
assert small_j3 == {5:1620, 6:121450, 7:2334269}
assert small_j4 == {6:16780, 7:4658836, 8:220720864, 9:4136767056}
assert all(v > 0 for v in small_j3.values())
assert all(v > 0 for v in small_j4.values())

# Fixed-defect limiting ratio from leading coefficients.
for j in range(1, 8):
    lead_jm1 = sp.Rational(1, factorial(j-1))
    lead_j = sp.Rational(1, factorial(j))
    lead_jp1 = sp.Rational(1, factorial(j+1))
    ratio = sp.factor(lead_j**2/(lead_jm1*lead_jp1))
    assert ratio == sp.Rational(j+1, j)

print("P0282 exact symbolic boundary certificate")
for j, ej in enumerate(Evals):
    print(f"E_{j}(n)={sp.factor(ej)}")
print(f"M3_factor={M3}")
print(f"Q3_shift_n_eq_m_plus_8={sp.expand(Q3.subs(n,m+8))}")
print(f"small_j3_margins={small_j3}")
print(f"M4_factor={M4}")
print(f"Q4_shift_n_eq_m_plus_10={sp.expand(Q4.subs(n,m+10))}")
print(f"small_j4_margins={small_j4}")
print("fixed_defect_asymptotic=E_j(n)=n^(2j)/j!+O_j(n^(2j-1))")
print("fixed_defect_ratio_limit=(j+1)/j")
print("scope_guard=proves source inequality at defects j=3,4 for all valid n; combined with prior report gives top four interior positions")
print("ALL_EXACT_CHECKS_PASS")
