"""Independent finite audit of the preceding tree result; standard library only."""
from fractions import Fraction as F
from itertools import product
from math import comb, prod
import os
import resource
import signal
import time

signal.alarm(120)
start = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"


def survive(bs):
    t = F(1)
    for b in bs[::-1]:
        t = 1 - (1 - t / 2)**b
    return t


def law(bs):
    dist = {1: F(1)}
    for b in bs:
        nxt = {}
        for z, mass in dist.items():
            for j in range(b*z + 1):
                nxt[j] = nxt.get(j, F(0)) + mass * F(comb(b*z, j), 2**(b*z))
        dist = nxt
    return dist


moments = prefixes = horizons = 0
for n in range(6):
    for bs in product((1, 2), repeat=n):
        d = law(bs)
        means = [F(1)] + [prod(F(b, 2) for b in bs[:i]) for i in range(1, n+1)]
        q = 1 - d.get(0, F(0))
        assert q == survive(bs)
        assert sum(z*z*v for z, v in d.items()) / means[-1]**2 == 1 + sum(1/m for m in means[1:])/2
        for b in (1, 2):
            qnext = survive(bs + (b,))
            assert 0 <= 1/qnext - 1/q <= 1/means[-1]
            horizons += 1
        for m in range(n+1):
            prefix = law(bs[:m])
            t = survive(bs[m:])
            g = {z: 1-(1-t)**z for z in prefix}
            assert sum(v*g[z] for z, v in prefix.items()) == q
            tv = sum(v*abs(g[z]/q-z/means[m]) for z, v in prefix.items())/2
            k = sum(v*F(z*(z-1), 2) for z, v in prefix.items())
            assert tv <= k*t/means[m]
            prefixes += 1
        moments += 1
print(f"PASS: {moments} tree distributions and second moments; {prefixes} prefix/TV checks; {horizons} horizon checks")

# Check the mixture identity directly, allowing attachment edges to be open
# even when their branches fail to survive.
unions = 0
for qa, qb in product((F(1, 32), F(1, 3), F(3, 4)), repeat=2):
    u, v = qa/2, qb/2
    a = u*v/(u+v)
    for ea, eb, sa, sb in product((0, 1), repeat=4):
        base = F(1, 4)*(qa if sa else 1-qa)*(qb if sb else 1-qb)
        U, V = bool(ea and sa), bool(eb and sb)
        mu = base*int(U or V)/(u+v-u*v)
        mix = base*(int(U)+int(V))/(u+v)
        both = base*int(U and V)/(u*v)
        assert mix == (1-a)*mu + a*both
        unions += 1
print(f"PASS: {unions} union-mixture atom identities")

# Second derivation of the increment constant: optimize over relative
# survival factors directly rather than using reciprocal maps.
increments = 0
for eps in (F(1, 64), F(1, 4), F(2)):
    lo = 1/(1+eps)
    for w, ra, rb in product((F(j, 16) for j in range(17)), (lo, (1+lo)/2, F(1)), (lo, (1+lo)/2, F(1))):
        delta = abs(w*ra/(w*ra+(1-w)*rb)-w)
        assert delta <= eps*w*(1-w) <= eps/4
        increments += 1
print(f"PASS: {increments} mixture-weight increment inequalities")

da = db = 0
for k in range(1, 65):
    if k % 2:
        da += 2*k-1
    else:
        db += 2*k-1
    assert da-db == (-1)**(k+1)*k
    assert da+db == k*k
    n = 2**(k*k+10)
    prev = 0 if k == 1 else 2**((k-1)**2+10)
    L = n-prev-(2*k-1)
    assert L >= F(n, 2)
    assert F(4*(n+1), L+4) / 2**k <= F(16, 2**k)
    if k >= 2:
        prevprev = 0 if k == 2 else 2**((k-2)**2+10)
        oldL = prev-prevprev-(2*k-3)
        eps = F(8*2**(2*k-1), prev)
        assert eps == F(2)**(-k*k+4*k-9)
        assert F(4*2**(2*k-1), oldL) <= eps
        assert eps/4 == F(2)**(-k*k+4*k-11)
print("PASS: 64 stage certificates, endpoint dominance and adjacent-increment exponents")
assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS={os.environ['OMP_NUM_THREADS']}")
print(f"Elapsed seconds: {time.monotonic()-start:.3f}")
print(f"Peak RSS bytes (macOS): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
print("PASS: preceding result holds in all finite checks; infinite conclusions checked analytically in LOG.md")
