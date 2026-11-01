"""Upper bound on the FEI constant for read-once AND/OR/NOT formulas by a slack function.

Claim. Let Gamma: (0,1) -> [0, inf) be symmetric, Gamma(p) = Gamma(1-p), and suppose for all p, q in (0,1)

    (A)  Gamma(pq) <= q (Gamma(p) + h(V_p)) + p (Gamma(q) + h(V_q)) - Ht_AND(p, q),

where V_p = 4p(1-p), h is the binary entropy (bits) and Ht_AND(p, q) is the biased spectral entropy of AND on
independent inputs of measures p and q. Then every read-once formula f over AND, OR, NOT satisfies

    H(f) <= C I(f) - Gamma(Pr[f])  with  C = Gamma(1/2),   hence  H(f) <= Gamma(1/2) I(f).

Proof sketch (induction over the formula): a variable has H = 0, I = 1, Pr = 1/2. For g = AND(a, b) with
independent inputs, the composition lemma gives H(g) = q V_p H+_a + p V_q H+_b + Ht_AND(p,q) and
I(g) = q V_p I+_a + p V_q I+_b with I+ = I/V, H+ = (H - h(V))/V; substituting H_i <= C I_i - Gamma(p_i) yields
H(g) <= C I(g) - [q(Gamma(p)+h(V_p)) + p(Gamma(q)+h(V_q)) - Ht_AND] <= C I(g) - Gamma(pq) by (A). OR is the
dual of AND (same H, I, complemented measures), so symmetry of Gamma covers it, and NOT preserves H, I.
The constraints are only needed at the (dyadic) measures that formulas realise; imposing them for all real p, q
is a relaxation, so the smallest Gamma(1/2) found here is a valid upper bound on the read-once constant.

Numerics: value iteration Gamma <- min(Gamma, T Gamma) from the cap Gamma(1/2) = C, Gamma = +inf elsewhere, on a
grid; feasible iff the limit is >= 0 everywhere; binary search on C. Off-grid values Gamma(r/p) are interpolated
linearly (not yet rigorous; an interval version would make the bound a theorem).
"""
import sys, math, time
import numpy as np

def h2(v):
    v = np.clip(v, 1e-300, 1 - 1e-16)
    return -v * np.log2(v) - (1 - v) * np.log2(1 - v)

def phi(w):
    w = np.clip(w, 0.0, 1.0)
    out = np.zeros_like(w); m = w > 1e-300
    out[m] = -w[m] * np.log2(w[m]); return out

def Ht_and(p, q):
    Vp = 4 * p * (1 - p); Vq = 4 * q * (1 - q)
    pr = p * q; Ita = q * Vp; Itb = p * Vq
    w0 = (1 - 2 * pr) ** 2; wab = w0 + Ita + Itb - 1
    return phi(w0) + phi(Ita - wab) + phi(Itb - wab) + phi(wab)

def iterate(C, N=2000, iters=400, tol=1e-10, verbose=False):
    ps = np.arange(1, N) / N                      # grid of measures
    G = np.full(N - 1, 60.0); G[N // 2 - 1] = C  # p = 1/2 is index N/2 - 1; elsewhere a large finite cap (the largest admissible Gamma under the cap at 1/2 is what the monotone iteration finds)
    hV = h2(4 * ps * (1 - ps))
    # precompute, for each r (index i) and each p >= r on the grid, q = r/p, interpolation weights for Gamma(q)
    # to keep memory sane, process r in chunks
    def T(G):
        newG = np.full_like(G, np.inf)
        Gi = np.concatenate([[np.inf], G, [np.inf]])   # pad: Gamma(0) = Gamma(1) = +inf (never used as a factor)
        for i0 in range(0, N - 1, 200):
            i1 = min(N - 1, i0 + 200)
            r = ps[i0:i1][:, None]                     # (R,1)
            p = ps[None, :]                            # (1,P)
            q = r / p                                  # (R,P)
            valid = (q < 1 - 1e-12) & (q > 1e-12)
            qc = np.clip(q, 1e-12, 1 - 1e-12)
            # linear interpolation of Gamma at q
            x = qc * N; j = np.floor(x).astype(int); t = x - j
            j = np.clip(j, 0, N)                       # index into padded array Gi (size N+1): Gi[k] = Gamma(k/N)
            Gl = Gi[j]; Gr = Gi[np.minimum(j + 1, N)]
            # inf-safe linear interpolation: a weight of exactly zero never touches an infinite endpoint
            Gq = np.where(t <= 0, Gl, np.where(t >= 1, Gr, np.where(np.isinf(Gl) | np.isinf(Gr), np.inf, (1 - t) * np.where(np.isinf(Gl), 0, Gl) + t * np.where(np.isinf(Gr), 0, Gr))))
            hq = h2(4 * qc * (1 - qc))
            rhs = q * (G[None, :] + hV[None, :]) + p * (Gq + hq) - Ht_and(p, qc)
            rhs = np.where(valid & np.isfinite(rhs), rhs, np.inf)
            newG[i0:i1] = np.min(rhs, axis=1)
        # symmetry: Gamma(r) = Gamma(1-r) -> the OR constraints
        newG = np.minimum(newG, newG[::-1])
        return newG
    for k in range(iters):
        TG = T(G)
        G2 = np.minimum(G, TG)
        if verbose and k % 20 == 0:
            print("  iter %3d: min Gamma %.6f at p=%.4f, Gamma(1/2)=%.6f, Gamma(1/4)=%.6f" % (k, G2.min(), ps[np.argmin(G2)], G2[N // 2 - 1], G2[N // 4 - 1]), flush=True)
        done = np.all((np.isinf(G) & np.isinf(G2)) | (np.abs(G2 - G) < tol))
        G = G2
        if G.min() < -1e-9:
            return False, G, ps
        if done:
            break
    return bool(G.min() >= -1e-9), G, ps

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    for C in (6.0, 6.4547837, 6.6, 7.0):
        t0 = time.time()
        ok, G, ps = iterate(C, N=N, iters=300, verbose=(C == 6.6))
        fin = np.isfinite(G)
        print("C = %.7f: %s  (min Gamma %.6f at p=%.4f; finite entries %d of %d; %.0f s)" % (C, "FEASIBLE" if ok else "infeasible", G.min(), ps[np.argmin(G)], fin.sum(), len(G), time.time() - t0), flush=True)
    # binary search
    lo, hi = 6.0, 7.5
    for _ in range(18):
        mid = (lo + hi) / 2
        ok, G, ps = iterate(mid, N=N, iters=300)
        if ok:
            hi = mid
        else:
            lo = mid
        print("  bisect: C=%.6f %s" % (mid, "feasible" if ok else "infeasible"), flush=True)
    print("smallest feasible C on grid N=%d: %.6f  (Hod lower bound 6.4547837)" % (N, hi))
