"""Recompute Section 5, all table rows, and independent cross-checks."""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import signal
import time
import resource
import math
from pathlib import Path
import numpy as np
import mpmath as mp

signal.alarm(240)
started = time.monotonic()
mp.mp.dps = 60
lines = []


def say(s):
    print(s, flush=True)
    lines.append(s)


def harmonic(n):
    return float(mp.harmonic(n))


def window(n, L):
    # u[k]=a(n,n-k); only the L+1 relevant states are stored.
    H = np.array([harmonic(n - 1 - k) for k in range(L + 1)])
    u = np.zeros(L + 1)
    u[0] = 1
    reciprocal = 1.0 / np.arange(1, L + 1)
    for k in range(1, L + 1):
        u[k] = np.dot(u[:k] / H[:k], reciprocal[k-1::-1])
    return u, H


def window_mp(n, L):
    H = [mp.harmonic(n - 1)]
    for k in range(1, L + 1):
        H.append(H[-1] - mp.mpf(1) / (n - k))
    u = [mp.mpf(1)]
    for k in range(1, L + 1):
        u.append(mp.fsum(u[r] / ((k - r) * H[r]) for r in range(k)))
    return mp.fsum(u[1:])


n = 4000
h = np.concatenate(([0.0], np.cumsum(1.0 / np.arange(1, n))))
a = np.zeros(n + 1)
a[n] = 1
for i in range(n - 1, 0, -1):
    m = np.arange(i + 1, n + 1)
    a[i] = np.dot(a[i+1:] / h[i:n], 1.0 / (m - i))
# A second algorithm: propagate mass from each state down to all destinations.
b = np.zeros(n + 1)
b[n] = 1
for m in range(n, 1, -1):
    b[1:m] += b[m] / (h[m-1] * np.arange(m-1, 0, -1))
say("n=4000 reverse-recursion / forward-flow max absolute difference: %.3g" % np.max(np.abs(a-b)))
i = np.arange(2, n + 1)
g = (i - 1) / h[1:n]
alim = 6 / math.pi**2 * h[1:n] / (i - 1)
drift = np.dot(a[2:], g)
limit_drift = np.dot(alim, g)
say("drift occupation sum: %.13f; exact target: 3999" % drift)
say("drift limit sum: %.13f; ratio: %.15f; pi^2/6: %.15f" % (limit_drift, drift/limit_drift, math.pi**2/6))
say("linear occupation sum: %.12f; n log n: %.12f" % (np.dot(a[2:], i), n*math.log(n)))
say("linear limit sum: %.12f; (6/pi^2)n log n: %.12f" % (np.dot(alim, i), 6/math.pi**2*n*math.log(n)))
eligible = n >= i + i//2
ratios = a[2:][eligible] / alim[eligible]
arg = int(i[eligible][np.argmax(ratios)])
say("max a(4000,i)/a(i) subject to Cor2.4(a): %.12f, at i=%d" % (np.max(ratios), arg))
say("Table1: n L V lower upper applicable [60-digit V when cross-checked]")
for power, L in [(9,56), (10,64), (14,1024), (16,4096), (18,16384),
                  (22,16384), (30,16384), (40,16384)]:
    n = 2**power
    u, H = window(n,L)
    v = math.fsum(u[1:])
    lam = math.log(8*n/L)
    lower = H[0]/(10*lam)
    upper = harmonic(L)/(H[-1]-harmonic(L))
    applicable = H[0] >= 2*lam
    extra = ""
    if power in [9,10,14]:
        vm = window_mp(n,L)
        extra = " mp=" + mp.nstr(vm,26) + " error=" + mp.nstr(abs(vm-v),5)
        assert abs(vm-v) < mp.mpf('1e-12')
    assert v <= upper
    if applicable:
        assert v >= lower
    say(f"2^{power} {L} {v:.12f} {lower:.12f} {upper:.12f} {applicable}{extra}")
# Re-derive the limit linear sum using a closed identity for sum h_k/k.
n=4000
hh=mp.harmonic(n-1)
second=mp.fsum(mp.mpf(1)/(k*k) for k in range(1,n))
linear_limit=6/mp.pi**2*(n*hh-(n-1)+(hh*hh+second)/2)
say("independent closed-identity linear limit n=4000: " + mp.nstr(linear_limit,30))
say(f"Elapsed seconds: {time.monotonic() - started:.3f}")
say(f"Peak resident bytes (macOS): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}; inherited nice: {os.getpriority(os.PRIO_PROCESS, 0)}")
Path("audit_numerics.out").write_text("\n".join(lines)+"\n")
