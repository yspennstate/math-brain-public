"""The classical companion: for mu supported in an interval of length D, is mu * N(0,t) unimodal for
every t >= D^2/4, and is that sharp?

The argument: at a local minimum of the density with a local maximum on each side, translated to 0,
    G = int d phi_t(d) drho = 0    and    H = int (d^2-t) phi_t(d) drho >= 0,
rho being the reflected measure, supported in an interval of length D containing 0 in its hull.  The
measures on that interval with G = 0 form a convex compact set whose extreme points carry at most two
atoms; a single atom must sit at 0 and has H = -t phi_t(0) < 0; and for a pair at -a and b the
stationarity condition fixes the weights and gives

    H >= 0  <=>  t <= ab,

with a + b <= D so ab <= D^2/4.  Hence no separating local minimum exists once t > D^2/4.

This checks it by building the density directly and counting modes.
"""
import numpy as np

def density(atoms, weights, t, xs):
    atoms = np.asarray(atoms, float); w = np.asarray(weights, float); w = w / w.sum()
    d = xs[:, None] - atoms[None, :]
    return (w[None, :] * np.exp(-d * d / (2 * t)) / np.sqrt(2 * np.pi * t)).sum(axis=1)

def modes(atoms, weights, t, pad=12.0, n=400001):
    lo, hi = min(atoms) - pad * np.sqrt(t), max(atoms) + pad * np.sqrt(t)
    xs = np.linspace(lo, hi, n)
    f = density(atoms, weights, t, xs)
    up = np.diff(f) > 0
    # count sign changes from rising to falling
    return int(np.sum(up[:-1] & ~up[1:]))

def threshold(atoms, weights, lo=1e-4, hi=10.0):
    """least t from which the density is unimodal, by bisection"""
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if modes(atoms, weights, mid) <= 1: hi = mid
        else: lo = mid
    return hi

CASES = [
    ("two equal atoms at +-1/2",       [-0.5, 0.5],            [1, 1]),
    ("two atoms 0.3/0.7 at +-1/2",     [-0.5, 0.5],            [0.3, 0.7]),
    ("two atoms 0.1/0.9 at +-1/2",     [-0.5, 0.5],            [0.1, 0.9]),
    ("three atoms -1/2, 0, 1/2",       [-0.5, 0.0, 0.5],       [0.45, 0.10, 0.45]),
    ("three atoms -1/2, 0.1, 1/2",     [-0.5, 0.1, 0.5],       [0.4, 0.2, 0.4]),
    ("four atoms spread over [-1/2,1/2]", [-0.5, -0.2, 0.2, 0.5], [0.3, 0.2, 0.2, 0.3]),
    ("uniform-ish on [-1/2,1/2]",      list(np.linspace(-0.5, 0.5, 9)), [1] * 9),
    ("atoms at -1/2 and 1/2 plus a spike", [-0.5, -0.45, 0.5], [0.3, 0.4, 0.3]),
]

print("every measure below has support of diameter 1, so the claim is: unimodal for t >= 1/4 = 0.25")
print(f"{'measure':>38} {'threshold t*':>13} {'<= 0.25?':>9}")
worst = 0.0
for name, a, w in CASES:
    t = threshold(a, w)
    worst = max(worst, t)
    print(f"{name:>38} {t:>13.6f} {'yes' if t <= 0.2500 + 1e-6 else 'NO':>9}")
print(f"\nlargest threshold over these: {worst:.6f}; the claim is that D^2/4 = 0.25 is an upper bound")
print("and that the two equal atoms attain it exactly")
