"""If the spectrum of f lives in ONE parity class (all |S| odd, or all even), then
|S_{-i}| determines |S| mod 2 and hence S_i, so H(S_i|S_{-i}) = 0 for every i and B = 0.
The P03 erasure reduction then gives FEI with constant 2/ln 2 = 2.8854 for that whole class.
Odd (antisymmetric) functions, f(complement x) = -f(x), have exactly this property.
Test: do they all satisfy B = 0 and H/I <= 2.8854?"""
import numpy as np, sys
from erasure import spectrum, stats

TWO_OVER_LN2 = 2/np.log(2)

def odd_function(n, rng):
    """f(x_complement) = -f(x): choose freely on half the cube, mirror antisymmetrically"""
    N = 1 << n
    f = np.zeros(N, dtype=np.int8)
    half = rng.integers(0, 2, N//2).astype(np.int8)
    for x in range(N//2):
        f[x] = half[x]
        f[N-1-x] = 1 - half[x]          # complement input gets the opposite value
    return f

if __name__ == '__main__':
    print("odd (antisymmetric) Boolean functions:  B should be 0 and H/I <= 2/ln2 = %.4f" % TWO_OVER_LN2)
    rng = np.random.default_rng(1)
    worstB = 0.0; worstHI = 0.0; tested = 0; viol = 0
    for n in range(3, 15):
        for _ in range(25 if n < 12 else 6):
            f = odd_function(n, rng)
            if f.sum() in (0, 1 << n): continue
            mu = spectrum(f, n); I, H, B = stats(mu, n)
            if I <= 1e-12: continue
            worstB = max(worstB, abs(B)); worstHI = max(worstHI, H/I)
            tested += 1
            if H/I > TWO_OVER_LN2 + 1e-9: viol += 1
    print("  tested %d odd functions (n = 3..14)" % tested)
    print("  max |B|          = %.3e      (0 expected)" % worstB)
    print("  max H/I          = %.6f" % worstHI)
    print("  H/I above 2/ln2  : %d of %d" % (viol, tested))
    # NEGATIVE CONTROL: general functions must NOT have B = 0
    print("\nnegative control - general (non-odd) functions:")
    nz = 0; tot = 0; mx = 0.0
    for n in range(3, 12):
        for _ in range(25):
            f = rng.integers(0, 2, 1 << n).astype(np.int8)
            if f.sum() in (0, 1 << n): continue
            mu = spectrum(f, n); I, H, B = stats(mu, n)
            tot += 1; mx = max(mx, B)
            if B > 1e-9: nz += 1
    print("  %d of %d have B > 0 (max B = %.4f) -> the B = 0 finding is a property of the class,"
          % (nz, tot, mx))
    print("  not of the estimator")
    # and check the parity-support claim directly
    print("\ndirect check of the mechanism (is the spectrum on one parity class?):")
    for n in (5, 7, 9):
        f = odd_function(n, rng); mu = spectrum(f, n)
        idx = np.arange(1 << n); pc = np.array([bin(k).count('1') for k in idx])
        w_even = float(mu[pc % 2 == 0].sum()); w_odd = float(mu[pc % 2 == 1].sum())
        print("  n=%-3d weight on even |S| = %.3e   weight on odd |S| = %.6f" % (n, w_even, w_odd))
