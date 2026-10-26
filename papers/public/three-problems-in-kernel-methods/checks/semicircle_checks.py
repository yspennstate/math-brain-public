#!/usr/bin/env python3
"""Small-dimension companions to the semicircle section of the paper, run on a laptop.

Everything here is cheap enough to reproduce in minutes.  Each block prints the numbers the paper
quotes, with the design counts used.

  1. Kolmogorov--Smirnov distance between the spectrum of sqrt(d) A and the semicircle law, for the
     Veronese normal and for the Gaussian-row control, at d = 20, 40, 60.
  2. The sphere construction (inputs uniform on the sphere, rows xx^T - I/d in the traceless block):
     the excess of d^{k-1} Tr(A^{2k}) over the Catalan number, against the excess of the Gaussian-row
     Veronese normal at the same d.
  3. The kurtosis of <z, U> along a typical direction U, for the Gaussian row (3 + 24/d) and the
     sphere row, and along the null direction of a design.
  4. Rows with independent coordinates of kurtosis kappa (three-point law) against Gaussian rows,
     and the dependence dial r (sum of r independent rank-one forms), at d = 14.
  5. The finite-r approach of the operator norm of an r x r random matrix to its 2 sqrt(r) asymptote.

Usage: python semicircle_checks.py [--quick]
"""
import argparse, math, time, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--quick", action="store_true")
ap.add_argument("--seed", type=int, default=20260916)
a = ap.parse_args()
rng = np.random.default_rng(a.seed)
Q = a.quick
CAT = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}


def sym_basis_vec(M):
    """vec of a symmetric matrix in an orthonormal Frobenius basis: diag, then sqrt2 * upper."""
    d = M.shape[0]
    iu = np.triu_indices(d, 1)
    return np.concatenate([np.diag(M), math.sqrt(2.0) * M[iu]])


def unvec(v, d):
    M = np.zeros((d, d))
    iu = np.triu_indices(d, 1)
    M[np.diag_indices(d)] = v[:d]
    M[iu] = v[d:] / math.sqrt(2.0)
    M = M + M.T - np.diag(np.diag(M))
    return M


def veronese_rows(d, m, rng):
    X = rng.standard_normal((m, d))
    # z(x) = vec((xx^T - I)/sqrt2) in the orthonormal basis: diag (x_a^2-1)/sqrt2, off-diag x_a x_b
    Z = np.empty((m, d * (d + 1) // 2))
    Z[:, :d] = (X ** 2 - 1.0) / math.sqrt(2.0)
    iu = np.triu_indices(d, 1)
    Z[:, d:] = X[:, iu[0]] * X[:, iu[1]]
    return Z


def null_normal(Z):
    """unit normal to the rows of Z (m x p, m = p-1), as a symmetric d x d matrix of unit Frobenius norm."""
    _, _, Vt = np.linalg.svd(Z, full_matrices=True)
    v = Vt[-1]
    p = Z.shape[1]
    d = int((math.isqrt(8 * p + 1) - 1) // 2)
    A = unvec(v, d)
    return A / np.linalg.norm(A, "fro")


def moments(A):
    ev = np.linalg.eigvalsh(A)
    d = A.shape[0]
    return {k: d ** (k - 1) * float((ev ** (2 * k)).sum()) for k in (2, 3, 4, 5)}, ev


def ks_semicircle(ev):
    """KS distance between the empirical law of sqrt(d) lambda and the semicircle on [-2, 2]."""
    d = len(ev)
    x = np.sort(np.sqrt(d) * ev)
    x = np.clip(x, -2.0, 2.0)
    F = 0.5 + (x * np.sqrt(4 - x ** 2) + 4 * np.arcsin(x / 2)) / (4 * math.pi)
    i = np.arange(1, d + 1)
    return float(max(np.max(i / d - F), np.max(F - (i - 1) / d)))


def sphere_rows_traceless(d, m, rng):
    """inputs uniform on S^{d-1}; rows xx^T - I/d, expressed in an orthonormal basis of Sym_d^0."""
    X = rng.standard_normal((m, d))
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    p = d * (d + 1) // 2
    Z = np.empty((m, p))
    Z[:, :d] = X ** 2 - 1.0 / d
    iu = np.triu_indices(d, 1)
    Z[:, d:] = math.sqrt(2.0) * X[:, iu[0]] * X[:, iu[1]]
    # project onto Sym_d^0: remove the component along vec(I)/sqrt(d) (only the diagonal block carries it)
    e0 = np.zeros(p); e0[:d] = 1.0 / math.sqrt(d)
    Z -= np.outer(Z @ e0, e0)
    # orthonormal basis of the complement of e0: Householder that maps e0 to the first coordinate, drop it
    w = e0.copy(); w[0] -= 1.0; w /= np.linalg.norm(w)
    Zt = Z - 2.0 * np.outer(Z @ w, w)          # Z H, H = I - 2 w w^T ; first column is now the e0 component (zero)
    return Zt[:, 1:], w                          # m x (p-1)


def sphere_normal(d, rng):
    m = d * (d + 1) // 2 - 1                     # dim Sym_d^0
    Zt, w = sphere_rows_traceless(d, m - 1, rng)
    _, _, Vt = np.linalg.svd(Zt, full_matrices=True)
    v = np.concatenate([[0.0], Vt[-1]])
    v = v - 2.0 * w * (w @ v)                    # back to the original coordinates
    A = unvec(v, d)
    return A / np.linalg.norm(A, "fro")


def mse(v):
    v = np.asarray(v); return v.mean(), (v.std(ddof=1) / math.sqrt(len(v)) if len(v) > 1 else 0.0)


t0 = time.time()
print("== 1. KS distance of sqrt(d) A to the semicircle law: Veronese normal and Gaussian-row control")
for d, reps in ((20, 40 if Q else 200), (40, 20 if Q else 100), (60, 6 if Q else 40)):
    p = d * (d + 1) // 2
    ksv, ksg, edgev, edgeg = [], [], [], []
    for _ in range(reps):
        A = null_normal(veronese_rows(d, p - 1, rng)); _, ev = moments(A); ksv.append(ks_semicircle(ev)); edgev.append(math.sqrt(d) * np.abs(ev).max())
        G = rng.standard_normal((p - 1, p)); B = null_normal(G); _, ev = moments(B); ksg.append(ks_semicircle(ev)); edgeg.append(math.sqrt(d) * np.abs(ev).max())
    (mv, sv), (mg, sg) = mse(ksv), mse(ksg)
    print(f"  d={d} designs={reps}: KS Veronese {mv:.4f}+-{sv:.4f} (edge {np.mean(edgev):.3f})  Gaussian rows {mg:.4f}+-{sg:.4f} (edge {np.mean(edgeg):.3f})  ratio {mv/mg:.2f}   [{time.time()-t0:.0f}s]", flush=True)

print("== 2. The sphere construction against the Gaussian-row Veronese normal, excess over Catalan")
for d, reps in ((16, 60 if Q else 300), (24, 40 if Q else 200), (32, 20 if Q else 120), (40, 10 if Q else 80)):
    p = d * (d + 1) // 2
    exv = {k: [] for k in CAT}; exs = {k: [] for k in CAT}
    for _ in range(reps):
        mv, _ = moments(null_normal(veronese_rows(d, p - 1, rng)))
        ms, _ = moments(sphere_normal(d, rng))
        for k in CAT:
            exv[k].append(mv[k] - CAT[k]); exs[k].append(ms[k] - CAT[k])
    line = f"  d={d} designs={reps}:"
    for k in CAT:
        (a1, s1), (a2, s2) = mse(exv[k]), mse(exs[k])
        line += f"  k={k}: Veronese +{a1:.3f}+-{s1:.3f} sphere +{a2:.3f}+-{s2:.3f} ratio {a2/a1:.2f}"
    print(line + f"   [{time.time()-t0:.0f}s]", flush=True)

print("== 3. Kurtosis of <z,U> along a typical direction, Gaussian row (3+24/d) and sphere row; and along the null direction")
N = 200000 if Q else 1000000
for d in (6, 10, 20, 30):
    p = d * (d + 1) // 2
    U = unvec(rng.standard_normal(p), d); U /= np.linalg.norm(U, "fro")
    X = rng.standard_normal((N, d))
    zg = ((X @ U) * X).sum(axis=1) - np.trace(U)          # <xx^T - I, U>
    zg /= math.sqrt(2.0)
    kg = np.mean(zg ** 4) / np.mean(zg ** 2) ** 2
    Xs = X / np.linalg.norm(X, axis=1, keepdims=True)
    zs = ((Xs @ U) * Xs).sum(axis=1) - np.trace(U) / d     # <xx^T - I/d, U>
    ks_ = np.mean(zs ** 4) / np.mean(zs ** 2) ** 2
    tr4 = float((np.linalg.eigvalsh(U) ** 4).sum())
    print(f"  d={d}: Gaussian row kurtosis {kg:.3f} (3+12 Tr U^4 = {3+12*tr4:.3f}; 3+24/d = {3+24/d:.3f})  sphere row {ks_:.3f}", flush=True)
d = 20; p = d * (d + 1) // 2
A = null_normal(veronese_rows(d, p - 1, rng)); X = rng.standard_normal((N, d))
z = (((X @ A) * X).sum(axis=1) - np.trace(A)) / math.sqrt(2.0)
U = unvec(rng.standard_normal(p), d); U /= np.linalg.norm(U, "fro")
z2 = (((X @ U) * X).sum(axis=1) - np.trace(U)) / math.sqrt(2.0)
print(f"  d=20: kurtosis along the null direction of one design {np.mean(z**4)/np.mean(z**2)**2:.3f}; along an independent random direction {np.mean(z2**4)/np.mean(z2**2)**2:.3f}")

print("== 4. Independent coordinates: three-point law of kurtosis kappa against Gaussian rows, d=14; and the dependence dial r")
d = 14; p = d * (d + 1) // 2; m = p - 1
reps = 3000 if Q else 30000
def excess_rows(rowfn, reps):
    ex = {k: [] for k in CAT}
    for _ in range(reps):
        mv, _ = moments(null_normal(rowfn()))
        for k in CAT: ex[k].append(mv[k] - CAT[k])
    return {k: mse(ex[k]) for k in CAT}
def threepoint(kappa):
    q = 1.0 / kappa
    def f():
        u = rng.random((m, p)); s = rng.choice([-1.0, 1.0], size=(m, p))
        return np.where(u < q, s / math.sqrt(q), 0.0)
    return f
res_g = excess_rows(lambda: rng.standard_normal((m, p)), reps)
print("  Gaussian rows:      " + "  ".join(f"k={k}: +{res_g[k][0]:.4f}+-{res_g[k][1]:.4f}" for k in CAT), flush=True)
for kappa in (1.0, 3.0, 5.0, 9.0):
    r_ = excess_rows(threepoint(kappa), reps)
    nz = p / kappa
    print(f"  three-point kappa={kappa:g} (nonzeros/row {nz:.0f}): " + "  ".join(f"k={k}: +{r_[k][0]:.4f}+-{r_[k][1]:.4f} ({(r_[k][0]-res_g[k][0])/math.hypot(r_[k][1],res_g[k][1]):+.1f} se from Gaussian)" for k in CAT), flush=True)
def rankr(r):
    def f():
        Xr = rng.standard_normal((m, d, r))
        M = np.einsum('mik,mjk->mij', Xr, Xr) - r * np.eye(d)[None]
        M /= math.sqrt(2.0 * r)
        Z = np.empty((m, p)); iu = np.triu_indices(d, 1)
        Z[:, :d] = M[:, np.arange(d), np.arange(d)]; Z[:, d:] = math.sqrt(2.0) * M[:, iu[0], iu[1]]
        return Z
    return f
for r in (1, 2, 4, 8):
    r_ = excess_rows(rankr(r), reps // 3)
    print(f"  rank-{r} rows (XX^T - rI)/sqrt(2r): " + "  ".join(f"k={k}: +{r_[k][0]:.4f}+-{r_[k][1]:.4f}" for k in CAT), flush=True)

print("== 5. Operator norm of an r x r random matrix relative to 2 sqrt(r)")
for r in (4, 16, 64, 256):
    reps = 300 if Q else 2000
    out = []
    for shape in ("real symmetric", "complex symmetric", "complex Ginibre"):
        vals = []
        for _ in range(reps):
            if shape == "real symmetric":
                G = rng.standard_normal((r, r)); G = (G + G.T) / math.sqrt(2.0)
            elif shape == "complex symmetric":
                G = (rng.standard_normal((r, r)) + 1j * rng.standard_normal((r, r))) / math.sqrt(2.0); G = (G + G.T) / math.sqrt(2.0)
            else:
                G = (rng.standard_normal((r, r)) + 1j * rng.standard_normal((r, r))) / math.sqrt(2.0)
            vals.append(np.linalg.norm(G, 2) / (2 * math.sqrt(r)))
        out.append(f"{shape} {np.mean(vals):.3f}")
    print(f"  r={r}: " + "; ".join(out), flush=True)
print(f"done in {time.time()-t0:.0f}s")
