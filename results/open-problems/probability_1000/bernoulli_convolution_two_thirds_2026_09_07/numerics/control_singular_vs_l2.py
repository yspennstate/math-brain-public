"""Control: does the weight-profile method discriminate, or would it 'close the lane' for anything?

My closure rests on the profile Cum(u) being LINEAR in u with slope (2/3)||f||^2 -- the signature of a
linear correlation integral, i.e. of an L^2 density.  If the same computation produced a linear profile
for a measure that is provably SINGULAR, the method would be vacuous and the closure worthless.

Control measure: the middle-thirds Cantor measure, Y_C = sum_k B_k 2 3^-(k+1), B fair iid bits.
It is singular with correlation dimension D_2 = log2/log3 = 0.6309, so P(|Y_C - Y'_C| <= r) ~ r^0.6309,
NOT linear.  Same code path, same estimator, on both measures.

If the estimator returns slope 1 for the 2/3 measure and 0.63 for the Cantor measure, it discriminates
and the closure means what I said.  If it returns 1 for both, the closure is an artifact.
"""
import numpy as np

def diff_law(weights, steps, depth):
    """Exact law of Y - Y' on a lattice, by integer shift-add. steps are integer scaled increments."""
    half = int(sum(abs(s) for s in steps))
    size = 2 * half + 1
    p = np.zeros(size); p[half] = 1.0
    for s in steps:
        s = int(s)
        q = weights[1] * p
        q[s:] += weights[2] * p[:size - s]
        q[:size - s] += weights[0] * p[s:]
        p = q
    return p, half

def slope_report(name, p, half, scale, radii):
    v = np.arange(-half, half + 1)
    a = np.abs(v)
    o = np.argsort(a, kind="stable")
    aS, pS = a[o], p[o]
    cum = np.cumsum(pS)
    print(f"  {name}")
    print(f"    {'r':>10} {'P(|D|<=r)':>13} {'P/r':>10} {'log P/log r':>13}")
    prev = None
    for r in radii:
        j = np.searchsorted(aS, r * scale, side="right")
        val = cum[j - 1] if j > 0 else 0.0
        if val > 0:
            print(f"    {r:>10.5f} {val:>13.6f} {val/r:>10.4f} {np.log(val)/np.log(r):>13.4f}")

# 1. the 2/3 Bernoulli convolution: Y = (1/3) sum B_k (2/3)^k, eta = B - B' at (1/4,1/2,1/4)
K = 13
steps23 = [(2 ** i) * (3 ** (K - i)) for i in range(K + 1)]   # D * 3^(K+1)
p23, h23 = diff_law([0.25, 0.5, 0.25], steps23, K)
print("Bernoulli convolution at 2/3 (target: slope 1, i.e. P(|D|<=r)/r constant near 0.804/3*... )")
slope_report("lambda = 2/3", p23, h23, 3.0 ** (K + 1), [0.05, 0.02, 0.01, 0.005, 0.002])

# 2. the middle-thirds Cantor measure: Y = sum B_k 2*3^-(k+1); D*3^(N) integer with steps 2*3^(N-1-k)
N = 15
stepsC = [2 * (3 ** (N - 1 - k)) for k in range(N)]
pC, hC = diff_law([0.25, 0.5, 0.25], stepsC, N - 1)
print()
print("Middle-thirds Cantor measure (target: exponent log2/log3 = 0.6309, NOT 1)")
slope_report("Cantor", pC, hC, 3.0 ** N, [0.05, 0.02, 0.01, 0.005, 0.002])
