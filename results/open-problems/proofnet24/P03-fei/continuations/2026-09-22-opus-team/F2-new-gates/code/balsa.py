"""Exact-balance annealing over G-invariant partial cores (plain groups).  Every move changes one orbit and a
compensating orbit so that sum c0 stays 0.  Uses Model2 from orbsa2."""
import numpy as np
from orbsa2 import phi_sum, add_row


def balance_greedy(M, v, rng, hole_frac=0.7):
    size = M.size
    v = v.copy()
    bal = int((size * v).sum())
    tries = 0
    while bal != 0 and tries < 100000:
        tries += 1
        sgn = 1 if bal > 0 else -1
        cands = [o for o in range(M.no) if v[o] == sgn and size[o] <= abs(bal)]
        if not cands:
            cands = [o for o in range(M.no) if v[o] == sgn]
        o = cands[rng.integers(len(cands))]
        if 2 * size[o] <= abs(bal) and rng.random() > hole_frac:
            v[o] = -sgn
        else:
            v[o] = 0
        bal = int((size * v).sum())
    return v


def _state(M, v):
    W = v @ M.B
    Ev = M.E @ v
    Dvv = int((M.D * v * v).sum()); vEv = int(v @ Ev)
    Ha, I2a, _, _ = M.aux(v)
    return W, Ev, Dvv, vEv, Ha, I2a


def anneal_bal(M, v, iters, T0, T1, rng, hole_ok=None):
    N = M.N
    size = M.size
    by_size = {}
    for o in range(M.no):
        by_size.setdefault(int(size[o]), []).append(o)
    if hole_ok is None:
        hole_ok = np.ones(M.no, dtype=bool)
    v = v.copy()
    W, Ev, Dvv, vEv, Ha, I2a = _state(M, v)
    Hc = phi_sum(W, M.phi)

    def ratio(Hc, Dvv, vEv, Ha, I2a):
        I = (Dvv - vEv + I2a) / (2.0 * N)
        return (Hc + Ha) / (I - 1.0) if I > 1 + 1e-12 else -1e9

    R = ratio(Hc, Dvv, vEv, Ha, I2a)
    best, bestR = v.copy(), R
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters)
        o1 = int(rng.integers(M.no))
        opts1 = (-1, 0, 1) if hole_ok[o1] else (-1, 1)
        nv1 = opts1[rng.integers(len(opts1))]
        if nv1 == v[o1]:
            continue
        d1 = int(size[o1]) * (nv1 - v[o1])
        opts = []
        for s2, dv2 in ((abs(d1), -int(np.sign(d1))), ((abs(d1) // 2) if abs(d1) % 2 == 0 else -1, -2 * int(np.sign(d1)))):
            if s2 <= 0:
                continue
            for o2 in by_size.get(s2, []):
                if o2 == o1:
                    continue
                nv2 = int(v[o2]) + dv2
                if -1 <= nv2 <= 1 and (nv2 != 0 or hole_ok[o2]):
                    opts.append((o2, nv2))
        if not opts:
            continue
        o2, nv2 = opts[rng.integers(len(opts))]
        moves = [(o1, nv1), (o2, nv2)]
        old = {o: int(v[o]) for o, _ in moves}
        Dvv_n, vEv_n = Dvv, vEv
        Ev_n = Ev.copy()
        for o, nvv in moves:
            dv = nvv - int(v[o])
            Dvv_n += int(M.D[o]) * (nvv * nvv - int(v[o]) ** 2)
            vEv_n += 2 * dv * int(Ev_n[o]) + int(M.E[o, o]) * dv * dv
            Ev_n += M.E[:, o] * dv
            add_row(W, M.B, o, dv)
            v[o] = nvv
        Hc_n = phi_sum(W, M.phi)
        if any(old[o] == 0 or nvv == 0 for o, nvv in moves):
            Ha_n, I2a_n, _, _ = M.aux(v)
        else:
            Ha_n, I2a_n = Ha, I2a
        R_n = ratio(Hc_n, Dvv_n, vEv_n, Ha_n, I2a_n)
        if R_n >= R or rng.random() < np.exp((R_n - R) / T):
            Dvv, vEv, Ev, Hc, Ha, I2a, R = Dvv_n, vEv_n, Ev_n, Hc_n, Ha_n, I2a_n, R_n
            if R > bestR:
                bestR, best = R, v.copy()
        else:
            for o, nvv in moves:
                add_row(W, M.B, o, old[o] - nvv)
                v[o] = old[o]
    return best, bestR
