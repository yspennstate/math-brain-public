"""How large can B/I get?  Exhaustive over all functions of <= 4 variables, sampled at 5,
plus structured families.  B = sum_i H(S_i|S_{-i}) (erasure entropy of the spectral sample).
If sup B/I = K then the P03 erasure reduction gives FEI with K + 2/ln2 = K + 2.8854."""
import numpy as np, itertools, sys, random
from erasure import spectrum, stats, tribes

def exhaustive(n):
    N = 1 << n
    best = (0.0, None); vals = []
    for t in range(1 << N):
        f = np.array([(t >> k) & 1 for k in range(N)], dtype=np.int8)
        s = f.sum()
        if s == 0 or s == N: continue
        mu = spectrum(f, n)
        I, H, B = stats(mu, n)
        if I <= 1e-12: continue
        vals.append(B/I)
        if B/I > best[0]: best = (B/I, t, I, H, B)
    return best, len(vals), vals

def sample(n, k, seed=0):
    rng = np.random.default_rng(seed)
    best = (0.0, None)
    for _ in range(k):
        f = rng.integers(0, 2, 1 << n).astype(np.int8)
        if f.sum() in (0, 1 << n): continue
        mu = spectrum(f, n); I, H, B = stats(mu, n)
        if I <= 1e-12: continue
        if B/I > best[0]: best = (B/I, None, I, H, B)
    return best

def one_point(n):
    """f = 1 exactly at one input (the family the record says maximises the step)"""
    f = np.zeros(1 << n, dtype=np.int8); f[0] = 1
    return f

def majority(n):
    idx = np.arange(1 << n)
    pc = np.array([bin(k).count('1') for k in idx])
    return (pc > n//2).astype(np.int8)

if __name__ == '__main__':
    print("=== exhaustive over all non-constant functions of n variables ===")
    for n in (2, 3, 4):
        (b, t, I, H, B), cnt, vals = exhaustive(n)
        print("n=%d  functions=%-7d  max B/I = %.6f   (that f: I=%.4f H=%.4f B=%.4f, H/I=%.4f)"
              % (n, cnt, b, I, H, B, H/I))
        sys.stdout.flush()
    print("\n=== random sample at n = 5..14 ===")
    for n in range(5, 15):
        b, _, I, H, B = sample(n, 300 if n < 12 else 60, seed=n)
        print("n=%-3d random: max B/I = %.4f  (I=%.3f H=%.3f)" % (n, b, I, H))
        sys.stdout.flush()
    print("\n=== structured families ===")
    for n in range(2, 20):
        f = one_point(n); mu = spectrum(f, n); I, H, B = stats(mu, n)
        print("one-point  n=%-3d I=%8.4f H=%8.4f H/I=%6.3f B=%8.4f B/I=%6.3f" % (n, I, H, H/I, B, B/I))
    for n in (3, 5, 7, 9, 11, 13, 15):
        f = majority(n); mu = spectrum(f, n); I, H, B = stats(mu, n)
        print("majority   n=%-3d I=%8.4f H=%8.4f H/I=%6.3f B=%8.4f B/I=%6.3f" % (n, I, H, H/I, B, B/I))
