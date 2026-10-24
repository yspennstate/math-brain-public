"""Independent reproduction of |c(n)| on a high block, at two grid spacings.

c(n) = (1/B_n) int over [(3/2)^n, (3/2)^(n+1)) of exp(3 pi i v) Q(v)^2 dv,  B_n = int Q^2 over the block.
The criterion needs |c(n)| <= 1/3 - delta. Reported values near n = 30 were about 0.08-0.12.
Q^2 is band-limited to 3 and cos(3 pi v) Q^2 to 4.5, so the shortest period in the integrand is 2/9;
a BLOCK integral is not covered by the band-limit exactness argument, so the honest check is refinement.
Two spacings, h = 1/16 and h = 1/48, on the same block. If they agree the number is real.
"""
import numpy as np

def block(n, h, CH=2_000_000):
    lo, hi = 1.5 ** n, 1.5 ** (n + 1)
    npts = int((hi - lo) / h)
    du = (hi - lo) / npts
    B = 0.0; Cr = 0.0; Ci = 0.0
    for s in range(0, npts, CH):
        k = min(CH, npts - s)
        v = lo + (s + np.arange(k) + 0.5) * du
        q = np.ones(k); j = 0
        while True:
            a = (2.0/3.0) ** j * v
            q *= np.cos(np.pi * a); j += 1
            if a.max() < 1e-9: break
        q2 = q * q
        ph = 3.0 * np.pi * v
        B += q2.sum() * du
        Cr += (np.cos(ph) * q2).sum() * du
        Ci += (np.sin(ph) * q2).sum() * du
    return B, Cr, Ci, j

print(f"{'n':>3} {'h':>8} {'B_n':>13} {'Re c':>10} {'Im c':>10} {'|c|':>9} {'factors':>8}")
for n in (28, 30, 32):
    out = []
    for h in (1/16, 1/48):
        B, Cr, Ci, j = block(n, h)
        c = complex(Cr / B, Ci / B)
        out.append((h, B, c))
        print(f"{n:>3} {h:>8.5f} {B:>13.5e} {c.real:>10.5f} {c.imag:>10.5f} {abs(c):>9.5f} {j:>8}")
    (h1, B1, c1), (h2, B2, c2) = out
    print(f"    refinement: |c| {abs(c1):.5f} -> {abs(c2):.5f}  (change {abs(c2)-abs(c1):+.5f}), "
          f"B relative change {(B2-B1)/B1:+.2e}")
print("\ncriterion needs |c| <= 1/3 - delta = 0.3333 - delta; reported mean near n=30 was about 0.08-0.12")
