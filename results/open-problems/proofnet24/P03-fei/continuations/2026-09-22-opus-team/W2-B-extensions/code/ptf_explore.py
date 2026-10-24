"""Numerics for degree-2 polynomial threshold functions: H/I and the rank-localisation index

    Phi(f) = min over orderings r of Sigma_r(f) / I(f),   Sigma_r(f) = E_S sum_{i in S} ln+(r(i)/|S|),

computed exactly by the Hungarian method.  The rank method proves FEI on a class exactly when Phi
is bounded on the class (Lemma 6 plus H(|S|) <= 3I give H <= [3 + (1 + ln(a/(a-1)) + a Phi)/ln 2] I).

Usage: python ptf_explore.py families   (structured and random families, several n)
       python ptf_explore.py anneal N SEED ITERS OBJ   (OBJ = phi or hi; simulated annealing over
                                                         dense quadratic forms at n = N)
"""
import sys, time
import numpy as np
from fei_lib import *

setup_process()


def quad_values(X, A, b, th):
    """p(x) = sum_{j<k} A[j,k] x_j x_k + b.x - th, A strictly upper triangular."""
    return ((X @ A) * X).sum(1) + X @ b - th


def evaluate(f, n, with_order=False):
    c = wht(f)
    H, I = HI(c, n)
    if I < 1e-12:
        return None
    phi, order = phi_min(c, n)
    infl = influences(c, n)
    inf_order = list(np.argsort(-infl, kind="stable"))
    sig_inf = sigma_of_order(c, n, inf_order)
    out = dict(H=H, I=I, HI=H / I, phi=phi / I, phi_inf=sig_inf / I)
    if with_order:
        out["order"] = order
    return out


def families(logf):
    rng = np.random.default_rng(7)
    for n in (12, 14, 16, 18):
        X = coords(n)
        rows = []
        # dense Gaussian quadratics, several linear strengths and thresholds
        for beta in (0.0, 1.0, 3.0):
            for rep in range(3):
                A = np.triu(rng.standard_normal((n, n)), 1)
                b = beta * rng.standard_normal(n)
                sd = np.sqrt((A ** 2).sum() + (b ** 2).sum())
                th = rng.normal(0, 1.0) * sd
                rows.append(("dense b=%g" % beta, sgn(quad_values(X, A, b, th))))
        # dense with heavy-tailed (geometric) coefficient scales
        for rep in range(3):
            s = 1.5 ** (-rng.permutation(n * (n - 1) // 2))
            A = np.zeros((n, n))
            A[np.triu_indices(n, 1)] = s * rng.choice([-1, 1], size=s.size)
            b = 1.5 ** (-rng.permutation(n)) * rng.choice([-1, 1], size=n)
            th = rng.normal(0, 0.3)
            rows.append(("geomdense", sgn(quad_values(X, A, b, th))))
        # cycle / path with random or equal weights ("energy" functions)
        for kind in ("cycle", "path"):
            for wk in ("equal", "gauss", "geom"):
                A = np.zeros((n, n))
                m = n if kind == "cycle" else n - 1
                if wk == "equal":
                    w = np.ones(m)
                elif wk == "gauss":
                    w = rng.standard_normal(m)
                else:
                    w = 1.4 ** (-np.arange(m)) * rng.choice([-1, 1], size=m)
                for j in range(m):
                    a, bb = j, (j + 1) % n
                    A[min(a, bb), max(a, bb)] = w[j]
                th = 0.5 if wk == "equal" else rng.normal(0, 0.3) * np.sqrt((w ** 2).sum())
                rows.append(("%s-%s" % (kind, wk), sgn(quad_values(X, A, np.zeros(n), th))))
        # random 3-regular-ish graph (configuration pairing) with Gaussian weights
        for rep in range(2):
            A = np.zeros((n, n))
            for _ in range(3 * n // 2):
                a, bb = rng.choice(n, 2, replace=False)
                A[min(a, bb), max(a, bb)] = rng.standard_normal()
            th = rng.normal(0, 0.5) * np.sqrt((A ** 2).sum())
            rows.append(("sparse3", sgn(quad_values(X, A, np.zeros(n), th))))
        # low rank: product of two opposite-order linear forms, and discs
        g = 1.35 ** (-np.arange(n))
        L1f = X @ (g * rng.choice([-1, 1], size=n))
        L2f = X @ (g[::-1] * rng.choice([-1, 1], size=n))
        for th in (0.0, 0.05, 0.2, 0.5):
            rows.append(("prod-opp th=%g" % th, sgn(L1f * L2f - th)))
        for th in (0.3, 1.0, 2.0):
            rows.append(("disc-opp th=%g" % th, sgn(L1f ** 2 + L2f ** 2 - th)))
        ang = rng.uniform(0, 2 * np.pi, n)
        wts = 1.25 ** (-np.arange(n))
        U1 = X @ (wts * np.cos(ang))
        U2 = X @ (wts * np.sin(ang))
        s2 = (wts ** 2).sum()
        for th in (0.5, 1.0, 2.0):
            rows.append(("disc-rot th=%g" % th, sgn(U1 ** 2 + U2 ** 2 - th * s2)))
        # sum of squares of 3 random linear forms (rank 3 quadratic)
        V = rng.standard_normal((3, n))
        Q3 = ((X @ V.T) ** 2).sum(1)
        for th in (0.7, 1.0, 1.4):
            rows.append(("rank3 th=%g" % th, sgn(Q3 - th * (V ** 2).sum())))
        # block-separable controls (covered by Theorem B): LTF of pair-ANDs and of pair-XORs
        m = n // 2
        wp = 1.3 ** (-np.arange(m))
        AND2 = np.stack([np.where((X[:, 2 * j] > 0) & (X[:, 2 * j + 1] > 0), 1.0, -1.0) for j in range(m)], 1)
        XOR2 = np.stack([X[:, 2 * j] * X[:, 2 * j + 1] for j in range(m)], 1)
        rows.append(("LTF(AND2) blocks", sgn(AND2 @ wp - 0.2)))
        rows.append(("LTF(XOR2) blocks", sgn(XOR2 @ wp - 0.1)))
        rows.append(("MAJ(AND2) blocks", sgn(AND2.sum(1) + 0.5 - m / 2)))
        for name, f in rows:
            t0 = time.time()
            r = evaluate(f, n)
            if r is None:
                continue
            print("n=%2d %-20s H/I=%.4f  Phi=%.4f  Sigma(infl order)/I=%.4f  (%.1fs)"
                  % (n, name, r["HI"], r["phi"], r["phi_inf"], time.time() - t0), file=logf, flush=True)


def anneal(n, seed, iters, obj, logf):
    rng = np.random.default_rng(seed)
    X = coords(n)
    P = np.einsum("xi,xj->xij", X, X)[:, np.triu_indices(n, 1)[0], np.triu_indices(n, 1)[1]]  # (2^n, m) pair products
    m = P.shape[1]

    def score(a, b, th):
        f = sgn(P @ a + X @ b - th)
        r = evaluate(f, n)
        if r is None or r["I"] < 0.05:
            return -1.0, r
        return (r["phi"] if obj == "phi" else r["HI"]), r

    a = rng.standard_normal(m) * (1.4 ** (-rng.permutation(m)))
    b = rng.standard_normal(n) * 0.5
    th = 0.0
    cur, rcur = score(a, b, th)
    best, rbest, bestp = cur, rcur, (a.copy(), b.copy(), th)
    T0 = 0.05 if obj == "phi" else 0.1
    for it in range(iters):
        T = T0 * (1 - it / iters) + 1e-4
        a2, b2, th2 = a.copy(), b.copy(), th
        mv = rng.integers(0, 4)
        if mv == 0:
            j = rng.integers(0, m); a2[j] = rng.standard_normal() * np.abs(a).max() * rng.uniform(0.01, 1.5)
        elif mv == 1:
            j = rng.integers(0, n); b2[j] = rng.standard_normal() * (np.abs(a).max() + np.abs(b).max()) * rng.uniform(0.01, 1.5)
        elif mv == 2:
            th2 = th + rng.normal(0, 0.3) * (np.abs(a).sum() + np.abs(b).sum()) / np.sqrt(m)
        else:
            j = rng.integers(0, m); a2[j] = 0.0
        s2, r2 = score(a2, b2, th2)
        if s2 >= cur or rng.random() < np.exp((s2 - cur) / T):
            a, b, th, cur, rcur = a2, b2, th2, s2, r2
            if cur > best:
                best, rbest, bestp = cur, rcur, (a.copy(), b.copy(), th)
        if it % 200 == 0:
            print("it=%d cur=%.4f best=%.4f (best H/I=%.4f Phi=%.4f)" % (it, cur, best, rbest["HI"], rbest["phi"]),
                  file=logf, flush=True)
    np.savez("../logs/anneal_%s_n%d_s%d.npz" % (obj, n, seed), a=bestp[0], b=bestp[1], th=bestp[2])
    print("FINAL obj=%s n=%d seed=%d best=%.5f  H/I=%.5f Phi=%.5f Sigma(infl)/I=%.5f I=%.4f"
          % (obj, n, seed, best, rbest["HI"], rbest["phi"], rbest["phi_inf"], rbest["I"]), file=logf, flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "families":
        with open("../logs/ptf_families.log", "w") as logf:
            families(logf)
    elif sys.argv[1] == "anneal":
        n, seed, iters, obj = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        with open("../logs/ptf_anneal_%s_n%d_s%d.log" % (obj, n, seed), "w") as logf:
            anneal(n, seed, iters, obj, logf)
