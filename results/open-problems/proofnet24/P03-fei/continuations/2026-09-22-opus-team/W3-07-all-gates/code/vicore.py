"""Value iteration of the slack function over read-once formulas with arbitrary gates and biased inputs.

V(r) = inf{ C I(F) - H(F) : F a read-once formula over the gate set, Pr[F true] = r }.  For a gate G on k inputs fed
by formulas of measures p_i on disjoint variables (composition identity, CONTEXT.md section 3),

    s_C(G(f_1..f_k)) = sum_i w_i (s_C(f_i) + h(V_i)) - Htilde_G(p),      w_i = It_i/V_i,  V_i = 4 p_i (1-p_i),

so V(p_out) <= sum_i w_i (V(p_i) + h(V_i)) - Htilde_G(p).  Base case V(1/2) <= C (one variable), V(0) = V(1) = 0.

Representation (as in F1/ro_gamma.py and the 09-21 certificate): on p <= 1/2 put x = log2(1/p), G(x) = V(p)/p,
piecewise linear in x through the grid nodes; V(1-p) = V(p); beyond x = K linear extrapolation with the last
slope (clipped at 0).  Moves:
  AND/OR   V(pq) <= q (V(p)+h(V_p)) + p (V(q)+h(V_q)) - Ht_AND(p,q)   (F1's numerically stable E-form)
  XOR      V(p + q - 2pq) <= V(p) + V(q)
  families (gate table, set K of biased inputs, one solver in K, the other inputs single variables at 1/2): the
           free biases run over given arrays, the solver's bias is solved so that Pr[F] lands exactly on each node.
Every compute-heavy entry point calls lowprio() first (BelowNormal, affinity [2,3,10..15]).
"""
import math, time
import numpy as np


def lowprio(threads=6):
    try:
        import psutil
        p = psutil.Process()
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
    except Exception:
        pass
    try:
        import numba
        numba.set_num_threads(threads)
    except Exception:
        pass


import numba as nb
from numba import prange

LN2 = math.log(2.0)


class Grid:
    """Nodes on (0, 1/2]: uniform step `mid_step` on [1/32, 1/2], M per octave below 1/32 down to 2^-K, and an optional
    finer uniform block (lo, step) on [lo, 1/2]."""

    def __init__(self, M=24, K=40, mid_step=2.0 ** -11, fine=None):
        mid = np.arange(int(round((1 / 32) / mid_step)), int(round(0.5 / mid_step)) + 1) * mid_step
        tail = 2.0 ** (-(5 + np.arange(1, (K - 5) * M + 1) / M))
        parts = [mid, tail]
        if fine is not None:
            lo, st = fine
            parts.append(np.arange(int(round(lo / st)), int(round(0.5 / st)) + 1) * st)
        ps = np.unique(np.concatenate(parts))[::-1]
        self.ps = ps
        self.N = len(ps)
        self.xs = np.log2(1.0 / ps)
        self.xs[0] = 1.0
        self.K = float(K)
        self.M = M
        self.mid_step = mid_step
        self.fine = fine
        self.rs = np.concatenate([ps, 1.0 - ps[1:]])          # output nodes: small side, then mirrors
        self.allp = np.unique(self.rs)
        self.Lall = np.log2(1.0 / self.allp)

    def sig(self, G):
        return max((G[-1] - G[-2]) / (self.xs[-1] - self.xs[-2]), 0.0)

    def V(self, G, q):
        q = np.atleast_1d(np.asarray(q, float))
        return v_vec(self.xs, G, self.K, self.sig(G), q)


# ----------------------------------------------------------------------------------------------------------------
# scalar primitives
# ----------------------------------------------------------------------------------------------------------------

@nb.njit(cache=True)
def vat(xs, G, K, sig, q):
    s = q if q < 1.0 - q else 1.0 - q
    if s <= 0.0:
        return 0.0
    x = -math.log2(s)
    if x >= K:
        return s * (G[-1] + (x - K) * sig)
    if x <= xs[0]:
        return s * G[0]
    j = np.searchsorted(xs, x) - 1
    n = xs.shape[0]
    if j < 0:
        j = 0
    if j > n - 2:
        j = n - 2
    t = (x - xs[j]) / (xs[j + 1] - xs[j])
    return s * ((1.0 - t) * G[j] + t * G[j + 1])


@nb.njit(parallel=True, cache=True)
def v_vec(xs, G, K, sig, q):
    out = np.empty(q.shape[0])
    for i in prange(q.shape[0]):
        out[i] = vat(xs, G, K, sig, q[i])
    return out


@nb.njit(cache=True)
def hV(p):
    """h(4p(1-p)) in bits, cancellation-free at both ends."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    if p > 0.5:
        p = 1.0 - p
    u = (1.0 - 2.0 * p) ** 2
    if u <= 0.0:
        return 0.0
    v = 4.0 * p * (1.0 - p)
    if u < 0.5:
        lv = math.log1p(-u) / LN2
    else:
        lv = math.log2(v)
    if p < 0.25:
        lu = 2.0 * math.log1p(-2.0 * p) / LN2
    else:
        lu = math.log2(u)
    return -v * lv - u * lu


@nb.njit(cache=True)
def psi_s(z):
    if z > 0.5:
        zz = 1.0 - z
        return psi_s(zz) * zz / z
    if z <= 0.25:
        u = 2.0 * z
        return (4.0 / LN2) * (1.0 - u) ** 2 * (-math.log1p(-u) / u)
    w = (1.0 - 2.0 * z) ** 2
    if w <= 0.0:
        return 0.0
    return -w * math.log2(w) / z


# ----------------------------------------------------------------------------------------------------------------
# AND / OR and XOR operators
# ----------------------------------------------------------------------------------------------------------------

@nb.njit(parallel=True, cache=True)
def T_and(xs, G, K, sig, rs, allp, Lall):
    nA = allp.shape[0]
    GamA = np.empty(nA)
    psiA = np.empty(nA)
    for a in range(nA):
        GamA[a] = vat(xs, G, K, sig, allp[a])
        psiA[a] = psi_s(allp[a])
    out = np.empty(rs.shape[0])
    arg = np.empty(rs.shape[0])
    for k in prange(rs.shape[0]):
        r = rs[k]
        best = np.inf
        bp = 0.0
        psir = psi_s(r)
        for a in range(nA):
            p = allp[a]
            if p <= r:
                continue
            q = r / p
            if q >= 1.0 - 1e-15:
                continue
            Lq = -math.log2(q)
            Gq = vat(xs, G, K, sig, q)
            E = 8 * p * (1 - q) * Lall[a] + 8 * q * (1 - p) * Lq + 8 * (1 - p) * (1 - q) + psir - psiA[a] - psi_s(q)
            v = q * GamA[a] + p * Gq - p * q * E
            if v < best:
                best = v
                bp = p
        out[k] = best
        arg[k] = bp
    return out, arg


@nb.njit(parallel=True, cache=True)
def T_xor(xs, G, K, sig, ps):
    """outputs at the small-side nodes ps (<= 1/2); both inputs <= 1/2 without loss of generality."""
    n = ps.shape[0]
    out = np.empty(n)
    for k in prange(n):
        r = ps[k]
        best = np.inf
        for a in range(n):
            p = ps[a]
            if p >= r:
                continue
            q = (r - p) / (1.0 - 2.0 * p)
            if q <= 0.0:
                continue
            v = vat(xs, G, K, sig, p) + vat(xs, G, K, sig, q)
            if v < best:
                best = v
        out[k] = best
    return out


# ----------------------------------------------------------------------------------------------------------------
# general gates
# ----------------------------------------------------------------------------------------------------------------

@nb.njit(cache=True)
def gmean(tab, k, p, buf):
    """E_mu[G] (the +-1 mean) at TRUE-probabilities p; entry x of tab has bit i = 1 iff input i TRUE."""
    n = 1 << k
    for x in range(n):
        buf[x] = tab[x]
    size = n
    for i in range(k):
        pi = p[i]
        half = size >> 1
        for y in range(half):
            buf[y] = (1.0 - pi) * buf[2 * y] + pi * buf[2 * y + 1]
        size = half
    return buf[0]


@nb.njit(cache=True)
def gstats(tab, k, p, buf, It):
    """biased spectrum at p: returns (mean, Htilde); fills It[i] = sum_{T ni i} Ghat_mu(T)^2."""
    n = 1 << k
    for x in range(n):
        buf[x] = tab[x]
    h = 1
    for i in range(k):
        pi = p[i]
        s = math.sqrt(pi * (1.0 - pi))
        for base in range(0, n, 2 * h):
            for off in range(h):
                a0 = buf[base + off]
                a1 = buf[base + off + h]
                buf[base + off] = (1.0 - pi) * a0 + pi * a1
                buf[base + off + h] = s * (a0 - a1)
        h *= 2
    Ht = 0.0
    for i in range(k):
        It[i] = 0.0
    for T in range(n):
        w = buf[T] * buf[T]
        if w > 0.0:
            Ht -= w * math.log2(w)
            t = T
            i = 0
            while t:
                if t & 1:
                    It[i] += w
                t >>= 1
                i += 1
    return buf[0], Ht


@nb.njit(parallel=True, cache=True)
def D_batch(tab, k, P, xs, G, K, sig):
    """gate defect D = sum_i w_i (V(p_i)+h(V_i)) - Ht - V(p_out), Poincare denominator W and p_out, for each row of P."""
    nb_ = P.shape[0]
    D = np.empty(nb_)
    Wd = np.empty(nb_)
    po = np.empty(nb_)
    for b in prange(nb_):
        buf = np.empty(1 << k)
        It = np.empty(k)
        p = P[b]
        mean, Ht = gstats(tab, k, p, buf, It)
        pout = 0.5 * (1.0 - mean)
        if pout < 0.0:
            pout = 0.0
        if pout > 1.0:
            pout = 1.0
        s = -Ht
        sw = 0.0
        for i in range(k):
            Vi = 4.0 * p[i] * (1.0 - p[i])
            sw += It[i]
            if Vi > 0.0:
                s += It[i] / Vi * (vat(xs, G, K, sig, p[i]) + hV(p[i]))
        D[b] = s - vat(xs, G, K, sig, pout)
        Wd[b] = sw / 4.0 - pout * (1.0 - pout)
        po[b] = pout
    return D, Wd, po


@nb.njit(parallel=True, cache=True)
def S_batch(tab, k, P, xs, G, K, sig):
    """composition slack s = sum_i w_i (V(p_i)+h(V_i)) - Ht and p_out for each row of P."""
    nb_ = P.shape[0]
    S = np.empty(nb_)
    po = np.empty(nb_)
    for b in prange(nb_):
        buf = np.empty(1 << k)
        It = np.empty(k)
        p = P[b]
        mean, Ht = gstats(tab, k, p, buf, It)
        po[b] = 0.5 * (1.0 - mean)
        s = -Ht
        for i in range(k):
            Vi = 4.0 * p[i] * (1.0 - p[i])
            if Vi > 0.0:
                s += It[i] / Vi * (vat(xs, G, K, sig, p[i]) + hV(p[i]))
        S[b] = s
    return S, po


# ---- families: free biases on arrays, one solver solved per output node ----

@nb.njit(parallel=True, cache=True)
def fam_ab(tab, k, pbase, Kidx, js, FP):
    """for each free configuration (rows of FP, one column per entry of Kidx; column js ignored) the output mean is
    e0 + (e1-e0) p_solver."""
    nf = FP.shape[0]
    m = Kidx.shape[0]
    e0 = np.empty(nf)
    e1 = np.empty(nf)
    for f in prange(nf):
        buf = np.empty(1 << k)
        p = pbase.copy()
        for q in range(m):
            p[Kidx[q]] = FP[f, q]
        p[Kidx[js]] = 0.0
        e0[f] = gmean(tab, k, p, buf)
        p[Kidx[js]] = 1.0
        e1[f] = gmean(tab, k, p, buf)
    return e0, e1


@nb.njit(parallel=True, cache=True)
def fam_count(e0, e1, rs, plo, phi):
    R = rs.shape[0]
    nf = e0.shape[0]
    cnt = np.zeros(R, dtype=np.int64)
    for r in prange(R):
        tgt = 1.0 - 2.0 * rs[r]
        c = 0
        for f in range(nf):
            d = e1[f] - e0[f]
            if d == 0.0:
                continue
            pj = (tgt - e0[f]) / d
            if pj > plo and pj < phi:
                c += 1
        cnt[r] = c
    return cnt


@nb.njit(parallel=True, cache=True)
def fam_fill(tab, k, pbase, Kidx, js, FP, e0, e1, rs, plo, phi, off, P, W, c0, Ir, fidx):
    R = rs.shape[0]
    nf = FP.shape[0]
    m = Kidx.shape[0]
    for r in prange(R):
        buf = np.empty(1 << k)
        It = np.empty(k)
        p = pbase.copy()
        tgt = 1.0 - 2.0 * rs[r]
        idx = off[r]
        for f in range(nf):
            d = e1[f] - e0[f]
            if d == 0.0:
                continue
            pj = (tgt - e0[f]) / d
            if not (pj > plo and pj < phi):
                continue
            for q in range(m):
                p[Kidx[q]] = FP[f, q]
            p[Kidx[js]] = pj
            mean, Ht = gstats(tab, k, p, buf, It)
            irest = 0.0
            for i in range(k):
                irest += It[i]
            cc = -Ht
            for q in range(m):
                i = Kidx[q]
                irest -= It[i]
                Vi = 4.0 * p[i] * (1.0 - p[i])
                wq = It[i] / Vi
                P[idx, q] = p[i]
                W[idx, q] = wq
                cc += wq * hV(p[i])
            c0[idx] = cc
            Ir[idx] = irest
            fidx[idx] = f
            idx += 1


@nb.njit(parallel=True, cache=True)
def fam_sweep(xs, G, K, sig, C, off, P, W, c0, Ir):
    R = off.shape[0] - 1
    out = np.full(R, np.inf)
    arg = np.full(R, -1, dtype=np.int64)
    m = P.shape[1]
    for r in prange(R):
        best = np.inf
        ba = -1
        for idx in range(off[r], off[r + 1]):
            v = c0[idx] + C * Ir[idx]
            for q in range(m):
                v += W[idx, q] * vat(xs, G, K, sig, P[idx, q])
            if v < best:
                best = v
                ba = idx
        out[r] = best
        arg[r] = ba
    return out, arg


class Family:
    """gate `tab` (+-1 array, length 2^k); inputs in Kidx biased (free biases from `free` arrays, solver Kidx[js]);
    the remaining inputs are single variables at 1/2.  Output nodes restricted to `rs` (a subset of grid.rs, given as
    indices into grid.rs)."""

    def __init__(self, name, tab, Kidx, js, free_arrays, grid, r_index=None, plo=2.0 ** -40, phi=1 - 2.0 ** -40,
                 FP=None):
        self.name = name
        tab = np.asarray(tab, float)
        k = int(round(math.log2(len(tab))))
        self.k = k
        self.tab = tab
        self.Kidx = np.asarray(Kidx, np.int64)
        self.js = int(js)
        m = len(Kidx)
        if FP is None:
            # free configurations: cartesian product over the non-solver positions
            cols = []
            for q in range(m):
                cols.append(np.asarray(free_arrays[q], float) if q != js else np.array([0.5]))
            mesh = np.meshgrid(*cols, indexing="ij")
            FP = np.stack([a.ravel() for a in mesh], axis=1)
        FP = np.ascontiguousarray(np.asarray(FP, float).reshape(-1, m))
        self.FP = FP
        pbase = np.full(k, 0.5)
        e0, e1 = fam_ab(tab, k, pbase, self.Kidx, self.js, FP)
        if r_index is None:
            r_index = np.arange(len(grid.rs))
        self.r_index = np.asarray(r_index, np.int64)
        rs = grid.rs[self.r_index]
        cnt = fam_count(e0, e1, rs, plo, phi)
        off = np.zeros(len(rs) + 1, np.int64)
        off[1:] = np.cumsum(cnt)
        n = int(off[-1])
        self.n = n
        self.P = np.empty((n, m))
        self.W = np.empty((n, m))
        self.c0 = np.empty(n)
        self.Ir = np.empty(n)
        self.fidx = np.empty(n, np.int64)
        fam_fill(tab, k, pbase, self.Kidx, self.js, FP, e0, e1, rs, plo, phi, off, self.P, self.W, self.c0, self.Ir,
                 self.fidx)
        self.off = off

    def sweep(self, grid, G, C):
        out, arg = fam_sweep(grid.xs, G, grid.K, grid.sig(G), C, self.off, self.P, self.W, self.c0, self.Ir)
        full = np.full(len(grid.rs), np.inf)
        full[self.r_index] = out
        return full, arg

    def config(self, j):
        """full bias vector of stored configuration j"""
        p = np.full(self.k, 0.5)
        for q, i in enumerate(self.Kidx):
            p[i] = self.P[j, q]
        return p


# ----------------------------------------------------------------------------------------------------------------
# the iteration
# ----------------------------------------------------------------------------------------------------------------

def iterate(grid, C, families=(), use_xor=True, iters=3000, tol=1e-12, cap=60.0, G0=None, verbose=True,
            every=10, stop_below=True, fam_every=1, log=print):
    """V <- min(V, T V).  Returns dict(ok, G, reason, it, hist)."""
    ps = grid.ps
    N = grid.N
    if G0 is None:
        Gam = np.full(N, cap)
        Gam[0] = C
    else:
        Gam = np.minimum(G0 * ps, np.inf)
        Gam[0] = min(Gam[0], C)
    G = Gam / ps
    t0 = time.time()
    hist = []
    reason = "converged"
    it = 0
    for it in range(iters):
        sig = grid.sig(G)
        Tv, _ = T_and(grid.xs, G, grid.K, sig, grid.rs, grid.allp, grid.Lall)
        if use_xor:
            tx = T_xor(grid.xs, G, grid.K, sig, ps)
            Tv[:N] = np.minimum(Tv[:N], tx)
        if families and (it % fam_every == 0):
            for fam in families:
                b, _ = fam.sweep(grid, G, C)
                Tv = np.minimum(Tv, b)
        Ts = Tv[:N].copy()
        Ts[1:] = np.minimum(Ts[1:], Tv[N:])
        Gam2 = np.minimum(Gam, Ts)
        diff = np.max(np.abs(Gam2 - Gam) / ps)
        Gam = Gam2
        G = Gam / ps
        hist.append((it, Gam[0] - C, Gam.min(), diff))
        if verbose and (it % every == 0):
            log("  it %4d  max dG %.3e  min V %.4e  V(1/2)-C %+.3e  (%.0f s)" % (it, diff, Gam.min(), Gam[0] - C,
                                                                             time.time() - t0))
        if stop_below and (Gam.min() < -1e-9 or Gam[0] < C - 1e-10):
            reason = "diverged"
            break
        if diff < tol:
            break
    if verbose:
        log("  end it %d: %s  V(1/2)-C %+.3e  min V %.4e  (%.0f s)" % (it, reason, Gam[0] - C, Gam.min(), time.time() - t0))
    return dict(ok=(reason == "converged"), G=G, reason=reason, it=it, hist=hist)


def pm_from_int(tt, k):
    n = 1 << k
    return np.array([1.0 - 2.0 * ((int(tt) >> x) & 1) for x in range(n)])


@nb.njit(cache=True)
def D_serial(tab, k, P, xs, G, K, sig):
    """serial twin of D_batch (small batches: no thread synchronisation on a loaded machine)"""
    nb_ = P.shape[0]
    D = np.empty(nb_)
    Wd = np.empty(nb_)
    po = np.empty(nb_)
    buf = np.empty(1 << k)
    It = np.empty(k)
    for b in range(nb_):
        p = P[b]
        mean, Ht = gstats(tab, k, p, buf, It)
        pout = 0.5 * (1.0 - mean)
        if pout < 0.0:
            pout = 0.0
        if pout > 1.0:
            pout = 1.0
        s = -Ht
        sw = 0.0
        for i in range(k):
            Vi = 4.0 * p[i] * (1.0 - p[i])
            sw += It[i]
            if Vi > 0.0:
                s += It[i] / Vi * (vat(xs, G, K, sig, p[i]) + hV(p[i]))
        D[b] = s - vat(xs, G, K, sig, pout)
        Wd[b] = sw / 4.0 - pout * (1.0 - pout)
        po[b] = pout
    return D, Wd, po
