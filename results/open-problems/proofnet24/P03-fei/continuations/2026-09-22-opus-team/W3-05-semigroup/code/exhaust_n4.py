"""Exhaustive tests over all Boolean functions on n <= 4 variables (65536 at n = 4).

For every function: H, I, the KKL split H = K + R, the terminal entropy H(q_inf), and on a t-grid the
tilted-law flux -dH(q_t)/dt against E_t|S| and Var_t|S|, the unnormalized flux G(t) against
M(t), N(t), Kr(t), and the gauged identity H = H_inf + 2 int Cov_t(|S xor U|, L) dt.
Entropies in nats unless marked bits.
"""
import math, itertools
import numpy as np
from fei_core import lowprio, popcounts

lowprio()
LN2 = math.log(2)


def hadamard(n):
    N = 1 << n
    idx = np.arange(N)
    M = np.empty((N, N))
    for S in range(N):
        pc = np.zeros(N, dtype=np.int64)
        v = idx & S
        for i in range(n):
            pc += (v >> i) & 1
        M[:, S] = np.where(pc % 2 == 1, -1.0, 1.0)
    return M


def run(n, tgrid):
    N = 1 << n
    nf = 1 << N
    codes = np.arange(nf, dtype=np.int64)
    F = np.empty((nf, N))
    for x in range(N):
        F[:, x] = np.where((codes >> x) & 1, -1.0, 1.0)
    Hd = hadamard(n)
    A = F @ Hd / N
    W = A * A
    W[W < 1e-15] = 0.0
    k = popcounts(n).astype(float)
    pos = W > 0
    L = np.zeros_like(W); L[pos] = -np.log(W[pos])
    H = (W * L).sum(1)
    I = (W * k).sum(1)
    nonconst = I > 1e-12
    # influences and KKL split
    idx = np.arange(N)
    inf = np.stack([(W[:, ((idx >> i) & 1) == 1]).sum(1) for i in range(n)], 1)
    linf = np.where(inf > 0, -np.log(np.maximum(inf, 1e-300)), 0.0)
    member = np.stack([((idx >> i) & 1) for i in range(n)], 0).astype(float)  # n x N
    sumlog = linf @ member                                                    # nf x N
    kk = np.where(k > 0, k, 1.0)
    K = (W * sumlog / kk)[:, k > 0].sum(1)
    R = H - K
    res = {}
    r = np.where(nonconst, H / np.where(nonconst, I, 1), 0)
    res['max H/I bits'] = (r.max() / LN2, int(r.argmax()))
    rk = np.where(nonconst, K / np.where(nonconst, I, 1), 0)
    rr = np.where(nonconst, R / np.where(nonconst, I, 1), 0)
    res['max K/I nats'] = (rk.max(), int(rk.argmax()))
    res['max R/I nats'] = (rr.max(), int(rr.argmax()))
    # terminal entropy of the normalized tilt: normalized lowest nonempty-weight level
    kmin = np.where(pos, k[None, :], 99).min(1)
    Hinf = np.zeros(nf)
    for kv in range(n + 1):
        sel = (kmin == kv)
        if not sel.any():
            continue
        Wl = W[sel][:, k == kv]
        p = Wl / Wl.sum(1, keepdims=True)
        with np.errstate(divide='ignore', invalid='ignore'):
            Hinf[sel] = -(np.where(p > 0, p * np.log(p), 0)).sum(1)
    rh = np.where(nonconst, Hinf / np.where(nonconst, I, 1), 0)
    res['max H(q_inf)/I nats'] = (rh.max(), int(rh.argmax()))
    # tilt scans
    best_E = np.zeros(nf); best_E_t = np.zeros(nf)
    best_V = np.zeros(nf)
    min_flux = np.zeros(nf)
    best_P = np.zeros(nf)   # G / (M + Kr + N)
    for t in tgrid:
        u = W * np.exp(-2 * t * k)[None, :]
        Z = u.sum(1, keepdims=True)
        q = u / Z
        Ek = (q * k).sum(1)
        Vk = (q * (k - Ek[:, None]) ** 2).sum(1)
        mlq = np.where(q > 0, L + 2 * t * k + np.log(Z), 0.0)
        Em = (q * mlq).sum(1)
        flux = 2 * (q * (k - Ek[:, None]) * (mlq - Em[:, None])).sum(1)
        ok = nonconst & (Ek > 1e-12)
        ratioE = np.where(ok, flux / np.where(ok, Ek, 1), 0)
        upd = ratioE > best_E
        best_E = np.where(upd, ratioE, best_E); best_E_t = np.where(upd, t, best_E_t)
        okv = nonconst & (Vk > 1e-9)
        ratioV = np.where(okv, flux / np.where(okv, Vk, 1), 0)
        best_V = np.maximum(best_V, ratioV)
        min_flux = np.minimum(min_flux, flux)
        # unnormalized pointwise test
        G = (u * k * L).sum(1); M = (u * k * k).sum(1); Nn = (u * k).sum(1); Kr = (u * sumlog).sum(1)
        den = M + Kr + Nn
        okp = nonconst & (den > 1e-300)
        best_P = np.maximum(best_P, np.where(okp, G / np.where(okp, den, 1), 0))
    res['sup_t (-dH/dt)/E_t'] = (best_E.max(), int(best_E.argmax()), float(best_E_t[best_E.argmax()]))
    res['sup_t (-dH/dt)/Var_t'] = (best_V.max(), int(best_V.argmax()))
    res['min_t -dH/dt'] = (min_flux.min(), int(min_flux.argmin()))
    res['sup_t G/(M+Kr+N)'] = (best_P.max(), int(best_P.argmax()))
    res['count nonconst'] = int(nonconst.sum())
    return res, W, H, I


def gauged_identity_check(W, H, rows, n, tmax=40.0, steps=40000):
    """H - H_inf = 2 int_0^inf Cov_{q_t^U}(|S xor U|, L) dt, U = argmax w."""
    N = 1 << n
    idx = np.arange(N)
    out = []
    ts = np.linspace(0, tmax, steps + 1)
    for r in rows:
        w = W[r]
        U = int(w.argmax())
        d = popcounts(n)[idx ^ U].astype(float)
        pos = w > 0
        L = np.zeros(N); L[pos] = -np.log(w[pos])
        vals = []
        for t in ts:
            u = w * np.exp(-2 * t * d); q = u / u.sum()
            Ed = (q * d).sum(); EL = (q * L).sum()
            vals.append(2 * (q * (d - Ed) * (L - EL)).sum())
        integ = np.trapezoid(vals, ts)
        out.append((r, H[r] - (-math.log(w.max())), integ))
    return out


def main():
    lines = []
    P = lambda *a: lines.append(' '.join(str(x) for x in a))
    tgrid = np.concatenate([np.linspace(0, 2, 81), np.linspace(2.1, 12, 100)])
    for n in [2, 3, 4]:
        res, W, H, I = run(n, tgrid)
        P(f"## n = {n}")
        for key, v in res.items():
            P(key, v)
        rng = np.random.default_rng(1)
        rows = rng.choice(W.shape[0], 6, replace=False)
        for r, lhs, rhs in gauged_identity_check(W, H, rows, n):
            P("gauged identity f=%d  H-H_inf=%.12f  2*int Cov=%.12f" % (r, lhs, rhs))
    txt = '\n'.join(lines)
    print(txt)
    with open('../logs/exhaust_n4.log', 'w') as fh:
        fh.write(txt + '\n')


if __name__ == '__main__':
    main()
