"""Checks for 'Hub paths in the barely subcritical configuration model'.

Run: python checks.py   (needs sympy). Every printed line is cited in the paper by its tag.
The proofs in the paper do not depend on these computations; they check the exact identities, the
integrality of the two families, the size of the error terms at concrete parameters, and the
combinatorial inequality Y^2 <= 2Y + D_0 by exhaustive enumeration on a small degree sequence.
"""
import math
from fractions import Fraction as Fr
from itertools import permutations

import sympy as sp

ok = True


def report(tag, cond, msg):
    global ok
    ok &= bool(cond)
    print(f"[{tag}] {'PASS' if cond else 'FAIL'}  {msg}")


def fall(a, k):
    z = 1
    for i in range(k):
        z *= a - i
    return z


def pairs_prod(ell, r):
    """P_r = prod_{j<r} (ell - 2j - 1)."""
    z = 1
    for j in range(r):
        z *= ell - 2 * j - 1
    return z


# ---------------------------------------------------------------- I: exact identities (symbolic)
n, M, d, y, N1, N3, r1, r3, C, H, ell, eps = sp.symbols('n M d y N1 N3 r1 r3 C H ell eps')
N3e = n / 4 - (d - 1)**2 * M / 4 - y
N1e = n - N3e - M
elle = N1e + 3 * N3e + d * M
excess = N1e * 1 * (1 - 2) + N3e * 3 * (3 - 2) + M * d * (d - 2)        # sum_i d_i (d_i - 2)
report('I1', sp.expand(excess + 4 * y) == 0, "sum_i d_i(d_i-2) = -4y, i.e. ell*eps = 4y exactly")
report('I2', sp.expand(elle - (n + 2 * N3e + (d - 1) * M)) == 0, "ell = n + 2 N_3 + (d-1) M (parity)")
report('I3', sp.expand(elle - (3 * n / 2 - (d - 1)**2 * M / 2 - 2 * y + (d - 1) * M)) == 0,
       "ell = 3n/2 - (d-1)^2 M/2 - 2y + (d-1)M")
# compensated drift (4.1): sleeping and active contributions to E[Delta C] times B_t
lhs = -(N1 - r1) + 3 * (N3 - r3) - 2 * d * (M - H) - 2 * (C + d * H - 1)
rhs = -ell * eps - M * d**2 + r1 - 3 * r3 - 2 * C + 2
report('I4', sp.expand((lhs - rhs).subs(ell * eps, N1 - 3 * N3 - d * (d - 2) * M)) == 0,
       "compensated drift numerator: -(N1-r1)+3(N3-r3)-2d(M-H)-2(A-1) = -ell eps - M d^2 + r1 - 3 r3 - 2C + 2")
# drift of A (3.1): sum over all non-seed vertices of d_v(d_v-2) splits as sleeping + discovered
k = sp.symbols('k', integer=True)
report('I5', all(kk * (kk - 2) >= -1 for kk in range(1, 200)), "k(k-2) >= -1 for every positive integer k (k < 200 shown; (k-1)^2 >= 0)")
report('I6', all(kk * (kk - 2)**2 <= kk**3 for kk in range(1, 200)), "k(k-2)^2 <= k^3 for k >= 1 (k < 200 shown)")


# ---------------------------------------------------------------- the family of Theorem 1
def family(nn, MM, dd, yy, K):
    assert nn % 4 == 0 and ((dd - 1)**2 * MM) % 4 == 0
    n3 = nn // 4 - (dd - 1)**2 * MM // 4 - yy
    n1 = nn - n3 - MM
    L = n1 + 3 * n3 + dd * MM
    e = Fr(4 * yy, L)
    w = dd**2 * (dd * (dd - 1))**(K - 2)
    mu = Fr(fall(MM, K) * w, pairs_prod(L, K - 1))
    ED0 = Fr(fall(MM, 2 * K) * w * w, pairs_prod(L, 2 * K - 2))
    return dict(n3=n3, n1=n1, L=L, eps=e, mu=mu, ED0=ED0)


def conditions(nn, MM, dd, K, f):
    e = f['eps']
    third = Fr(f['n1'] + 27 * f['n3'] + dd**3 * MM, nn)
    q = nn * e**3
    log_ne3 = math.log(q.numerator) - math.log(q.denominator)
    return dict(
        nonneg=f['n1'] > 0 and f['n3'] > 0, even=f['L'] % 2 == 0,
        eps=float(e), third=float(third), hub_third=float(Fr(MM * dd**3, nn)),
        n_eps3=log_ne3 / math.log(10), H_over_E=float(dd * e) / log_ne3,
        c3a=float(Fr(K * K * dd * dd, nn) / e), c3b=float(Fr(K * MM * dd * dd, nn) / e),
        mu=float(f['mu']), d0_ratio=float(f['ED0'] / f['mu']**2))


# Example A: d = m^2, M = m^(3K-2), n = 8 m^(3K+5), y = 3n/(8m), so ell*eps = 3n/(2m).
for m, K in [(16, 2), (64, 2), (1024, 2), (2**16, 2), (2**20, 3), (2**40, 4)]:
    nn, MM, dd = 8 * m**(3 * K + 5), m**(3 * K - 2), m * m
    yy = 3 * nn // (8 * m)
    f = family(nn, MM, dd, yy, K)
    c = conditions(nn, MM, dd, K, f)
    good = c['nonneg'] and c['even'] and 4 * yy == Fr(3 * nn, 2 * m)
    report(f'A{m}_{K}', good,
           f"m={m} K={K}: eps*m={c['eps']*m:.6f}  E[D^3]={c['third']:.6f}  M d^3/n={c['hub_third']:.2e}  "
           f"log10(n eps^3)={c["n_eps3"]:.1f}  H/E={c['H_over_E']:.3e}  K^2d^2/(n eps)={c['c3a']:.2e}  "
           f"KMd^2/(n eps)={c['c3b']:.2e}  mu={c['mu']:.6g} (m/12^(K-1)={m/12**(K-1):.6g})  ED0/mu^2={c['d0_ratio']:.12f}")

# Example B: s odd, d = s^20, M = s^31, n = 4 s^100, y = ceil(e_s n); eps = 4y/ell ~ 8 e_s/3 as e_s -> 0, K = 2.
for s, es_name, es in [(11, 's^-10', Fr(1, 11**10)), (101, 's^-10', Fr(1, 101**10)),
                       (1001, 's^-10', Fr(1, 1001**10)), (1001, '1/(100 log s)', 1 / (100 * math.log(1001))),
                       (10**6 + 1, '1/(100 log log s)', 1 / (100 * math.log(math.log(10**6 + 1))))]:
    nn, MM, dd, K = 4 * s**100, s**31, s**20, 2
    yy = math.ceil(Fr(es) * nn)
    f = family(nn, MM, dd, yy, K)
    c = conditions(nn, MM, dd, K, f)
    good = c['nonneg'] and c['even']
    report(f'B{s}', good,
           f"s={s} e_s={es_name}: eps={c['eps']:.4e} (4e_s/(3/2-2e_s)={4*float(es)/(1.5-2*float(es)):.4e})  E[D^3]={c['third']:.6f}  "
           f"M d^3/n={c['hub_third']:.2e}  H/E={c['H_over_E']:.3e}  K^2d^2/(n eps)={c['c3a']:.2e}  "
           f"KMd^2/(n eps)={c['c3b']:.2e}  mu={c['mu']:.6g} (M^2 d^2/ell={float(Fr(MM*MM*dd*dd, f['L'])):.6g})  ED0/mu^2={c['d0_ratio']:.12f}")

# ---------------------------------------------------------------- W: exhaustive check of (5.1) and of the moment formulas
# Ten half-edges: four hubs of degree 2 (vertices 0-3), two leaves (4, 5). 9!! = 945 perfect matchings.
owners = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5]


def matchings(xs):
    if not xs:
        yield []
        return
    a = xs[0]
    for i in range(1, len(xs)):
        for rest in matchings(xs[1:i] + xs[i + 1:]):
            yield [(a, xs[i])] + rest


for K in (2, 3):
    total = sz = sd = 0
    ineq = True
    for prs in matchings(list(range(10))):
        adj = [[] for _ in range(6)]
        for a, b in prs:
            u, v = owners[a], owners[b]
            adj[u].append(v)
            adj[v].append(u)
        tree = {}
        for u in range(6):
            if u in tree:
                continue
            seen, stack = {u}, [u]
            while stack:
                v = stack.pop()
                for w_ in adj[v]:
                    if w_ not in seen:
                        seen.add(w_)
                        stack.append(w_)
            good = sum(v < 4 for v in seen) == K and sum(len(adj[v]) for v in seen) == 2 * (len(seen) - 1)
            for v in seen:
                tree[v] = good
        wit = []
        for order in permutations(range(4), K):
            mult = 1
            for u, v in zip(order, order[1:]):
                mult *= adj[u].count(v)
            wit.extend([order] * mult)
        Y = sum(tree[w_[0]] for w_ in wit)
        D0 = sum(not (set(a) & set(b)) for a in wit for b in wit)
        ineq &= Y * Y <= 2 * Y + D0
        total += 1
        sz += len(wit)
        sd += D0
    w = 2**2 * (2 * 1)**(K - 2)
    ez = Fr(fall(4, K) * w, pairs_prod(10, K - 1))
    ed = Fr(fall(4, 2 * K) * w * w, pairs_prod(10, 2 * K - 2))
    report(f'W{K}', total == 945 and ineq and Fr(sz, total) == ez and Fr(sd, total) == ed,
           f"K={K}: {total} matchings; Y^2 <= 2Y + D_0 in every one; E Z = {Fr(sz, total)} = (M)_K w/P_(K-1) = {ez}; "
           f"E D_0 = {Fr(sd, total)} = {ed}")

print('ALL CHECKS PASS' if ok else 'SOME CHECK FAILED')
