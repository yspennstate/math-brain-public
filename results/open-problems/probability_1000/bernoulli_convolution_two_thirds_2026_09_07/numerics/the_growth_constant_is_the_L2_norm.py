"""The window constant IS the L2 norm - so the operator route is circular. And the integrand is CHEAP.

c_M = int_0^M prod_(j>=0) cos^2(pi (2/3)^j u) du = int_0^M nuhat(u/2)^2 du.
Its fastest factor is j = 0, period 1 in u - unlike the lacunary Fourier sum this integrand has NO fine
scale, so c_M can be pushed to M = 10^5 cheaply and the tail of int |nuhat|^2 read directly. If 6 c_M
tracks the independently computed ||f||^2 = 1 + 2S = 1.206310, the identity holds and the transfer-operator
route returns the very quantity it was meant to bound.
"""
import numpy as np

PTS = 400          # points per unit u
CH  = 2_000_000    # chunk size
def c_upto(M, prev=(0.0, 0.0)):
    """integrate on [prev_M, M], return running total"""
    lo, tot = prev
    n = int((M - lo) * PTS)
    du = (M - lo) / n
    acc = 0.0
    for s in range(0, n, CH):
        k = min(CH, n - s)
        u = lo + (s + np.arange(k) + 0.5) * du
        p = np.ones(k)
        jj = 0
        while True:
            a = (2.0/3.0) ** jj * u
            p *= np.cos(np.pi * a) ** 2
            jj += 1
            if a.max() < 1e-9:
                break
        acc += p.sum() * du
    return (M, tot + acc)

TARGET = 1.206310   # ||f||^2 = 1 + 2S, from the independent Fourier-side computation
print(f"{'M':>9} {'c_M':>12} {'6 c_M':>12} {'vs ||f||^2':>12} {'tail added':>12} {'tail/decade':>12}")
st = (0.0, 0.0); prevtot = 0.0
for M in (10, 100, 1_000, 10_000, 100_000):
    st = c_upto(float(M), st)
    added = st[1] - prevtot
    print(f"{M:>9} {st[1]:>12.6f} {6*st[1]:>12.6f} {6*st[1]-TARGET:>+12.6f} {added:>12.6f} {6*added:>12.6f}")
    prevtot = st[1]
print()
print("If 6 c_M -> 1.206310 and the per-decade tail collapses, the identity holds AND the integral")
print("converges as far as any finite M can say - which is exactly the open question, restated.")
