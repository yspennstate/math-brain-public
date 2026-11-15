"""Check E_{(j,i)}(F o psi) = Inf_j(F) E_i(psi) + sum_{T not j} Phi(Fhat(T)^2, Fhat(T+j)^2 psihat(i)^2)
and Inf_{(j,i)} = Inf_j(F) Inf_i(psi), psi balanced, disjoint copies. Then Q_b(Maj_m o psi) vs G(psi)."""
import numpy as np, itertools, sys


def wht_rows(T):
    T = T.astype(float).copy(); N = T.shape[1]; h = 1
    while h < N:
        T = T.reshape(T.shape[0], -1, 2 * h)
        a = T[:, :, :h].copy(); b = T[:, :, h:].copy()
        T[:, :, :h] = a + b; T[:, :, h:] = a - b
        T = T.reshape(T.shape[0], N); h *= 2
    return T / N


def EI(F, n):
    w2 = F ** 2; idx = np.arange(1 << n); E = []; I = []
    for i in range(n):
        bit = 1 << i; T = idx[(idx & bit) == 0]
        a = w2[:, T]; c = w2[:, T | bit]; s = a + c
        t = np.divide(c, s, out=np.zeros_like(s), where=s > 1e-300)
        with np.errstate(divide="ignore", invalid="ignore"):
            H = -(t * np.log2(np.where(t > 0, t, 1)) + (1 - t) * np.log2(np.where(t < 1, 1 - t, 1)))
        E.append((s * H).sum(1)); I.append(c.sum(1))
    return np.array(E).T, np.array(I).T


def Q(E, I, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(I > 1e-15, (1 + np.log2(1 / np.where(I > 1e-15, I, 1))) ** (-b), 0.0)
    num = (g * E).sum(1); den = (g * I).sum(1)
    return np.where(den > 1e-12, num / np.where(den > 1e-12, den, 1), 0.0)



def table(fn, n):
    return np.array([fn([1 - 2 * ((x >> k) & 1) for k in range(n)]) for x in range(1 << n)], float)


def Phi(a, c):
    s = a + c
    if s <= 0 or c <= 0 or a <= 0:
        return 0.0
    t = c / s
    return s * -(t * np.log2(t) + (1 - t) * np.log2(1 - t))


def compose(Ftab, m, ptab, n):
    N = 1 << (m * n); out = np.empty(N)
    for x in range(N):
        ys = 0
        for j in range(m):
            blk = (x >> (j * n)) & ((1 << n) - 1)
            if ptab[blk] < 0:
                ys |= 1 << j
        out[x] = Ftab[ys]
    return out


maj = lambda m: (lambda v: 1.0 if sum(v) > 0 else -1.0)
psis = {"and2xor": (3, lambda v: (1.0 if (v[0] == -1 and v[1] == -1) else -1.0) * v[2]),
        "maj3": (3, lambda v: 1.0 if sum(v) > 0 else -1.0),
        "sel": (3, lambda v: v[1] if v[0] == 1 else v[2])}
for name, (n, fn) in psis.items():
    p = table(fn, n); assert abs(p.mean()) < 1e-12
    ph = wht_rows(p[None])[0]; Ep, Ip = EI(ph[None], n); Ep, Ip = Ep[0], Ip[0]
    G = Ep.sum() / Ip.sum()
    for m in (3, 5):
        Ft = table(maj(m), m); Fh = wht_rows(Ft[None])[0]; EF, IF = EI(Fh[None], m)
        c = compose(Ft, m, p, n); ch = wht_rows(c[None])[0]
        Ec, Ic = EI(ch[None], m * n); Ec, Ic = Ec[0], Ic[0]
        err = 0.0
        for j in range(m):
            for i in range(n):
                k = j * n + i
                T = sum(Phi(Fh[S] ** 2, Fh[S | (1 << j)] ** 2 * ph[1 << i] ** 2)
                        for S in range(1 << m) if not (S >> j) & 1)
                pred = IF[0][j] * Ep[i] + T
                err = max(err, abs(Ec[k] - pred), abs(Ic[k] - IF[0][j] * Ip[i]))
        print(f"{name} m={m}: max|err|={err:.2e} G(psi)={G:.4f} Q0={Q(Ec[None], Ic[None], 0)[0]:.4f} "
              f"Q1={Q(Ec[None], Ic[None], 1)[0]:.4f} Q1(psi)={Q(Ep[None], Ip[None], 1)[0]:.4f}")
