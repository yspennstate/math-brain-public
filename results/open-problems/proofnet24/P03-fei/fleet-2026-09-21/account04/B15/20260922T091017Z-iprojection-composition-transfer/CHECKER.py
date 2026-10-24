"""Standard-library self-check for the exact I-projection composition transfer.

Reconstructs the actual Boolean witness F=x1 OR (x2 AND x3) on the uniform cube,
computes its conditioned squared spectrum, the maximum-entropy I-projection, and
the hierarchy KL terms in the binary OR/AND decomposition.
"""
from fractions import Fraction
from math import log2, sqrt


def bits(x, n):
    return [(x >> i) & 1 for i in range(n)]


def walsh_raw(vals):
    n = (len(vals)).bit_length() - 1
    out = []
    for s in range(1 << n):
        total = 0
        for x, fx in enumerate(vals):
            parity = ((s & x).bit_count() & 1)
            total += fx * (-1 if parity else 1)
        out.append(total)
    return out


def entropy(P):
    return sum(-p * log2(p) for p in P.values() if p > 0)


def kl(P, Q):
    return sum(p * log2(p / Q[k]) for k, p in P.items() if p > 0)


def zeta_for(r):
    mu = sum(r)
    if abs(mu - 1.0) < 1e-14:
        return 0.0  # boundary handled separately
    lo, hi = 1e-15, 1.0
    def f(z):
        prod = 1.0
        for ri in r:
            prod *= 1.0 - z * ri
        return 1.0 - z - prod
    # f is positive just right of zero and nonpositive at one.
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def q_from_marginals(r):
    n = len(r)
    mu = sum(r)
    if abs(mu - 1.0) < 1e-13:
        return {1 << i: r[i] for i in range(n) if r[i] > 0}
    z = zeta_for(r)
    t = [z * x for x in r]
    Q = {}
    for mask in range(1, 1 << n):
        p = 1.0
        for i, ti in enumerate(t):
            p *= ti if (mask >> i) & 1 else (1.0 - ti)
        Q[mask] = p / z
    return Q


def hmax(r):
    Q = q_from_marginals(r)
    return entropy(Q)


# +1=false, -1=true, little-endian x1,x2,x3.
vals = [1, -1, 1, -1, 1, -1, -1, -1]
raw = walsh_raw(vals)
assert raw == [-2, 6, 2, 2, 2, 2, -2, -2]

sq = {m: Fraction(a * a, 64) for m, a in enumerate(raw)}
v = 1 - sq[0]
P = {m: float(sq[m] / v) for m in range(1, 8)}
assert P[1] == 3 / 5
for m in range(2, 8):
    assert P[m] == 1 / 15
r = [sum(p for m, p in P.items() if (m >> i) & 1) for i in range(3)]
assert all(abs(a-b) < 1e-14 for a,b in zip(r, [4/5, 4/15, 4/15]))

z = zeta_for(r)
z_exact = (35 - 5 * sqrt(34)) / 8
assert abs(z - z_exact) < 2e-14
Q = q_from_marginals(r)
K_direct = kl(P, Q)
K_h = hmax(r) - entropy(P)
assert abs(K_direct - K_h) < 2e-13

# Outer OR conditioned spectral law has masses 3/5,1/5,1/5 on {L},{A},{L,A}.
P0 = {1: 3/5, 2: 1/5, 3: 1/5}
alpha = [4/5, 2/5]
Qalpha = q_from_marginals(alpha)
assert kl(P0, Qalpha) < 2e-14  # every Omega_2 law is its own I-projection

# Global Q induces block activation probabilities u_i.
t_global = [z * ri for ri in r]
u0 = t_global[0]
u1 = 1 - (1 - t_global[1]) * (1 - t_global[2])
# Conditional product law on active blocks under the global I-projection.
QA = {}
for mask in (1, 2, 3):
    p = (u0 if mask & 1 else 1-u0) * (u1 if mask & 2 else 1-u1)
    QA[mask] = p / z
outer_hier = kl(Qalpha, QA)

# AND child: P_i=Q_{r_i}=uniform on the three nonempty subsets, r=(2/3,2/3).
Qr_and = {1: 1/3, 2: 1/3, 3: 1/3}
assert kl(Qr_and, q_from_marginals([2/3, 2/3])) < 2e-14
# Global I-projection induces unconditioned t=z*(4/15) in each AND physical coordinate.
t = z * (4/15)
u = 1 - (1-t)**2
Qi = {
    1: t*(1-t)/u,
    2: t*(1-t)/u,
    3: t*t/u,
}
and_tilt = kl(Qr_and, Qi)
weighted_and = (2/5) * and_tilt
hier = outer_hier + weighted_and
assert abs(hier - K_direct) < 2e-13

print('PASS')
print('Walsh raw =', raw)
print('r =', ['4/5', '4/15', '4/15'])
print('zeta = %.15f' % z)
print('K_occ direct = %.15f' % K_direct)
print('K_occ Hmax-H = %.15f' % K_h)
print('outer hierarchy KL = %.15f' % outer_hier)
print('AND internal tilt KL = %.15f' % and_tilt)
print('weighted AND tilt = %.15f' % weighted_and)
print('hierarchy total = %.15f' % hier)
