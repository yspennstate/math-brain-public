"""Independent check of agent's tower value W(1/2)=6.521845711 for the PM(K33) gate.
F(b) = -1 iff the edge set {e : b_e = 1} of K_{3,3} contains a perfect matching (and the complement orientation).
p-biased Fourier by brute force: phi(b) = (b - p)/sqrt(p(1-p)), Pr[b=1] = p."""
import itertools, math
import numpy as np

edges = [(i, j) for i in range(3) for j in range(3)]
perms = list(itertools.permutations(range(3)))
N = 1 << 9
bits = np.array([[(x >> e) & 1 for e in range(9)] for x in range(N)], dtype=float)
pm = np.array([any(all((x >> (3 * i + s[i])) & 1 for i in range(3)) for s in perms) for x in range(N)])
Fpm = np.where(pm, -1.0, 1.0)
sizes = bits.sum(1)

def stats(F, p):
    s = math.sqrt(p * (1 - p))
    w = np.prod(np.where(bits == 1, p, 1 - p), axis=1)          # Pr of each point
    phi = (bits - p) / s                                         # (N, 9)
    # character chi_S(x) = prod_{e in S} phi_e(x); S indexed by subset mask = rows of bits
    chi = np.ones((N, N))
    for e in range(9):
        chi *= np.where(bits[:, e][:, None] == 1, phi[:, e][None, :], 1.0).T if False else 1.0
    # build chi[x, S] directly
    chi = np.prod(np.where(bits[None, :, :] == 1, phi[:, None, :], 1.0), axis=2)   # (x, S)
    coef = (w * F) @ chi                                         # fhat_p(S)
    mean = coef[0]
    var = 1 - mean ** 2
    q = coef[1:] ** 2 / var
    q = q[q > 0]
    G = float(-(q * np.log2(q)).sum())
    J = float((coef[1:] ** 2 * sizes[1:]).sum() / var)
    pnew = float(w[F < 0].sum())
    return pnew, G, J, float((coef ** 2).sum())

for name, F in [("PM=-1", Fpm), ("PM=+1", -Fpm)]:
    p, G, J = 0.5, 0.0, 1.0
    out = []
    for step in range(80):
        pn, g, j, parseval = stats(F, p)
        G, J = g + j * G, j * J
        out.append((step, p, g, j, G / J, parseval))
        p = pn
        if J > 1e300:
            break
    print(name)
    for r in out[:6] + out[-3:]:
        print("  step %2d p=%.9f G_p=%.6f J_p=%.6f G/J=%.9f parseval=%.12f" % r)
