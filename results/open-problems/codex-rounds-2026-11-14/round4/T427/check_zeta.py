#!/usr/bin/env python3
"""Independent zeta check of the earlier square heat finite part.

Writes no files. Run with OMP_NUM_THREADS=1, nice -n 15, python3 -B.
"""
import os
import sys
import resource

assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
if priority < 15:
    raise SystemExit("REFUSED: actual niceness must be at least 15")
resource.setrlimit(resource.RLIMIT_CPU, (90, 95))

import mpmath as mp

mp.mp.dps = 75


def beta(s):
    return (mp.zeta(s, mp.mpf(1) / 4) - mp.zeta(s, mp.mpf(3) / 4)) / 4**s


# This calculation uses a Laurent expansion of the Dirichlet series,
# not the theta integrals of the earlier script.
derivative = mp.diff(beta, mp.mpf(1), method="quad", radius=mp.mpf("0.2"))
assert abs(mp.im(derivative)) < mp.mpf("1e-65")
derivative = mp.re(derivative)
h = mp.mpf(1) / 6 + derivative / mp.pi**2 - mp.log(mp.pi) / (2 * mp.pi)

# Independent way to compute beta'(1): the functional equation and the
# Hurwitz-zeta derivative at zero. It uses only Gamma(1/4), Gamma(3/4).
bprime0 = mp.log(mp.gamma(mp.mpf(1)/4) / mp.gamma(mp.mpf(3)/4)) - mp.log(2)
bprime1 = mp.pi/4 * (mp.euler + mp.log(mp.pi/2) - 2*bprime0)
h_gamma = mp.mpf(1)/6 + bprime1/mp.pi**2 - mp.log(mp.pi)/(2*mp.pi)
assert abs(h - h_gamma) < mp.mpf("1e-65")
earlier = mp.mpf("0.00402223657274227817227364756500595607753013990163588814077047")
assert abs(h-earlier) < mp.mpf("1e-51")
earlier_tail = 4*mp.exp(-36*mp.pi)/(36*mp.pi**2*(1-mp.exp(-mp.pi))*(1-mp.exp(-13*mp.pi)))
assert 0 < h-earlier < earlier_tail

print(f"niceness={priority}; precision={mp.mp.dps} decimal digits")
print("beta'(1) via contour derivative =", mp.nstr(derivative, 60))
print("h_Q via zeta finite part =", mp.nstr(h, 60))
print("h_Q via Gamma identity =", mp.nstr(h_gamma, 60))
print("difference from earlier H_5 =", mp.nstr(h-earlier, 12))
print("earlier H_5 analytic tail bound =", mp.nstr(earlier_tail, 12))
print("PASS: independent zeta and Gamma checks agree with round 3.")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss = rss if sys.platform == "darwin" else rss*1024
assert rss < 1_000_000_000
print(f"Peak resident memory: {rss} bytes")
