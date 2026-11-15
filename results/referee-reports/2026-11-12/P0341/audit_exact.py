"""Independent rational and 60-decimal checks; no author code is used."""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import time
import signal
import resource
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import mpmath as mp

signal.alarm(240)
started = time.monotonic()
mp.mp.dps = 60
lines = []
counts = Counter()


def say(s):
    print(s, flush=True)
    lines.append(s)


def check(label, condition):
    counts[label] += 1
    if not condition:
        raise AssertionError(label)


def harmonic_exact(n):
    h = [F(0)]
    for k in range(1, n + 1):
        h.append(h[-1] + F(1, k))
    return h


def occupation(n, h, zero, one):
    a = [zero for _ in range(n + 1)]
    a[n] = one
    for i in range(n - 1, 0, -1):
        a[i] = sum((a[m] / ((m - i) * h[m - 1])
                    for m in range(i + 1, n + 1)), zero)
    return a


h = harmonic_exact(80)
A = {n: occupation(n, h, F(0), F(1)) for n in range(2, 41)}
for n, a in A.items():
    check("absorption", a[1] == 1)
    check("Prop1.3(a) drift identity", sum(a[i] * (i - 1) / h[i - 1]
                                             for i in range(2, n + 1)) == n - 1)
    # The second identity after multiplying by pi^2/6 is exactly rational.
    check("Prop1.3(a) limit identity", sum(h[i - 1] / (i - 1) *
                                              (i - 1) / h[i - 1]
                                              for i in range(2, n + 1)) == n - 1)
    for r in range(2, n + 1):
        check("(4.2) below-r drift", sum(a[i] * (i - 1) / h[i - 1]
                                           for i in range(2, r + 1)) <= r - 1)
    for L in range(1, (n - 2) // 2 + 1):
        v = sum(a[n - L:n])
        check("Lemma2.1", v <= h[L] / (h[n - L - 1] - h[L]))
    for i in range(2, n + 1):
        for t in range(min(i - 1, n - i) + 1):
            check("Lemma2.3 first", a[i] <= h[i] / ((t + 1) * (h[i] - h[t])))
            if t:
                check("Lemma2.3 second", a[i] <= h[t] / (t * (h[i] - h[t])))
        if n >= i + i // 2:
            check("Cor2.4(a) first", a[i] <= 4 * h[i] / i)
            check("Cor2.4(a) second", 4 * h[i] / i <= 6 * h[i - 1] / (i - 1))
        for eps in [F(1, 100), F(1, 10), F(1, 4), F(1, 3), F(1, 2)]:
            if n - i >= eps * n:
                check("Cor2.4(b)", a[i] <= 3 * h[i - 1] / (eps * (i - 1)))
for i in range(2, 21):
    for t in range(i):
        check("Lemma2.2", sum(A[ell][i] for ell in range(i, i + t + 1))
              <= h[i] / (h[i] - h[t]))
        if t:
            check("Remark2.6 independent renewal bound", A[i + t][i] <=
                  1 / (t * h[i] * (1 - h[t - 1] / h[i])**2))
for n in range(4, 31):
    for L in range(1, n - 1):
        v = sum(A[n][n - L:n])
        for y in range(1, L + 1):
            q = h[y] / h[n - 1]
            for T in [1, 2, 3, 4, 8, 16, 40]:
                check("Lemma3.1", v >= T * (q**T - T * y / (L * h[n - L - 1])))
say("EXACT FRACTIONS: all checks passed; n=2..40; Lemma2.2 i=2..20, all t<i; Lemma3.1 n=4..30, all L,y, T=1,2,3,4,8,16,40.")
for label, count in sorted(counts.items()):
    say(f"  {label}: {count}")
say("Exact samples: a(4,2)=" + str(A[4][2]) + ", a(4,3)=" + str(A[4][3]))

# Grid of admissible Corollary 3.2 parameters, evaluated at 60 decimal digits.
for n in [144, 160, 256, 512, 1024]:
    hm = [mp.mpf(0)]
    for k in range(1, n):
        hm.append(hm[-1] + mp.mpf(1) / k)
    a = occupation(n, hm, mp.mpf(0), mp.mpf(1))
    for L in sorted(set([8, n // 8, n // 4, n // 3, n // 2])):
        lam = mp.log(mp.mpf(8) * n / L)
        if hm[n - 1] < 2 * lam:
            continue
        v = mp.fsum(a[n - L:n])
        lower = hm[n - 1] / (10 * lam)
        check("Cor3.2 60-digit", v >= lower >= mp.log(n) / (10 * lam))
        T, y = int(mp.floor(hm[n - 1] / lam)), (L + 7) // 8
        q = hm[y] / hm[n - 1]
        lower31 = T * (q**T - T * y / (L * hm[n - L - 1]))
        check("Lemma3.1 60-digit positive bound", v >= lower31 > lower)
        say(f"Cor3.2 n={n}, L={L}: V={float(v):.12f}, bound={float(lower):.12f}, Lemma3.1={float(lower31):.12f}")
say(f"Cor3.2 admissible 60-digit cases: {counts['Cor3.2 60-digit']}")

# Audit the numerical constants without binary rounding.
val = 2 * mp.mpf('1.23') / (9 * mp.log(16))
say("Cor3.2 constant 2*1.23/(9 log16)=" + mp.nstr(val, 25))
say("Cor3.2 final coefficient (2/3)*(0.25-0.099)=" + mp.nstr(mp.mpf(2)/3 * (mp.mpf('.25')-mp.mpf('.099')), 25))
check("Cor3.2 decimal constants", val < mp.mpf('.099') and
      mp.mpf(2)/3 * (mp.mpf('.25')-mp.mpf('.099')) > mp.mpf('.1'))
say(f"Elapsed seconds: {time.monotonic() - started:.3f}")
say(f"Peak resident bytes (macOS): {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}; inherited nice: {os.getpriority(os.PRIO_PROCESS, 0)}")
Path("audit_exact.out").write_text("\n".join(lines) + "\n")
