#!/usr/bin/env python3
"""Independent reconstruction of B12's child-only terminal-reserve no-go.

The finite sign is certified by exact rational prime exponents.  Decimal
arithmetic is used only to display values and to diagnose the analytic tensor
formulas, not to decide the strict finite inequality.
"""

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from math import lcm

getcontext().prec = 90
D = Decimal
LN2 = D(2).ln()

U = (-1, 1, -1, -1, -1, -1, 1, -1,
     1, 1, 1, -1, 1, -1, 1, -1)
V = (1, -1, -1, 1, -1, 1, 1, -1,
     -1, 1, 1, -1, 1, -1, -1, 1)


def fwht(values):
    a = [Q(x) for x in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x / len(a) for x in a]


def caps(p):
    a = list(p)
    n = len(a).bit_length()-1
    for j in range(n):
        bit = 1 << j
        for s in range(1 << n):
            if not s & bit:
                a[s] += a[s | bit]
    return a


def dec(q):
    return D(q.numerator) / D(q.denominator)


def U_decimal_from_coeffs(coeffs):
    p = [x*x for x in coeffs]
    c = caps(p)
    return sum((dec(x) * (dec(y/x).ln()/LN2) for x, y in zip(p, c) if x), D(0))


def kron(a, b):
    return [x*y for x in a for y in b]


def tensor(a, k):
    out = [Q(1)]
    for _ in range(k):
        out = kron(out, a)
    return out


def prime_factors(n):
    out = defaultdict(int)
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] += 1
            n //= p
        p += 1
    if n > 1:
        out[n] += 1
    return out


class LogExpr:
    def __init__(self):
        self.c = defaultdict(Q)

    def add(self, weight, argument):
        assert argument > 0
        for p, e in prime_factors(argument.numerator).items():
            self.c[p] += weight*e
        for p, e in prime_factors(argument.denominator).items():
            self.c[p] -= weight*e

    def plus(self, other, scale=Q(1)):
        for p, x in other.c.items():
            self.c[p] += scale*x
        return self

    def scaled(self, q):
        z = LogExpr()
        z.c.update({p:q*x for p, x in self.c.items()})
        return z

    def decimal(self):
        return sum((dec(x)*D(p).ln()/LN2 for p, x in self.c.items()), D(0))


def entropy_expr(atoms, upper_caps=None):
    cs = caps(atoms) if upper_caps is None else upper_caps
    e = LogExpr()
    for p, c in zip(atoms, cs):
        if p:
            e.add(p, c/p)
    return e


uh, vh = fwht(U), fwht(V)
assert uh == [Q(x, 8) for x in (-1,3,1,-3,1,-3,3,-1,-3,-3,-1,-1,-1,-1,1,1)]
assert vh == [Q(0)]*15 + [Q(1)]
p = [x*x for x in uh]
C = caps(p)
A = sum((x/y for x, y in zip(p, C)), Q())
rho = sum((x*y for x, y in zip(uh, vh)), Q())
assert A == Q(6911, 960)
assert rho == Q(1, 8)


def base_theta_expr(mu):
    a = [(x+y)/2 for x, y in zip(uh, vh)]
    b = [(y-x)/2 for x, y in zip(uh, vh)]
    b2 = [x*x for x in b]
    beta = sum(b2, Q())
    alpha2 = 1-mu*mu
    c2 = [(x+mu*y)**2 for x, y in zip(a, b)]
    mixed = [x+alpha2*y for x, y in zip(c2, b2)]
    e = entropy_expr(c2, caps(mixed))
    e.plus(entropy_expr(b2), alpha2)
    if mu:
        q = mu*mu
        psi = LogExpr()
        psi.add(q, 1/q)
        e.plus(psi, -beta)
    return e


# Exact six-physical-input witness (four untouched outer bits, two child bits).
mu = Q(-1, 2)
tm, tp, tmu = base_theta_expr(Q(-1)), base_theta_expr(Q(1)), base_theta_expr(mu)
centered = LogExpr().plus(tmu).plus(tm, -Q(1-mu, 2)).plus(tp, -Q(1+mu, 2))
beta = (1-rho)/2
ratio = centered.scaled(1/(beta*(1-mu*mu)))

den = 1
for x in ratio.c.values():
    den = lcm(den, x.denominator)
exponents = {p:int(x*den) for p, x in ratio.c.items() if x}
exponents[2] = exponents.get(2, 0)-4*den
left = right = 1
for prime, e in exponents.items():
    if e >= 0:
        left *= prime**e
    else:
        right *= prime**(-e)
assert left > right
assert den == 336
assert left.bit_length() == 3358 and right.bit_length() == 3340

# Reconstruct the composed Boolean truth table directly.
h = (-1, -1, -1, 1)  # mean -1/2
F = []
for mask in range(64):
    child = mask & 3
    z = mask >> 2
    F.append(V[z] if h[child] == 1 else U[z])
Fhat = fwht(F)
F_u = U_decimal_from_coeffs(Fhat)
h_u = U_decimal_from_coeffs(fwht(h))


def theta_decimal(ucoeff, vcoeff, bias):
    a = [(x+y)/2 for x, y in zip(ucoeff, vcoeff)]
    b = [(y-x)/2 for x, y in zip(ucoeff, vcoeff)]
    b2 = [x*x for x in b]
    beta0 = sum(b2, Q())
    alpha2 = 1-bias*bias
    c = [x+bias*y for x, y in zip(a, b)]
    c2 = [x*x for x in c]
    mixed = [x+alpha2*y for x, y in zip(c2, b2)]
    val = sum((dec(x)*(dec(y/x).ln()/LN2) for x, y in zip(c2, caps(mixed)) if x), D(0))
    val += dec(alpha2)*U_decimal_from_coeffs(b)
    if bias:
        q = bias*bias
        val -= dec(beta0*q)*(dec(1/q).ln()/LN2)
    return val

assert abs(F_u-(dec(beta)*h_u+theta_decimal(uh, vh, mu))) < D("1e-80")


def endpoint_ratio(ucoeff, vcoeff):
    a = [(x+y)/2 for x, y in zip(ucoeff, vcoeff)]
    b = [(y-x)/2 for x, y in zip(ucoeff, vcoeff)]
    b2 = [x*x for x in b]
    beta0 = sum(b2, Q())
    pu = [x*x for x in ucoeff]
    cu = caps(pu)
    cp = caps([2*x*y for x, y in zip(a, b)])
    derivative = D(0)
    for c0, b0, p0, cap0, capprime in zip(ucoeff, b, pu, cu, cp):
        if not p0:
            continue
        pprime = 2*c0*b0
        derivative += dec(pprime)*(dec(cap0/p0).ln()/LN2)
        derivative += dec(p0)*(dec(capprime/cap0-pprime/p0))/LN2
    derivative += D(2)*U_decimal_from_coeffs(b)-D(2)*dec(beta0)/LN2
    L = derivative+(U_decimal_from_coeffs(ucoeff)-U_decimal_from_coeffs(vcoeff))/D(2)
    return L/(D(2)*dec(beta0)), beta0


endpoint = []
source = []
for k in range(1, 4):
    uk, vk = tensor(uh, k), tensor(vh, k)
    qk, betak = endpoint_ratio(uk, vk)
    assert betak == (1-rho**k)/2
    proved = (dec(A**k)-D(3))/(D(2)*LN2)-D(2*k)
    assert qk >= proved
    endpoint.append((k, qk, proved))

    n = 8*k
    rare = Q(1, 1 << n)
    bias = -1+2*rare
    th = theta_decimal(uk, vk, bias)
    thm = theta_decimal(uk, vk, Q(-1))
    thp = theta_decimal(uk, vk, Q(1))
    overline = th-dec(1-bias)*thm/D(2)-dec(1+bias)*thp/D(2)
    child_I = Q(n*2, 1 << n)
    direct_ratio = overline/(dec(betak)*dec(child_I))
    q = 1-rare
    bracket = dec(q*(A**k-1))/(D(2)*LN2)-D(4*k)-D(2)/LN2
    lower = bracket/D(8*k)
    assert direct_ratio >= lower
    source.append((k, direct_ratio, lower))

# Check every rational premise used for the all-k source-influence bound.
for k in range(1, 41):
    rare = Q(1, 1 << (8*k))
    q = 1-rare
    # C_T >= 64^{-k}, so x=r/(qC_T) is at most this quantity.
    xmax = rare*(64**k)/q
    assert xmax <= Q(1, 2)

print("B19 independent review of B12 tensor reserve no-go")
print(f"rho={rho} A={A} A_gt_7={A>7}")
print(f"finite_ratio={ratio.decimal()}")
print(f"finite_ratio_gt_4_exact={left>right} denominator={den}")
print(f"integer_bit_lengths={left.bit_length()},{right.bit_length()}")
print(f"direct_composition_inputs=6 direct_chain_rule_error={abs(F_u-(dec(beta)*h_u+theta_decimal(uh,vh,mu)))}")
for k, value, bound in endpoint:
    print(f"endpoint k={k} direct={value} proved_lower={bound}")
for k, value, bound in source:
    print(f"source k={k} direct={value} proved_lower={bound}")
print("analytic_source_premises_checked_k=1..40")
print("verdict=ACCEPT_CHILD_ONLY_NO_GO_AT_DECLARED_SCOPE")
print("full_fei=OPEN")
print("PASS")
