"""Exact checks of the shared-data multiplexer theorem.
All 256 ordered pairs of Boolean functions on two shared data variables are covered.
Rational prime-log signatures check entropy identities without floating-point logs.
Finite checks supplement, and do not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import comb, gcd
from collections import defaultdict
import json


def fwht(a):
    a = list(a)
    step = 1
    while step < len(a):
        for base in range(0, len(a), step * 2):
            for j in range(step):
                u, v = a[base + j], a[base + j + step]
                a[base + j], a[base + j + step] = u + v, u - v
        step *= 2
    return a


def fourier(a):
    return [F(v, len(a)) for v in fwht(a)]


def factor(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def entropy_signature(probabilities):
    """Return exact rational coefficients of log_2(prime) in the entropy."""
    out = defaultdict(F)
    for p in probabilities:
        p = F(p)
        if not p:
            continue
        assert 0 < p <= 1
        for prime, power in factor(p.numerator).items():
            out[prime] -= p * power
        for prime, power in factor(p.denominator).items():
            out[prime] += p * power
    return {p: c for p, c in out.items() if c}


def add(*terms):
    out = defaultdict(F)
    for scale, sig in terms:
        for p, c in sig.items():
            out[p] += scale * c
    return {p: c for p, c in out.items() if c}


def nonnegative(sig):
    """Exact sign: clear rational exponents and compare positive integers."""
    den = 1
    for c in sig.values():
        den = den * c.denominator // gcd(den, c.denominator)
    num, div = 1, 1
    for p, c in sig.items():
        power = int(c * den)
        if power >= 0:
            num *= p ** power
        else:
            div *= p ** (-power)
    return num >= div


def Hhat(a):
    return entropy_signature(v * v for v in a)


def I2(a):
    return sum((F(j.bit_count()) * v * v for j, v in enumerate(a)), F(0))


def sign(bit):
    return 1 if bit else -1


results = {}
funcs = [[sign((mask >> x) & 1) for x in range(4)] for mask in range(16)]
pairs, orthogonal = 0, 0
for g in funcs:
    gh = fourier(g)
    for h in funcs:
        hh = fourier(h)
        # Selector is the least significant input bit.
        f = [g[x >> 1] if not (x & 1) else h[x >> 1] for x in range(8)]
        fh = fourier(f)
        rhs = add((1, {2: F(1)}), (F(1, 2), Hhat(gh)), (F(1, 2), Hhat(hh)))
        for t, (u, v) in enumerate(zip(gh, hh)):
            r = (u * u + v * v) / 2
            assert fh[2 * t] == (u + v) / 2
            assert fh[2 * t + 1] == (u - v) / 2
            if r:
                post = [u * u / (2 * r), v * v / (2 * r)]
                nu = [fh[2 * t] ** 2 / r, fh[2 * t + 1] ** 2 / r]
                assert sum(post) == sum(nu) == 1
                rhs = add((1, rhs), (r, entropy_signature(nu)), (-r, entropy_signature(post)))
        assert Hhat(fh) == rhs, (g, h, Hhat(fh), rhs)
        upper = add((1, {2: F(2)}), (F(1, 2), Hhat(gh)), (F(1, 2), Hhat(hh)))
        assert nonnegative(add((1, upper), (-1, Hhat(fh))))
        selector = F(sum(u != v for u, v in zip(g, h)), 4)
        assert I2(fh) == (I2(gh) + I2(hh)) / 2 + selector
        if sum(u * v for u, v in zip(g, h)) == 0:
            orthogonal += 1
            assert selector == F(1, 2)
            assert nonnegative(add((1, {2: 4 * I2(fh)}), (-1, Hhat(fh))))
        pairs += 1
results['all_two_variable_branch_pairs'] = {'pairs': pairs, 'orthogonal_pairs': orthogonal,
    'exact_collision_identity': 'PASS', 'exact_entropy_inequality': 'PASS',
    'exact_influence_identity': 'PASS'}

results["status"] = "PASS"
results["arithmetic"] = "Exact rational spectra and prime-log signatures; integer comparisons."
results["scope"] = "All two-variable branch pairs; finite verification, not a proof for all dimensions."
print(json.dumps(results, indent=2))
