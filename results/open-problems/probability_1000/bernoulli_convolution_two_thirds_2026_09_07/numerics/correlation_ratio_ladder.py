"""Does the correlation ratio stay bounded as factors are added? That is the whole remaining question.

ratio(n) = int_1^2 prod_(m<=n) f_m  /  prod_(m<=n) int_1^2 f_m,   f_m(x) = 1 + cos(2 pi x (3/2)^m / 3).
The denominator converges (proved: |mean - 1| <= 3/(pi (3/2)^m), summable), so ratio bounded is
equivalent to A_K bounded, which is equivalent to mu in L^2.

Measured so far for n = 0..7: 1.0000, 1.0000, 0.2652, 0.3297, 0.4752, 0.2683, 0.2394, 0.1623.
Extend it, with the grid sized so the fastest factor is resolved, and report the running min and max.
"""
import numpy as np, sys

NMAX = 26
per = (1.5 ** NMAX) / 3.0
N = 1 << 23
print(f"grid {N} points on [1,2]; fastest factor has {per:.0f} periods there, {N/per:.0f} points per period")
print(f"{'n':>4} {'joint':>12} {'prod of means':>15} {'ratio':>10} {'running min':>12} {'running max':>12}")
x = 1 + (np.arange(N) + 0.5) / N
run = np.ones(N); pm = 1.0
lo, hi = 1e9, 0.0
for n in range(NMAX + 1):
    fm = 1.0 + np.cos(2 * np.pi * x * (1.5 ** n) / 3.0)
    run *= fm
    pm *= float(fm.mean())
    joint = float(run.mean())
    r = joint / pm
    if n >= 2:
        lo = min(lo, r); hi = max(hi, r)
    print(f"{n:>4} {joint:>12.6f} {pm:>15.6f} {r:>10.4f} {lo:>12.4f} {hi:>12.4f}")
    sys.stdout.flush()
