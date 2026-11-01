# Twisted frame integrals J(a, kappa) = int |E exp(i(aL + tV + kappa L P))| dt for comb laws on a spread 3D frame.
# Frame: the 8 x 3 matrix of all sign vectors / sqrt 8 (leverages 3/8), optionally rotated inside its span.
# X_i = K_i + W_i/N, K_i uniform on {0..N-1}; the cell part is replaced by its Gaussian limit N(0, I_3/(12 N^2))
# in (L, V, P) (isotropic because the frame is orthonormal; its mean vanishes because the sign rows sum to zero).
import sys, math, time
import numpy as np

S = np.array([[a, b, c] for a in (1, -1) for b in (1, -1) for c in (1, -1)])

def triple_law(N):
    R = 8 * (N - 1)
    size = 2 * R + 1
    arr = np.zeros((size, size, size)); arr[R, R, R] = 1.0
    for s in S:
        new = np.zeros_like(arr)
        for k in range(N):
            new += np.roll(arr, shift=tuple(int(x) for x in s * k), axis=(0, 1, 2))
        arr = new / N
    idx = np.nonzero(arr > 1e-14)
    z = np.stack(idx, axis=1).astype(float) - R
    return z, arr[idx]

def rot(axis, ang):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + math.sin(ang) * K + (1 - math.cos(ang)) * K @ K

class Frame:
    def __init__(self, N, R):
        z, p = triple_law(N)
        y = z @ R / math.sqrt(8.0)          # rows (L, V, P)
        self.L, self.V, self.P, self.p = y[:, 0], y[:, 1], y[:, 2], p
        self.N = N
        self.sigma = 1.0 / (math.sqrt(12.0) * N)
        s = self.sigma
        self.h = s / 35.0
        rngV = self.V.max() - self.V.min()
        dt = 1.0 / (4.0 * rngV)
        M = int(2 * math.pi / (dt * self.h))
        self.M = 1 << int(math.ceil(math.log2(M)))
        self.j = np.rint((self.V - self.V.min()) / self.h).astype(np.int64)
        self.t = 2 * math.pi * np.fft.fftfreq(self.M, d=self.h)
        self.gt = np.exp(-s * s * self.t ** 2 / 2)
        self.dt = 2 * math.pi / (self.M * self.h)

    def J(self, a, kappa):
        s2 = self.sigma ** 2
        L, P = self.L, self.P
        al = a + kappa * P; ga = kappa * L
        den = 1.0 + kappa * kappa * s2 * s2
        w = self.p * np.exp(1j * (a * L + kappa * L * P)) / math.sqrt(den) * \
            np.exp(-(s2 * (al * al + ga * ga) + 2j * kappa * s2 * s2 * al * ga) / (2 * den))
        C = np.bincount(self.j, weights=w.real, minlength=self.M) + 1j * np.bincount(self.j, weights=w.imag, minlength=self.M)
        F = np.fft.ifft(C) * self.M * self.gt
        return float(np.abs(F).sum() * self.dt)

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    which = sys.argv[2] if len(sys.argv) > 2 else "irr"
    R = np.eye(3) if which == "rat" else rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
    t0 = time.time(); fr = Frame(N, R)
    print("N=%d frame=%s points=%d M=%d (%.1fs)" % (N, which, len(fr.p), fr.M, time.time() - t0), flush=True)
    amax = 7.0 / fr.sigma
    agrid = np.linspace(0, amax, 61)
    kappas = [0.0, 0.05, 0.1, 0.2, 0.4, 0.7, 1.0, 1.5, 2.0]
    res = np.array([[fr.J(a, k) for k in kappas] for a in agrid])
    print("kappa:        " + " ".join("%6.2f" % k for k in kappas))
    print("sup_a J:      " + " ".join("%6.3f" % x for x in res.max(axis=0)))
    print("mean_a J:     " + " ".join("%6.3f" % x for x in res.mean(axis=0)))
    ratio = res / np.maximum(res[:, :1], 1e-12)
    print("max ratio:    " + " ".join("%6.3f" % x for x in ratio.max(axis=0)))
    print("4 pi = %.3f; elapsed %.0fs" % (4 * math.pi, time.time() - t0))
