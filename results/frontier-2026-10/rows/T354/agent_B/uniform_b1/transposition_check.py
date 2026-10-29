# T354: check of the transposition bound behind "uniform in beta1" (agent B, 20 Oct 2026). One epoch, all n! orders,
# plus an independent two-point rest R (the other epochs). T = sum_q w_q E[b_pi(q) F(eta)], F = psi(1+eta) - 1 - p1 eta, against
# (i) the exact identity T = (1/4n) sum_{q,r} (w_q-w_r) E[(b_pi(q)-b_pi(r)) (F(pi) - F(pi o tau_qr))], and (ii) the claimed bound
# |T| <= C d S, S = (1/n) sum_{q,r} (w_q-w_r)(a_q-a_r) >= 0, with C free of beta1 and n. Argv: eps.
import itertools, math, sys
import numpy as np
eps = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
def run(bvals, x, d, b1, eps):
    n = len(bvals); b = np.array(bvals, float); b -= b.mean()
    g2 = (x + b) ** 2; V = g2.mean(); Z = g2 - V; s = math.sqrt(V)
    psi = lambda y: (s + eps) / (s * np.sqrt(y) + eps)
    h = 1e-6; p1 = (psi(1 + h) - psi(1 - h)) / (2 * h)
    b2 = 1 - d; a = (d / V) * b2 ** np.arange(n); w = (1 - b1) * b1 ** np.arange(n)
    r0 = 0.3 * math.sqrt(d)
    F = lambda e: psi(1 + e) - 1 - p1 * e
    perms = np.array(list(itertools.permutations(range(n))))
    eta = (a[None, :] * Z[perms]).sum(1)
    T = 0.0; I = 0.0
    for R in (-r0, r0):
        Fe = F(eta + R)
        T += 0.5 * (w[None, :] * b[perms] * Fe[:, None]).sum(1).mean()
        for q in range(n):
            for r in range(n):
                if q == r: continue
                etat = eta + (a[q] - a[r]) * (Z[perms[:, r]] - Z[perms[:, q]])
                I += 0.5 * (w[q] - w[r]) * ((b[perms[:, q]] - b[perms[:, r]]) * (Fe - F(etat + R))).mean() / (4 * n)
    S = ((w[:, None] - w[None, :]) * (a[:, None] - a[None, :])).sum() / n
    return T, I, S
for bv in ([3, -1, -1, -1, 1, -1], [2, -1, 0.5, -1.5, 0, 0], [4, -1, -1, -1, -1]):
    for d in (0.1, 0.01, 0.001):
        for b1 in (0.0, 0.9, 0.99, 0.999, 0.9999):
            T, I, S = run(bv, 0.05, d, b1, eps)
            print("b %s d %g beta1 %g  T %.4e  identity %.4e  rel.err %.1e  S %.3e  T/(d S) %.4f"
                  % (bv, d, b1, T, I, abs(T - I) / max(abs(T), 1e-300), S, T / (d * S)), flush=True)
