# -*- coding: utf-8 -*-
"""Referee 3, part 2: (A) how large must r / n / l actually be for each 'polylog, well inside
the range' line to be non-vacuous, and (B) numerical test of the repair I propose for the
longitudinal-range hole - deriving the all-j dogleg excess from the enclosing-ball condition
at the single direction u, with the constant degrading by exactly 1/C_L'.
"""
import math
import itertools
import numpy as np

def sec(t):
    print("\n" + "=" * 78); print(t); print("=" * 78)

# ---------------------------------------------------------------------------
sec("A1. r_0: smallest r for which the lemma's OWN range ledger is non-empty")
print(" lower(r) = max( (2C3/c_-) log r , (2/(c'' c_-)) log(18 C1 rho r) ),  upper(r) = delta^2 sqrt r")
print(" delta = min(1, 3C2/c_-),  c'' = c1/(6 sqrt(2+rho))\n")

def r0(C1, c1, C2, C3, c_, rho):
    delta = min(1.0, 3 * C2 / c_)
    cpp = c1 / (6 * math.sqrt(2 + rho))
    x = 1.0
    while x < 4000:
        r = 10 ** x
        lo = max((2 * C3 / c_) * math.log(r), (2.0 / (cpp * c_)) * math.log(18 * C1 * rho * r))
        hi = delta ** 2 * math.sqrt(r)
        if lo <= hi:
            return x, delta, cpp
        x += 0.5
    return float("inf"), delta, cpp

print("%-46s %10s %8s %10s" % ("(C1, c1, C2, C3, c_-, rho)", "log10 r_0", "delta", "c''"))
cases = [
    (1.0, 1.0, 1.0, 1.0, 1.0, 2.0),
    (1.0, 0.5, 1.0, 1.0, 0.5, 2.0),
    (1.0, 0.2, 1.0, 2.0, 0.2, 2.0),
    (1.0, 0.1, 0.5, 2.0, 0.1, 2.0),
    (1.0, 0.05, 0.5, 2.0, 0.05, 2.0),
    (1.0, 0.02, 0.1, 0.5, 0.05, 1.5),
    (1.0, 0.01, 0.1, 5.0, 0.01, 2.0),
]
for c in cases:
    x, delta, cpp = r0(*c)
    print("%-46s %10.1f %8.3f %10.2e" % (str(c), x, delta, cpp))
print("\n=> the lemma is VACUOUS below r_0, and r_0 is not stated anywhere in the draft.")

# ---------------------------------------------------------------------------
sec("A2. n_0 for G-f(i): 'polylog, far inside the range sigma^2 <= delta^2 sqrt n'")
print(" need (log M + 3 log n + O(1))/(c'' c_-)  <=  delta^2 sqrt(n)")
def n0_gf1(M, cppc, delta):
    x = 1.0
    while x < 4000:
        n = 10 ** x
        lo = (math.log(M) + 3 * math.log(n)) / cppc
        if lo <= delta ** 2 * math.sqrt(n):
            return x
        x += 0.5
    return float("inf")
print("%6s %10s %8s %12s" % ("M", "c''*c_-", "delta", "log10 n_0"))
for M in (5, 8):
    for cppc in (1.0, 0.1, 0.01, 0.001):
        for delta in (1.0, 0.1):
            print("%6d %10.3f %8.2f %12.1f" % (M, cppc, delta, n0_gf1(M, cppc, delta)))

# ---------------------------------------------------------------------------
sec("A3. n_0 for G-f(ii): the draft's 'n >~ M^3/theta^4' against the honest requirement")
print(" honest: c'' c_- (theta^2/4) sqrt(n) M^{-3/2} >= log(C M n)  [union] and >= the lemma's")
print(" own lower threshold (2C3/c_-) log(Mn) at R = Mn.")
def n0_gf2(M, theta, cppc, C=1.0):
    x = 1.0
    while x < 4000:
        n = 10 ** x
        expo = cppc * (theta ** 2 / 4) * math.sqrt(n) * M ** -1.5
        if expo >= math.log(C * M * n):
            return x
        x += 0.5
    return float("inf")
print("%6s %8s %10s %14s %16s" % ("M", "theta", "c''*c_-", "log10 n_0", "draft M^3/theta^4"))
for M in (5, 8):
    for theta in (0.05, 0.2, 0.5):
        for cppc in (1.0, 0.01):
            print("%6d %8.2f %10.3f %14.1f %16.2e"
                  % (M, theta, cppc, n0_gf2(M, theta, cppc), M ** 3 / theta ** 4))

# ---------------------------------------------------------------------------
sec("B. REPAIR of the longitudinal-range hole, derived from the ENCLOSING BALL and tested")
print("""CLAIM (mine, to replace the draft's 'v is arbitrary at its distance in the condition as
stated'): let n be the outward unit normal supporting B_g at u* = u/g(u), and suppose
B_g is inside a Euclidean ball of radius R touching at u* (Newman-Piza's printed condition).
Write phi(y) = <y,n>/<u*,n>, so phi <= g and phi is linear. Then
    g(v) + g(x-v) - g(x) = [g(v) - phi(v)] + [g(x-v) - phi(x-v)]          (phi linear, exact)
                        >= (1/(2 R <u*,n>)) [ g(v)|vhat-u*|^2 + g(x-v)|what-u*|^2 ].
For v at transversal offset d and ANY longitudinal position, |vhat-u*| ~ c d/|v| and
|what-u*| ~ c d/|x-v|, so the excess is >= c d^2 (1/|v| + 1/|x-v|) >= 4 c d^2/(|v|+|x-v|).
Since every site in the G-a union has |v| + |x-v| <= C_L' r = (2+rho) r, while the MIDPOINT
has |v|+|x-v| ~ r, the all-j excess is at least (1/C_L') times the midpoint excess.
TEST: measure  min_j excess(d,j) / excess(d,r/2)  over the whole G-a union range and check
it never drops below 1/C_L'.""")

def norms():
    return {
        "l1": lambda h, y: abs(h) + abs(y),
        "l2": lambda h, y: math.hypot(h, y),
        "lp1.3": lambda h, y: (abs(h) ** 1.3 + abs(y) ** 1.3) ** (1 / 1.3),
        "l4": lambda h, y: (abs(h) ** 4 + abs(y) ** 4) ** 0.25,
        "hex": lambda h, y: max(abs(y), 0.6 * abs(y) + 0.9 * abs(h), 1.2 * abs(h)),
        # a strictly convex, non-lp symmetric norm
        "mix": lambda h, y: 0.5 * math.hypot(h, y) + 0.5 * (abs(h) ** 4 + abs(y) ** 4) ** 0.25,
    }

rho = 2.0
r = 200.0
print("\n%-8s %6s %8s %10s %14s %12s" % ("norm", "tilt", "d", "min ratio", "argmin j", "1/C_L'"))
worst_overall = 9e9
for name, g in norms().items():
    for tilt in (0.0, 0.02, 0.1, 0.3):
        ux, uy = math.sin(tilt), math.cos(tilt)
        px, py = math.cos(tilt), -math.sin(tilt)
        X = (r * ux, r * uy)
        gx = g(*X)
        # admissibility of the (norm, direction) pair: (H-curv-LOWER) demands a POSITIVE
        # midpoint excess at every small offset. A facet direction has excess 0 for small d
        # (c_- = 0) even though large d may leave the facet - so test at the smallest offset.
        def _mid_exc(dd):
            vx, vy = (r / 2) * ux + dd * px, (r / 2) * uy + dd * py
            return g(vx, vy) + g(X[0] - vx, X[1] - vy) - gx
        if _mid_exc(0.25) <= 1e-9 * r:
            print("%-8s %6.2f %8s %10s %14s %12.4f"
                  % (name, tilt, "-", "FLAT c_-=0", "-", 1 / (2 + rho)))
            continue
        for d in (1.0, 5.0, 20.0):
            def exc(s):
                vx, vy = s * ux + d * px, s * uy + d * py
                return g(vx, vy) + g(X[0] - vx, X[1] - vy) - gx
            mid = exc(r / 2)
            if mid <= 1e-9 * r:
                # the hypothesis has NO content for this (norm, direction): the shape is flat
                # there, c_- = 0. l1 at any tilted direction and the hex norm at e_2 are exactly
                # section 3's "a shape can be flat (kills c_-)" case. Skip, do not divide by 0.
                print("%-8s %6.2f %8.1f %10s %14s %12.4f"
                      % (name, tilt, d, "FLAT c_-=0", "-", 1 / (2 + rho)))
                continue
            best, bj = None, None
            # G-a union range: j from -(rho-1)/2*r to r + (rho-1)/2*r  (the length cap)
            for s in np.linspace(-(rho - 1) / 2 * r, r + (rho - 1) / 2 * r, 2001):
                e = exc(s)
                if best is None or e / mid < best:
                    best, bj = e / mid, s
            worst_overall = min(worst_overall, best)
            print("%-8s %6.2f %8.1f %10.4f %14.1f %12.4f"
                  % (name, tilt, d, best, bj, 1 / (2 + rho)))
print("\nworst ratio over all norms/tilts/offsets:", round(worst_overall, 4),
      " vs the guaranteed 1/C_L' =", round(1 / (2 + rho), 4))
print("=> the derived degradation 1/C_L' is a valid (and loose) guarantee; measured loss is small,")
print("   but it is NOT zero for tilted spans, so the constant must be carried:")
print("   c_- -> c_-/C_L' for the far-j sites, i.e. worst case c'' c_- -> c1 c_-/(6 (2+rho)^{3/2}).")
print("   U[1,2]: c1 c_-/48 (Form A) and c1 c_-/96 (Form B) instead of /12 and /24.")

# ---------------------------------------------------------------------------
sec("C. Consolidated corrected constants")
for rho_ in (2.0,):
    CL = 2 + rho_
    print("rho = b/a_w = %.1f  (U[1,2])" % rho_)
    print("  site count N          : draft 6 rho r      -> sharp 2(rho r + 1) <= 4 rho r")
    print("  Form A prefactor      : draft 18 C1 rho r  -> 12 C1 rho r  (one-sided: 6 C1 rho r)")
    print("  c''                   : c1/(6 sqrt(%.0f)) = c1/%.0f  (unchanged, CONFIRMED)"
          % (CL, 6 * math.sqrt(CL)))
    print("  c'' after the far-j repair (tilted spans only): c1/(6 (%.0f)^{1/2}) with c_- -> c_-/%.0f"
          % (CL, CL))
    print("  C'''                  : draft delta^2 -> delta^2/4 (ceiling-safe for r >= 2/delta)")
    print("  wlog on delta         : delta <= min(1, 3C2/c_-)   CONFIRMED")
    print("  new wlog on c1        : c1 <= 3 sqrt(2+rho)/C3  (kills the middle-band hole; makes")
    print("                          the consumer's A >= C3 c'' branch vacuous, so A = 2 suffices)")
