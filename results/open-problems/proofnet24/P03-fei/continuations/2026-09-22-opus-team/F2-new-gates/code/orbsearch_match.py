"""Search over partial cores invariant under a group G of signed coordinate
permutations (plain: c0(pi x) = c0(x); dual: c0(~pi x) = -c0(x)).

Orbit values v_o in {-1,0,1}; c0(x) = sgn[x] v[rep[x]].
  W0 = sum_o v_o B_o                  (B_o = Walsh transform of the signed orbit indicator)
  I2core = sum_o v_o^2 D_o - 2 sum_{o<=o'} v_o v_o' E_oo'   (edge quadratic form)
  aux part = function of the hole mask {o : v_o = 0} (cached).
Balance: sum_o v_o sigma_o = 0 with sigma_o = sum_{x in o} sgn[x].
"""
import numpy as np
import numba as nb
from holecore import fwht_int, make_phi, make_par, aux_part, aux_part2, core_I2, summarize
from orbits import orbit_structure


class OrbitModel:
    def __init__(self, m, gens, hole_ok=None):
        self.m = m; N = self.N = 1 << m
        rep, sgn, forced = orbit_structure(m, gens)
        self.rep, self.sgn, self.forced = rep, sgn, forced
        no = self.no = len(forced)
        self.size = np.bincount(rep, minlength=no)
        self.sigma = np.zeros(no, dtype=np.int64)
        np.add.at(self.sigma, rep, sgn)
        B = np.zeros((no, N), dtype=np.int64)
        for o in range(no):
            ind = np.zeros(N, dtype=np.int64)
            xs = np.where(rep == o)[0]
            ind[xs] = sgn[xs]
            B[o] = fwht_int(ind)
        self.B = B
        # edge form
        D = np.zeros(no, dtype=np.int64)
        E = np.zeros((no, no), dtype=np.int64)
        for x in range(N):
            for i in range(m):
                y = x ^ (1 << i)
                if y > x:
                    a, b = rep[x], rep[y]
                    D[a] += 1; D[b] += 1
                    E[a, b] += sgn[x] * sgn[y]
        self.D = D
        self.E = E + E.T  # symmetric: I2 = sum D_o v_o^2 - sum_{a,b} E_ab v_a v_b  (E sym, full sum)
        self.phi = make_phi(N); self.par = make_par(N)
        pc = np.array([bin(x).count('1') for x in range(N)])
        self.layers = [sorted(set(pc[rep == o].tolist())) for o in range(no)]
        if hole_ok is None:
            hole_ok = np.ones(no, dtype=bool)
        self.hole_ok = np.asarray(hole_ok, dtype=bool) & ~np.zeros(no, dtype=bool)
        self.cache = {}

    def c0(self, v):
        return (self.sgn * v[self.rep]).astype(np.int64)

    def aux(self, v):
        mask = tuple(np.where(v == 0)[0].tolist())
        r = self.cache.get(mask)
        if r is None:
            c = self.c0(v)
            Ha, I2a, nc, mx = aux_part(c, self.m, self.phi, self.par)
            r = (Ha, I2a, nc, mx)
            self.cache[mask] = r
        return r

    def I2core(self, v):
        # sum over edges (c0(x)-c0(y))^2 = sum_o D_o v_o^2 - v^T E v   (E symmetric, counts each edge twice)
        return int((self.D * v * v).sum()) - int(v @ self.E @ v)

    def evaluate(self, v):
        v = np.asarray(v, dtype=np.int64)
        W = v @ self.B
        Hc = float(self.phi[np.abs(W)].sum())
        I2c = self.I2core(v)
        Ha, I2a, nc, mx = self.aux(v)
        I = (I2c + I2a) / (2.0 * self.N)
        if I <= 1.0:
            return -1e9, I
        return (Hc + Ha) / (I - 1.0), I


@nb.njit(cache=True)
def phi_sum(W, phi):
    s = 0.0
    for S in range(W.shape[0]):
        s += phi[abs(W[S])]
    return s


def check_I2(model, v):
    c = model.c0(np.asarray(v, dtype=np.int64))
    a = core_I2(c, model.m)
    vv = np.asarray(v, dtype=np.int64)
    b = model.I2core(vv)
    return a, b


def anneal_orbits(model, v0, iters, T0, T1, seed, balance_needed=None, verbose=False):
    rng = np.random.default_rng(seed)
    v = np.array(v0, dtype=np.int64)
    no = model.no
    if balance_needed is None:
        balance_needed = bool(np.any(model.sigma != 0))
    W = v @ model.B
    phi = model.phi
    Hc = phi_sum(W, phi)
    DvE = None
    I2c = model.I2core(v)
    Ha, I2a, nc, mx = model.aux(v)
    N = model.N
    def ratio(Hc, I2c, Ha, I2a):
        I = (I2c + I2a) / (2.0 * N)
        return (Hc + Ha) / (I - 1.0) if I > 1.0 + 1e-12 else -1e9
    R = ratio(Hc, I2c, Ha, I2a)
    best = v.copy(); bestR = R
    free = np.where(~model.forced)[0]
    Ev = model.E @ v
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        o1 = free[rng.integers(len(free))]
        choices = [-1, 0, 1] if model.hole_ok[o1] else [-1, 1]
        nv1 = choices[rng.integers(len(choices))]
        if nv1 == v[o1]:
            continue
        moves = [(o1, nv1)]
        if balance_needed:
            d = model.sigma[o1] * (nv1 - v[o1])
            if d != 0:
                # find a compensating orbit move
                cand = []
                for _ in range(40):
                    o2 = free[rng.integers(len(free))]
                    if o2 == o1:
                        continue
                    for nv2 in ((-1, 0, 1) if model.hole_ok[o2] else (-1, 1)):
                        if nv2 != v[o2] and model.sigma[o2] * (nv2 - v[o2]) == -d:
                            cand.append((o2, nv2))
                    if cand:
                        break
                if not cand:
                    continue
                moves.append(cand[rng.integers(len(cand))])
        # evaluate
        vn = v.copy()
        for o, nvv in moves:
            vn[o] = nvv
        Wn = W.copy()
        for o, nvv in moves:
            Wn += (nvv - v[o]) * model.B[o]
        Hcn = phi_sum(Wn, phi)
        I2cn = model.I2core(vn)
        Han, I2an, ncn, mxn = model.aux(vn)
        Rn = ratio(Hcn, I2cn, Han, I2an)
        if Rn >= R or rng.random() < np.exp((Rn - R) / T):
            v = vn; W = Wn; Hc = Hcn; I2c = I2cn; Ha = Han; I2a = I2an; R = Rn
            if R > bestR:
                bestR = R; best = v.copy()
                if verbose:
                    print(f"  it {it} new best {bestR:.12f}", flush=True)
    return best, bestR


@nb.njit(cache=True)
def enum_fast(B, Dv, E, sigma, rep, m, phi, par, masks, hole_orbs, topk, need_balance):
    """Exhaustive: for each hole mask (bitmask over hole_orbs), all +-1 sign vectors of
    the other orbits (first free orbit fixed to +1 by the global sign symmetry)."""
    no, N = B.shape
    outR = np.full(topk, -1e9)
    outV = np.zeros((topk, no), dtype=np.int64)
    c = np.ones(N, dtype=np.int64)
    v = np.zeros(no, dtype=np.int64)
    W = np.zeros(N, dtype=np.int64)
    Ev = np.zeros(no, dtype=np.int64)
    nh = hole_orbs.shape[0]
    for mi in range(masks.shape[0]):
        mask = masks[mi]
        isz = np.zeros(no, dtype=np.bool_)
        for j in range(nh):
            if (mask >> j) & 1:
                isz[hole_orbs[j]] = True
        for x in range(N):
            c[x] = 0 if isz[rep[x]] else 1
        Ha, I2a, nc, grp_ = aux_part2(c, m, phi, par, 6.52)
        free = np.zeros(no, dtype=np.int64); k = 0
        for o in range(no):
            if not isz[o]:
                free[k] = o; k += 1
        if k == 0:
            continue
        for o in range(no):
            v[o] = 0 if isz[o] else 1
        for S in range(N):
            W[S] = 0
        for j in range(k):
            o = free[j]
            for S in range(N):
                W[S] += B[o, S]
        for a in range(no):
            s_ = 0
            for b in range(no):
                s_ += E[a, b] * v[b]
            Ev[a] = s_
        vEv = 0; Dvv = 0; bal = 0
        for a in range(no):
            vEv += v[a] * Ev[a]; Dvv += Dv[a] * v[a] * v[a]; bal += sigma[a] * v[a]
        total = 1 << (k - 1)
        for t in range(total):
            if t > 0:
                # flip bit j = ctz(t) among free[1..k-1]
                j = 0; tt = t
                while (tt & 1) == 0:
                    tt >>= 1; j += 1
                o = free[j + 1]
                dv = -2 * v[o]
                # update vEv: new = old + 2 dv Ev[o] + E[o,o] dv^2
                vEv += 2 * dv * Ev[o] + E[o, o] * dv * dv
                for a in range(no):
                    Ev[a] += E[a, o] * dv
                bal += sigma[o] * dv
                v[o] += dv
                for S in range(N):
                    W[S] += dv * B[o, S]
            if need_balance and bal != 0:
                continue
            I2c = Dvv - vEv
            I = (I2c + I2a) / (2.0 * N)
            if I <= 1.0 + 1e-12:
                continue
            Hc = 0.0
            for S in range(N):
                Hc += phi[abs(W[S])]
            R = (Hc + Ha) / (I - 1.0)
            if R > outR[topk - 1]:
                jj = topk - 1
                while jj > 0 and outR[jj - 1] < R:
                    outR[jj] = outR[jj - 1]; outV[jj] = outV[jj - 1]; jj -= 1
                outR[jj] = R; outV[jj] = v
    return outR, outV


def run_enum(model, hole_orbs=None, topk=20, need_balance=None, max_holes_orbits=None):
    if hole_orbs is None:
        hole_orbs = np.where(model.hole_ok & ~model.forced)[0]
    hole_orbs = np.asarray(hole_orbs, dtype=np.int64)
    # forced-zero orbits are always holes: include them in every mask
    forced = np.where(model.forced)[0]
    allh = np.concatenate([hole_orbs, forced]).astype(np.int64)
    nh = len(hole_orbs)
    masks = []
    for mk in range(1 << nh):
        if max_holes_orbits is not None and bin(mk).count('1') > max_holes_orbits:
            continue
        masks.append(mk | (((1 << len(forced)) - 1) << nh))
    masks = np.array(masks, dtype=np.int64)
    if need_balance is None:
        need_balance = bool(np.any(model.sigma != 0))
    Dv = model.D.astype(np.int64)
    return enum_fast(model.B, Dv, model.E.astype(np.int64), model.sigma.astype(np.int64), model.rep,
                     model.m, model.phi, model.par, masks, allh, topk, need_balance)
