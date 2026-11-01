"""The Riesz product averages 1 globally. The octave [1,2] is a trough where it averages 0.05.

P_K(x) = prod_(m=0..K) (1 + cos(2 pi x (3/2)^m / 3)).
Every factor has mean 1, and the frequencies sum_m eps_m (3/2)^m / 3 with eps in {0,+-1} never vanish
for eps != 0 - multiply by 2^K and the relation sum eps_m 3^m 2^(K-m) = 0 is the dissociateness lemma.
So the constant term of P_K is exactly 1, and its average over a long interval tends to 1.

But the quantity the problem asks about is int_1^2 P_K, measured around 0.05. So the octave is a region
where the product is atypically SMALL - a trough, not a typical stretch. Measure that contrast, and see
how the interval average depends on WHERE the unit interval sits.
"""
import numpy as np

def P(x, K):
    out = np.ones_like(x)
    for m in range(K + 1):
        out *= 1.0 + np.cos(2 * np.pi * x * (1.5 ** m) / 3.0)
    return out

print("mean of P_K over [a, a+1] for several a, and over a long stretch")
print(f"{'K':>4} " + " ".join(f"{'[' + str(a) + ',' + str(a+1) + ']':>12}" for a in (0,1,2,3,5,10)) + f"{'long run':>12}")
for K in (6, 10, 14, 18):
    row = []
    for a in (0, 1, 2, 3, 5, 10):
        n = 1 << 22
        x = a + (np.arange(n) + 0.5) / n
        row.append(float(P(x, K).mean()))
    n = 1 << 23
    xl = 0.0 + (np.arange(n) + 0.5) * (3.0 ** (K + 1)) / n   # a full period of the slowest factor scale
    longrun = float(P(xl, K).mean())
    print(f"{K:>4} " + " ".join(f"{v:>12.6f}" for v in row) + f"{longrun:>12.6f}")

print()
print("The constant term is exactly 1 by dissociateness, so the long-run mean must be 1;")
print("the octave [1,2] sits far below it. That is where the whole difficulty lives.")
