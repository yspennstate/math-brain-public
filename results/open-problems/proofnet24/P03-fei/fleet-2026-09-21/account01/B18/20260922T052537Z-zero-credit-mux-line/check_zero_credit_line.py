#!/usr/bin/env python3
"""Source-bound checker for B18 zero-selector-credit MUX line.

Loads the pinned h96 candidate itself and verifies the robust inequalities used
in REPORT.md.  This does NOT rerun value iteration or the settled read-once
certificate.  It only reads the already-committed candidate array.
"""
from pathlib import Path
import hashlib, math, numpy as np

C0 = 6.4548
C = 6.521851214
a = 0.268204856
alpha = 4.9096
B = C/2.0 + 2.0
WLO = 2.229
WHI = 8.629
EXPECTED_BLOB = "1e2a1a5c293fa7b6ec9885b7a410910d6589be80"

# Locate repository root without any machine-specific path.
here = Path(__file__).resolve()
root = next(p for p in here.parents if (p / "proofnet24").is_dir())
npz = root / "proofnet24/P03-fei/continuations/2026-09-21-readonce-certificate/data/cert_vi_h96k40.npz"
raw = npz.read_bytes()
git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
assert git_blob == EXPECTED_BLOB, (git_blob, EXPECTED_BLOB)

d = np.load(npz)
xs = np.asarray(d["xs"], float)
G = np.asarray(d["G"], float)
Csrc = float(d["C"])
assert abs(Csrc-C0) < 1e-14
assert len(xs) == len(G) == 4321

# Global wobble envelope.  G-alpha*x is piecewise linear, so node extrema are
# global extrema on the interpolated source candidate; the tail has slope alpha.
w = G - alpha*xs
assert float(w.min()) > WLO
assert float(w.max()) < WHI

# Live potential on the small side.
def gamma(z):
    if z <= 0.0: return 0.0
    if z > 0.5: z = 1.0-z
    x = math.log2(1.0/z)
    j = int(np.searchsorted(xs, x, side="right")-1)
    j = max(0, min(j, len(xs)-2))
    if x <= xs[-1]:
        gv = G[j] + (x-xs[j])*(G[j+1]-G[j])/(xs[j+1]-xs[j])
    else:
        # Source tail slope is alpha for this certificate.
        gv = G[-1] + alpha*(x-xs[-1])
    return z*gv + a*z*(1.0-z)

# Endpoint used by the proof.
quarter = gamma(0.25)
assert abs(quarter - 4.5050884105) < 5e-13
endpoint_slack = C - 2.0 - quarter
assert endpoint_slack > 0.0167

# Lower source tail envelope and its derivative.
def tail_lower(z):
    if z == 0.0: return 0.0
    return z*(alpha*math.log2(1.0/z)+WLO) + a*z*(1.0-z)
def tail_lower_prime(z):
    return alpha*(math.log2(1.0/z)-1.0/math.log(2.0)) + WLO + a*(1.0-2.0*z)

# Local region 0<s<=1/50.  u=1/4+s/2 traverses only finitely many source
# interpolation segments.  On each segment, bound Gamma'(u) from above by the
# larger endpoint G value minus the exact segment slope/ln2 plus the largest
# quadratic-lift derivative.  tail_lower' decreases in s.
min_local_derivative = float("inf")
min_local_j = None
for j in range(len(xs)-1):
    # Convert source node x back to its p coordinate; source xs are increasing.
    p_hi = 2.0**(-xs[j])
    p_lo = 2.0**(-xs[j+1])
    # Intersection with u in [1/4, 0.26].
    lo = max(p_lo, 0.25)
    hi = min(p_hi, 0.26)
    if not (lo < hi):
        continue
    sL = 2.0*(lo-0.25)
    sR = 2.0*(hi-0.25)
    m = (G[j+1]-G[j])/(xs[j+1]-xs[j])
    gmax = max(G[j], G[j+1])
    gammap_upper = gmax - m/math.log(2.0) + a*(1.0-2.0*lo)
    tprime_lower = tail_lower_prime(sR)
    deriv_lower = 0.5*(tprime_lower-gammap_upper)
    if deriv_lower < min_local_derivative:
        min_local_derivative = deriv_lower
        min_local_j = j
assert min_local_derivative > 2.8, (min_local_derivative, min_local_j)

# Hence the local defect is increasing from its positive s=0 endpoint.
# Global tail sandwich section: s in [1/50,1/10].
def upper_source(z):
    return z*(alpha*math.log2(1.0/z)+WHI) + a*z*(1.0-z)
def L1(s):
    u = 0.25+0.5*s
    return C-2.0 + 0.5*tail_lower(s) - upper_source(u)
L1_002 = L1(0.02)
# u/s >= 3 and 1/2-s >= 0.4 on [0.02,0.1].
L1_derivative_floor = 0.5*(alpha*math.log2(3.0) - (WHI-WLO) + 0.4*a)
assert L1_002 > 0.047
assert L1_derivative_floor > 0.74

# Complementary-data MUX theorem supplies Gamma(s)>=4s(1-s)B.  Use it on
# [0.1,0.5].  The resulting lower envelope L2 is strictly concave, so its
# minimum is at an endpoint.
def L2(s):
    u = 0.25+0.5*s
    return C-2.0 + 2.0*B*s*(1.0-s) - upper_source(u)
L2_01, L2_05 = L2(0.1), L2(0.5)
# ln 2 > 0.69 and u>=0.3 give a completely coarse negative upper bound.
L2_second_upper = -4.0*B + alpha/(4.0*0.3*0.69) + a/2.0
assert L2_second_upper < -14.9
assert L2_01 > 0.26
assert L2_05 > 0.31

print("PASS")
print("candidate_blob", git_blob)
print("wobble_min", format(float(w.min()), ".15g"))
print("wobble_max", format(float(w.max()), ".15g"))
print("quarter", format(quarter, ".15g"))
print("endpoint_slack", format(endpoint_slack, ".15g"))
print("min_local_derivative_lower", format(min_local_derivative, ".15g"), "segment", min_local_j)
print("L1_at_1_over_50", format(L1_002, ".15g"))
print("L1_derivative_floor", format(L1_derivative_floor, ".15g"))
print("L2_at_1_over_10", format(L2_01, ".15g"))
print("L2_at_1_over_2", format(L2_05, ".15g"))
print("L2_second_derivative_upper", format(L2_second_upper, ".15g"))
