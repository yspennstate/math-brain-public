"""How many spectral lines sit near the criterion's frequency? Exact, by meet-in-the-middle.

The criterion's coefficient c(n) is the Fourier coefficient of a ratio-3/2 Riesz product at frequency
(3/2)^(n+1). That frequency is provably NOT attained (mod-3 induction), so |c(n)| is window leakage. The
leakage from a line at frequency distance d is significant while d <~ 2, since the window [1, 3/2) has
width 1/2. In integers, with S_eps = sum eps_i 3^i 2^(n+1-i), the frequency distance is
|3^(n+1) - S_eps| / 2^(n+1), so the quantity that controls the leakage is

    N(n, D) = # { eps in {0,+-1}^(n+1) : |3^(n+1) - S_eps| <= D * 2^(n+1) }.

Exact count by splitting the index set in half and merging sorted arrays. Also report the minimum
distance actually attained (the mod-3 lemma says the integer gap is >= 1, i.e. distance >= 2^-(n+1);
what matters is whether that floor is approached).
"""
import numpy as np

def counts(n, Ds):
    idx = list(range(n + 1))
    w = [3**i * 2**(n + 1 - i) for i in idx]
    h = (n + 1) // 2
    def sums(ws):
        a = np.zeros(1, dtype=object)
        for x in ws:
            a = np.concatenate([a - x, a, a + x])
        return a
    A = sums(w[:h]); B = sums(w[h:])
    tgt = 3**(n + 1)
    Bs = np.sort(B)
    out = []
    for D in Ds:
        R = D * 2**(n + 1)
        tot = 0
        for a in A:
            lo = np.searchsorted(Bs, tgt - a - R, side='left')
            hi = np.searchsorted(Bs, tgt - a + R, side='right')
            tot += hi - lo
        out.append(tot)
    # minimum attained distance
    best = None
    for a in A:
        k = np.searchsorted(Bs, tgt - a)
        for kk in (k - 1, k, k + 1):
            if 0 <= kk < len(Bs):
                d = abs(tgt - a - int(Bs[kk]))
                if best is None or d < best: best = d
    return out, best

Ds = [0.5, 1.0, 2.0, 4.0]
print(f"{'n':>3} {'3^(n+1)':>12} {'N(D=.5)':>9} {'N(1)':>8} {'N(2)':>8} {'N(4)':>8} "
      f"{'min gap':>12} {'min dist':>11}")
for n in range(4, 17):
    c, best = counts(n, Ds)
    print(f"{n:>3} {3**(n+1):>12} {c[0]:>9} {c[1]:>8} {c[2]:>8} {c[3]:>8} {best:>12} "
          f"{best/2**(n+1):>11.3e}")
print("\nIf N(2) stays bounded the leakage is a finite sum of window tails; if it grows like 2^n the")
print("naive bound reproduces the linearising overshoot and the criterion needs cancellation, not counting.")
