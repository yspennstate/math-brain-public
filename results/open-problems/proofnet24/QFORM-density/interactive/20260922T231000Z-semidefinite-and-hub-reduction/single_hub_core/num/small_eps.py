"""Does the density of Q = 2 X_h L + lambda V^2 + 2 eps L P grow as eps -> 0?

Window estimator, exact in the hub: given X', Q is affine in X_h with slope 2L, so
P(|Q - y| <= delta | X') = |F_h(x_2) - F_h(x_1)|, x_{1,2} = (y - R -+ delta)/(2L), R = lambda V^2 + 2 eps L P,
F_h the distribution function of the hub law. Printed: max over a grid of y of P(|Q - y| <= delta)/(2 delta), with
delta fixed at 0.002 for every eps (so that the resolution does not move with eps), for hub laws that are uniform on [0, 1] or a random union of intervals of length eps covering half of
[0, 2] (rough at the scale of the cross term), and light laws uniform on [-1/2, 1/2] or centred combs of 8 teeth of
width 1/8 at the integers.
"""
import sys
import numpy as np

try:
    import psutil
    psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass

rng = np.random.default_rng(7)


def hub_cdf(kind, eps):
    if kind == "unif":
        xs = np.array([0.0, 1.0]); Fs = np.array([0.0, 1.0])
        return xs, Fs
    n = int(round(2.0 / eps))
    keep = rng.random(n) < 0.5
    edges = np.arange(n + 1) * eps
    xs = [edges[0]]; Fs = [0.0]; F = 0.0
    for j in range(n):
        F += eps if keep[j] else 0.0
        xs.append(edges[j + 1]); Fs.append(F)
    Fs = np.array(Fs) / F
    return np.array(xs), Fs


def light(kind, size):
    if kind == "unif":
        return rng.random(size) - 0.5
    t = rng.integers(0, 8, size)
    return (t + rng.random(size) / 8.0) - (3.5 + 1 / 16.0)


def frames(kind, m):
    if kind == "walsh":
        W = np.array([1, 1, 1, 1]) / 2.0; V = np.array([1, -1, 1, -1]) / 2.0; P = np.array([1, 1, -1, -1]) / 2.0
        return W, V, P
    Q, _ = np.linalg.qr(rng.standard_normal((m, 3)))
    return Q[:, 0], Q[:, 1], Q[:, 2]


def peak(eps, hubkind, lawkind, framekind, m, lam=1.0, nsamp=3_000_000, B=200_000):
    xs, Fs = hub_cdf(hubkind, eps)
    w, v, p = frames(framekind, m)
    delta = 0.002
    ys = np.concatenate([np.linspace(-1.5, 1.5, 121), np.linspace(-0.1, 0.1, 101)])
    acc = np.zeros_like(ys)
    done = 0
    while done < nsamp:
        X = light(lawkind, (B, len(w)))
        L, V, P = X @ w, X @ v, X @ p
        R = lam * V * V + 2 * eps * L * P
        s = 2 * L
        s = np.where(np.abs(s) < 1e-12, 1e-12, s)
        for j, y in enumerate(ys):
            x1 = (y - R - delta) / s; x2 = (y - R + delta) / s
            acc[j] += np.abs(np.interp(x2, xs, Fs) - np.interp(x1, xs, Fs)).sum()
        done += B
    dens = acc / done / (2 * delta)
    j = int(np.argmax(dens))
    return dens[j], ys[j]


if __name__ == "__main__":
    framekind = sys.argv[1] if len(sys.argv) > 1 else "walsh"
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    for lawkind in ("comb", "unif"):
        for hubkind in ("rough", "unif"):
            out = []
            for eps in (0.3, 0.1, 0.03, 0.01, 0.003):
                d, y = peak(eps, hubkind, lawkind, framekind, m)
                out.append(f"eps={eps}: {d:.3f} (y={y:+.2f})")
            print(f"{framekind} m={m} light={lawkind} hub={hubkind}:  " + "  ".join(out), flush=True)
    print("done", flush=True)
