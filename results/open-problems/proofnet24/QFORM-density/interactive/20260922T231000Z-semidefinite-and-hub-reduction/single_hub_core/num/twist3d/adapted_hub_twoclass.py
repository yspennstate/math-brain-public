# The hub that sees P on the two-class frame of Example 5.2, where the maximal functional M_2 of (L, V) grows like N:
# w, v = the rotation by atan(sqrt 2) of (e1 + e2)/sqrt 2, (e3 + e4)/sqrt 2, and q^ = cos(phi) (e1 - e2)/sqrt 2 +
# sin(phi) (e3 - e4)/sqrt 2 with tan(phi) = sqrt 3. Combs of N teeth of width 1/N at the integers; beta = -E L, s = 0.
# Same estimator as adapted_hub.py: Phi keeps in each P-column its top unit set of x-bins; B0 uses one set for all P.
import sys, math, time
import numpy as np

def frame():
    th, ph = math.atan(math.sqrt(2)), math.atan(math.sqrt(3))
    e12 = np.array([1, 1, 0, 0]) / math.sqrt(2); e34 = np.array([0, 0, 1, 1]) / math.sqrt(2)
    d12 = np.array([1, -1, 0, 0]) / math.sqrt(2); d34 = np.array([0, 0, 1, -1]) / math.sqrt(2)
    w = math.cos(th) * e12 + math.sin(th) * e34
    v = -math.sin(th) * e12 + math.cos(th) * e34
    q = math.cos(ph) * d12 + math.sin(ph) * d34
    return np.stack([w, v, q], axis=1)

def run(N, s=0.0, n=40_000_000, chunk=2_000_000, b0=0.01, bp0=0.05, seed=5):
    # b0 is the x-bin width and also the unit of the top set (1/b0 bins); pass b0=0.05 for coarser, less noisy sets
    E = frame(); w, q = E[:, 0], E[:, 2]
    beta = -(N / 2.0) * w.sum()
    xmax = 3.0 * N
    pmin = N * q[q < 0].sum() - 0.1; pmax = N * q[q > 0].sum() + 0.1
    nx = int(round(2 * xmax / b0)); npb = int(math.ceil((pmax - pmin) / bp0))
    H = np.zeros((nx, npb)); H0 = np.zeros((nx, npb)); rng = np.random.default_rng(seed); half = None
    rg = ((-xmax, xmax), (pmin, pmin + npb * bp0))
    for c in range(n // chunk):
        X = rng.integers(0, N, size=(chunk, 4)) + rng.random((chunk, 4)) / N
        Y = X @ E; T = Y[:, 0] + beta; V = Y[:, 1]; P = Y[:, 2]
        xs = (s - V * V) / (2 * T); wt = 1.0 / (2 * np.abs(T))
        H += np.histogram2d(xs, P, bins=(nx, npb), range=rg, weights=wt)[0]
        # control: P shuffled across samples, so the hub that sees P can gain only through the estimator's noise
        H0 += np.histogram2d(xs, rng.permutation(P), bins=(nx, npb), range=rg, weights=wt)[0]
        if c == n // chunk // 2 - 1:
            half = H.copy()
    rows = []
    for tag, HH, nn in (("full", H, n), ("half", half, n // 2), ("shuffled P", H0, n)):
        top = int(round(1.0 / b0))
        B0 = np.sort(HH.sum(axis=1))[::-1][:top].sum() / nn
        ph = []
        for kp in (1, 4, 20):
            m = (npb // kp) * kp
            Hp = HH[:, :m].reshape(nx, -1, kp).sum(axis=2)
            ph.append((kp * bp0, np.sort(Hp, axis=0)[::-1][:top].sum() / nn))
        rows.append((tag, B0, ph))
    return rows

if __name__ == "__main__":
    b0 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01
    n = int(float(sys.argv[3])) if len(sys.argv) > 3 else 40_000_000
    for N in [int(x) for x in sys.argv[1].split(",")]:
        t0 = time.time()
        for tag, B0, ph in run(N, b0=b0, n=n):
            print("two-class frame N=%d %s bin %.2f  eps=0 bathtub %.4f  adapted Phi %s" % (N, tag, b0, B0, "  ".join("dP=%.2f: %.4f" % x for x in ph)), flush=True)
        print("   (%.0fs)" % (time.time() - t0), flush=True)
