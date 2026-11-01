"""Faster orbit machinery (numba BFS orbits) and a penalty annealer with single-orbit moves.
Objective during the walk: R_formal - pen*|sum c0|; only exactly balanced states are recorded."""
import numpy as np
import numba as nb
from holecore import fwht_int, make_phi, make_par, aux_part, aux_part2


@nb.njit(cache=True)
def bfs_orbits(m, gens, gsgn):
    N = 1 << m
    full = N - 1
    ng = gens.shape[0]
    rep = -np.ones(N, dtype=np.int64)
    sgn = np.zeros(N, dtype=np.int64)
    forced = np.zeros(N, dtype=np.bool_)
    stack = np.empty(N, dtype=np.int64)
    no = 0
    for x0 in range(N):
        if rep[x0] >= 0:
            continue
        rep[x0] = no; sgn[x0] = 1
        top = 0; stack[top] = x0; top += 1
        bad = False
        while top > 0:
            top -= 1
            x = stack[top]
            for g in range(ng):
                y = 0
                for i in range(m):
                    if (x >> i) & 1:
                        y |= 1 << gens[g, i]
                if gsgn[g] < 0:
                    y ^= full
                s = sgn[x] * gsgn[g]
                if rep[y] < 0:
                    rep[y] = no; sgn[y] = s
                    stack[top] = y; top += 1
                elif sgn[y] != s:
                    bad = True
        forced[no] = bad
        no += 1
    return rep, sgn, forced[:no].copy(), no


@nb.njit(cache=True)
def build_B(rep, sgn, no, N):
    B = np.zeros((no, N), dtype=np.int64)
    for x in range(N):
        B[rep[x], x] = sgn[x]
    for o in range(no):
        B[o] = fwht_int(B[o])
    return B


@nb.njit(cache=True)
def build_E(rep, sgn, no, m):
    N = 1 << m
    D = np.zeros(no, dtype=np.int64)
    E = np.zeros((no, no), dtype=np.int64)
    for x in range(N):
        for i in range(m):
            y = x ^ (1 << i)
            if y > x:
                a = rep[x]; b = rep[y]
                D[a] += 1; D[b] += 1
                E[a, b] += sgn[x] * sgn[y]
                E[b, a] += sgn[x] * sgn[y]
    return D, E


@nb.njit(cache=True)
def phi_sum(W, phi):
    s = 0.0
    for S in range(W.shape[0]):
        s += phi[abs(W[S])]
    return s


@nb.njit(cache=True)
def add_row(W, B, o, dv):
    for S in range(W.shape[0]):
        W[S] += dv * B[o, S]


class Model2:
    def __init__(self, m, perms, dual_perms=()):
        self.m = m; self.N = N = 1 << m
        gl = [list(p) for p in perms] + [list(p) for p in dual_perms]
        gs = [1] * len(perms) + [-1] * len(dual_perms)
        gens = np.array(gl, dtype=np.int64); gsgn = np.array(gs, dtype=np.int64)
        rep, sgn, forced, no = bfs_orbits(m, gens, gsgn)
        self.rep, self.sgn, self.forced, self.no = rep, sgn, forced, no
        self.size = np.bincount(rep, minlength=no)
        self.sigma = np.zeros(no, dtype=np.int64); np.add.at(self.sigma, rep, sgn)
        self.B = build_B(rep, sgn, no, N)
        self.D, self.E = build_E(rep, sgn, no, m)
        self.phi = make_phi(N); self.par = make_par(N)
        self.cache = {}

    def c0(self, v):
        return (self.sgn * np.asarray(v)[self.rep]).astype(np.int64)

    def aux(self, v):
        key = np.packbits(np.asarray(v) == 0).tobytes()
        r = self.cache.get(key)
        if r is None:
            c = np.where(np.asarray(v)[self.rep] == 0, 0, 1).astype(np.int64)
            if getattr(self, 'grouping', 'match') == 'match':
                Ha, I2a, ng, grp = aux_part2(c, self.m, self.phi, self.par, 6.52)
                r = (Ha, I2a, ng, 0)
            else:
                Ha, I2a, nc, mx = aux_part(c, self.m, self.phi, self.par)
                r = (Ha, I2a, nc, mx)
            self.cache[key] = r
        return r

    def evaluate(self, v):
        v = np.asarray(v, dtype=np.int64)
        W = v @ self.B
        Hc = phi_sum(W, self.phi)
        I2c = int((self.D * v * v).sum()) - int(v @ self.E @ v)
        Ha, I2a, nc, mx = self.aux(v)
        I = (I2c + I2a) / (2.0 * self.N)
        bal = int((self.sigma * v).sum())
        return ((Hc + Ha) / (I - 1.0) if I > 1 else -1e9), I, bal


def anneal_pen(model, v0, iters, T0, T1, seed, pen=0.01, hole_ok=None, verbose=False):
    rng = np.random.default_rng(seed)
    M = model; N = M.N
    v = np.array(v0, dtype=np.int64)
    if hole_ok is None:
        hole_ok = np.ones(M.no, dtype=bool)
    W = v @ M.B
    Hc = phi_sum(W, M.phi)
    Ev = M.E @ v
    Dvv = int((M.D * v * v).sum()); vEv = int(v @ Ev)
    bal = int((M.sigma * v).sum())
    Ha, I2a, nc, mx = M.aux(v)

    def score(Hc, Dvv, vEv, Ha, I2a, bal):
        I = (Dvv - vEv + I2a) / (2.0 * N)
        if I <= 1.0 + 1e-12:
            return -1e9, -1e9
        R = (Hc + Ha) / (I - 1.0)
        return R - pen * abs(bal), R

    J, R = score(Hc, Dvv, vEv, Ha, I2a, bal)
    bestR = R if bal == 0 else -1e9
    best = v.copy()
    free = np.where(~M.forced)[0]
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        o = free[rng.integers(len(free))]
        opts = (-1, 0, 1) if hole_ok[o] else (-1, 1)
        nv = opts[rng.integers(len(opts))]
        if nv == v[o]:
            continue
        dv = nv - v[o]
        # incremental pieces
        Dvv_n = Dvv + M.D[o] * (nv * nv - v[o] * v[o])
        vEv_n = vEv + 2 * dv * Ev[o] + M.E[o, o] * dv * dv
        bal_n = bal + M.sigma[o] * dv
        add_row(W, M.B, o, dv)
        Hc_n = phi_sum(W, M.phi)
        old = v[o]; v[o] = nv
        if old == 0 or nv == 0:
            Ha_n, I2a_n, _, _ = M.aux(v)
        else:
            Ha_n, I2a_n = Ha, I2a
        J_n, R_n = score(Hc_n, Dvv_n, vEv_n, Ha_n, I2a_n, bal_n)
        if J_n >= J or rng.random() < np.exp((J_n - J) / T):
            Ev += M.E[:, o] * dv
            Dvv, vEv, bal, Hc, Ha, I2a, J, R = Dvv_n, vEv_n, bal_n, Hc_n, Ha_n, I2a_n, J_n, R_n
            if bal == 0 and R > bestR:
                bestR = R; best = v.copy()
                if verbose:
                    print(f"   it {it}: balanced R = {R:.12f}", flush=True)
        else:
            v[o] = old
            add_row(W, M.B, o, -dv)
    return best, bestR
