"""G0013, lane claude-q2-attack-0912, 2026-09-12.  Two checks.

(1) T(identity)/n^4 against the continuum value 1/10 proved in the memo (exactly 1/10 for the
    diagonal coupling of two uniforms), for n up to 24.

(2) Band plans.  A plan is a "band plan in direction theta" if the n^2 grid cells are sorted by
    <z,theta> and cut into n consecutive blocks of n, and the blocks are handed to the atoms by some
    permutation rho.  The memo proves that in the two lattice directions (1,1) and (1,-1) no band
    plan ever exceeds M(identity), whatever sigma is; here we ask numerically whether SOME direction
    does, for the runner-up permutations that the exhaustive search says beat nothing but do have
    M(sigma) > M(identity).  If no direction reaches M(sigma), the certifying plan for sigma is
    genuinely two dimensional and no one-dimensional exchange argument can produce it.
"""
import sys, time
import numpy as np
from scipy.optimize import linear_sum_assignment


def cells_of(n):
    idx = np.arange(n)
    I, J = np.meshgrid(idx, idx, indexing="ij")
    return np.stack([I.ravel(), J.ravel()], 1)


def M_true(sigma, cells, n):
    atoms = np.stack([np.arange(n), np.asarray(sigma, dtype=np.int64)], 1)
    P = np.repeat(cells @ atoms.T, n, axis=1)
    r, c = linear_sum_assignment(-P)
    return int(P[r, c].sum())


def T_true(sigma, cells, n):
    atoms = np.stack([np.arange(n), np.asarray(sigma, dtype=np.int64)], 1)
    D = np.repeat(((cells[:, None, :] - atoms[None, :, :]) ** 2).sum(-1), n, axis=1)
    r, c = linear_sum_assignment(D)
    return int(D[r, c].sum())


def band_value(sigma, cells, n, theta):
    key = cells @ np.asarray(theta, dtype=float)
    order = np.argsort(key, kind="stable")
    blocks = order.reshape(n, n)
    I = cells[blocks, 0].sum(1).astype(float)
    J = cells[blocks, 1].sum(1).astype(float)
    ks = np.arange(n, dtype=float); sk = np.asarray(sigma, dtype=float)
    W = I[:, None] * ks[None, :] + J[:, None] * sk[None, :]      # block r -> atom k
    r, c = linear_sum_assignment(-W)
    return W[r, c].sum()


def main():
    print("(1) identity value against the continuum 1/10", flush=True)
    for n in list(range(3, 13)) + [16, 20, 24]:
        cells = cells_of(n)
        ident = tuple(range(n))
        T = T_true(ident, cells, n)
        print(f"    n={n:3d}  T(id)={T:8d}  W2^2={T/n**4:.8f}  (1/10 - W2^2 = {0.1 - T/n**4:+.8f})", flush=True)

    print("(2) best band plan over directions, versus the true M", flush=True)
    rng = np.random.default_rng(11)
    for n in (5, 6, 7, 8):
        cells = cells_of(n)
        ident = tuple(range(n))
        Mid = M_true(ident, cells, n)
        # the runner-up family the search reports: identity with the last two values swapped
        sig = list(range(n)); sig[-1], sig[-2] = sig[-2], sig[-1]; sig = tuple(sig)
        Ms = M_true(sig, cells, n)
        thetas = [(1.0, 1.0), (1.0, -1.0), (1.0, 0.0), (0.0, 1.0)]
        thetas += [tuple(v) for v in rng.normal(size=(400, 2))]
        best = max(band_value(sig, cells, n, th) for th in thetas)
        bestid = max(band_value(ident, cells, n, th) for th in thetas)
        print(f"    n={n}: sigma={sig}  M(id)={Mid}  M(sigma)={Ms}  best band plan for sigma={best:.2f}"
              f"  (band plan for id={bestid:.2f})", flush=True)
        print(f"         band plan reaches M(sigma): {best > Ms - 1e-9};  exceeds M(id): {best > Mid + 1e-9}", flush=True)


if __name__ == "__main__":
    try:
        import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    main()
