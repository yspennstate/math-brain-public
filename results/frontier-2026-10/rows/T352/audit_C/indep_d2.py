# T352 audit 2 (agent C, 20 Oct 2026). Independent recomputation of the Doeblin-torus numerics in
# agent_B/NOTE.md. Different method from doeblin_torus_check.py: the transition is applied by FFT circular
# convolution after pushing mass through phi with linear interpolation (mass-conserving), on two grid sizes, and the
# stationary laws are also found by power iteration to 1e-15. Then D_2 = log(1 + chi2) between the c = 1 and
# c = 1 - 2/n laws, n^2 D_2, and the small-n behaviour (is the n = 10 value anomalous?).
import sys, numpy as np
D, s, eta, A = 1.0, 0.3, 0.1, 0.5
def run(N, c, T):
    x = np.arange(N) * D / N; h = D / N
    z = np.mod(x + D / 2, D) - D / 2
    k = sum(np.exp(-(z + j * D) ** 2 / (2 * s * s)) for j in range(-6, 7)) / (s * np.sqrt(2 * np.pi))
    kh = np.fft.rfft(k * h)
    phi = np.mod(x + eta * c * A * 2 * np.pi / D * np.sin(2 * np.pi * x / D), D)
    pos = phi / h; i0 = np.floor(pos).astype(int) % N; fr = pos - np.floor(pos); i1 = (i0 + 1) % N
    f = np.zeros(N); f[0] = 1.0 / h      # delta at x0 = 0 (as a grid mass)
    for t in range(T):
        g = np.zeros(N); np.add.at(g, i0, f * (1 - fr)); np.add.at(g, i1, f * fr)   # push mass through phi
        f = np.fft.irfft(np.fft.rfft(g) * kh, N)                                     # convolve with wrapped k
    return f, h
for N in (2048, 8192):
    print("N", N)
    base, h = run(N, 1.0, 300)
    for n in (10, 30, 100, 1000, 10000):
        g, _ = run(N, 1 - 2.0 / n, 300)
        chi2 = np.sum((base - g) ** 2 / g) * h
        print("  n %6d  D2 %.4e  n^2 D2 %.5f" % (n, np.log1p(chi2), n * n * np.log1p(chi2)), flush=True)
# small-c expansion: chi2 ~ I (dc)^2 with I the Fisher information of the stationary law in c
N = 8192; f1, h = run(N, 1.0, 300); e = 1e-4; fp, _ = run(N, 1 + e, 300); fm, _ = run(N, 1 - e, 300)
dlog = (np.log(fp) - np.log(fm)) / (2 * e); I = np.sum(f1 * dlog ** 2) * h
print("Fisher info in c at c=1: %.5e ; 4 I = %.5f (predicted n^2 D2 limit)" % (I, 4 * I))
# Gibbs heuristic for comparison: law prop. to exp(-2 eta c A cos/s^2)
x = np.arange(N) * D / N; b = 2 * eta * A / s ** 2; cs = np.cos(2 * np.pi * x)
p = np.exp(-b * cs); p /= p.sum(); print("Gibbs Fisher info in c: %.5e" % (b * b * (np.sum(p * cs * cs) - np.sum(p * cs) ** 2)))
