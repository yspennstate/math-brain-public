"""T362 (agent A, 18 Oct 2026): exact last iterate of random reshuffling on a 1-D sum with DIFFERENT component curvatures
(the non-commuting-weights case the commuting instance in rr_exact.py cannot see). n1 components f = (L/2) x^2 - s x and n2 = n - n1
components f = (l/2) x^2 + s (n1/n2) x, so x* = 0, F''= mu = (n1 L + n2 l)/n, kappa = L/mu, G* = s, sigma*^2 = s^2 n1/n2.
One epoch is X -> A X + B with (A, B) a function of the type order (uniform over C(n, n1) orders). A DP over (step, #stiff used) gives
E A, E B, E A^2, E AB, E B^2 exactly; epochs are independent, so E X_K, E X_K^2 follow by recursion. Prints, per kappa, the
optimal-step last-iterate error E F(x_K) - F* against K, and its slope; mode mc checks the DP against simulated RR."""
import sys, numpy as np
from math import comb, lgamma, exp
def epoch_moments(g, n, n1, L, l, s):
    n2 = n - n1; aL, al = 1 - g * L, 1 - g * l; cL, cl = g * s, -g * s * n1 / n2
    # arrays over j = # stiff used; store sums over orders of A, B, A2, AB, B2, normalised by number of orders reaching (k, j)
    # use probabilities: P(next is stiff | k, j) = (n1 - j)/(n - k)
    A = {0: 1.0}; B = {0: 0.0}; A2 = {0: 1.0}; AB = {0: 0.0}; B2 = {0: 0.0}; P = {0: 1.0}
    for k in range(n):
        nA, nB, nA2, nAB, nB2, nP = {}, {}, {}, {}, {}, {}
        for j, p in P.items():
            if p == 0: continue
            ps = (n1 - j) / (n - k)
            for t, q in ((1, ps), (0, 1 - ps)):
                if q <= 0: continue
                a, c = (aL, cL) if t else (al, cl); jj = j + t; w = p * q
                # conditional moments at (k, j) are A[j] etc.; propagate weighted sums then renormalise
                nP[jj] = nP.get(jj, 0) + w
                nA[jj] = nA.get(jj, 0) + w * a * A[j]; nB[jj] = nB.get(jj, 0) + w * (a * B[j] + c)
                nA2[jj] = nA2.get(jj, 0) + w * a * a * A2[j]; nAB[jj] = nAB.get(jj, 0) + w * (a * a * AB[j] + c * a * A[j])
                nB2[jj] = nB2.get(jj, 0) + w * (a * a * B2[j] + 2 * a * c * B[j] + c * c)
        P = nP; A = {j: nA[j] / P[j] for j in P}; B = {j: nB[j] / P[j] for j in P}; A2 = {j: nA2[j] / P[j] for j in P}
        AB = {j: nAB[j] / P[j] for j in P}; B2 = {j: nB2[j] / P[j] for j in P}
    return A[n1], B[n1], A2[n1], AB[n1], B2[n1]
def epoch_moments_vec(gs, n, n1, L, l, s):
    """same DP, numpy over (step grid, #stiff used); returns arrays EA, EB, EA2, EAB, EB2 over gs."""
    gs = np.asarray(gs)[:, None]; n2 = n - n1; aL, al = 1 - gs * L, 1 - gs * l; cL, cl = gs * s, -gs * s * n1 / n2
    J = n1 + 1; G = gs.shape[0]; P = np.zeros((1, J)); P[0, 0] = 1.0
    A = np.zeros((G, J)); A[:, 0] = 1; B = np.zeros((G, J)); A2 = A.copy(); AB = np.zeros((G, J)); B2 = np.zeros((G, J))
    j = np.arange(J)
    for k in range(n):
        ps = np.clip((n1 - j) / (n - k), 0, 1)[None, :]; wS = P * ps; wF = P * (1 - ps)   # weights to go stiff (j -> j+1) / flat (j -> j)
        def sh(X): Y = np.zeros_like(X); Y[:, 1:] = X[:, :-1]; return Y
        nP = sh(wS) + wF
        nA = sh(wS * aL * A) + wF * al * A; nB = sh(wS * (aL * B + cL)) + wF * (al * B + cl)
        nA2 = sh(wS * aL * aL * A2) + wF * al * al * A2; nAB = sh(wS * (aL * aL * AB + cL * aL * A)) + wF * (al * al * AB + cl * al * A)
        nB2 = sh(wS * (aL * aL * B2 + 2 * aL * cL * B + cL * cL)) + wF * (al * al * B2 + 2 * al * cl * B + cl * cl)
        d = np.where(nP > 0, nP, 1.0); P = nP; A, B, A2, AB, B2 = nA / d, nB / d, nA2 / d, nAB / d, nB2 / d
    return A[:, n1], B[:, n1], A2[:, n1], AB[:, n1], B2[:, n1]
def err(g, n, n1, L, l, s, K, X0=1.0):
    mu = (n1 * L + (n - n1) * l) / n; EA, EB, EA2, EAB, EB2 = epoch_moments(g, n, n1, L, l, s); m1, m2 = X0, X0 * X0
    for _ in range(K): m1, m2 = EA * m1 + EB, EA2 * m2 + 2 * EAB * m1 + EB2
    return 0.5 * mu * m2
def err_from(mom, mu, K, X0=1.0):
    EA, EB, EA2, EAB, EB2 = mom; m1, m2 = X0, X0 * X0
    for _ in range(K): m1, m2 = EA * m1 + EB, EA2 * m2 + 2 * EAB * m1 + EB2
    return 0.5 * mu * m2
def best_all(n, n1, L, l, s, Ks):
    """epoch moments do not depend on K: compute them once on a log grid of steps (fine, 3 per percent), reuse for every K."""
    mu = (n1 * L + (n - n1) * l) / n; gs = np.exp(np.linspace(np.log(1e-6), np.log(1.99 / L), 900))
    V = epoch_moments_vec(gs, n, n1, L, l, s); moms = list(zip(*V))
    out = []
    for K in Ks:
        e = [err_from(m, mu, K) for m in moms]; i = int(np.argmin(e)); out.append((K, e[i], gs[i]))
    return out
if sys.argv[1] == 'mc':
    rng = np.random.default_rng(3620)
    for (n, n1, L, l, s, K, g) in ((6, 2, 1.0, 0.1, 1.0, 4, 0.3), (10, 1, 1.0, 0.0, 1.0, 6, 0.5), (8, 3, 2.0, 0.5, 0.7, 3, 0.2)):
        n2 = n - n1; h = np.array([L] * n1 + [l] * n2); c = np.array([s] * n1 + [-s * n1 / n2] * n2); R = 400000; X = np.ones(R)
        for k in range(K):
            Pm = np.argsort(rng.random((R, n)), axis=1)
            for j in range(n): X = X - g * (h[Pm[:, j]] * X - c[Pm[:, j]])
        mu = (n1 * L + n2 * l) / n; mc = 0.5 * mu * X ** 2
        ev = err_from([v[0] for v in epoch_moments_vec([g], n, n1, L, l, s)], (n1 * L + n2 * l) / n, K)
        print(f'n {n} n1 {n1} L {L} l {l} K {K} g {g}: exact {err(g, n, n1, L, l, s, K):.6e} vec {ev:.6e} MC {mc.mean():.6e} +- {mc.std() / np.sqrt(R):.1e}', flush=True)
else:
    L = 1.0; s = 1.0
    for kap in [int(v) for v in sys.argv[3].split(',')]:
        for n in [int(v) for v in sys.argv[2].split(',')]:
            n1 = n // kap; l = 0.0
            if n1 < 1 or n1 >= n: continue
            mu = n1 * L / n; row = best_all(n, n1, L, l, s, (1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000))
            sl = [np.log(row[i + 1][1] / row[i][1]) / np.log(row[i + 1][0] / row[i][0]) for i in range(len(row) - 1)]
            print(f'kappa {L / mu:.0f} n {n} n1 {n1} G* {s} sigma*^2 {s * s * n1 / (n - n1):.3g}: ' + ' '.join(f'K{K}:{e:.3e}(gL {g * L:.2g})' for K, e, g in row), flush=True)
            print('      slopes: ' + ' '.join(f'{v:+.2f}' for v in sl), flush=True)
