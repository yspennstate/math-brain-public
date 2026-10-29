# T352 (agent B, 19 Oct 2026). The T -> infinity value of Chien-Li's Renyi bound (arXiv:2410.01068 v2, Thm 3.7,
# full batch, (L, lam)-Holder gradient), as a function of n. Their bound:
#   eps(alpha) <= min alpha/(2 s^2) sum_{t=tau}^{T-1} [ (2 eta K/n)^2 / beta_t + a_t^2 / (1 - beta_t) ]
#   s.t. A_T = 0, A_{t-1} = h(A_t + a_{t-1}), A_tau >= D_tau,  h = g^{-1}, g(x) = x + eta L x^lam,
#        D_t = min(g(D_{t-1}) + 2 eta K/n, D_{t-1} + 2 eta K, D).
# For T -> infinity D_tau = D (the cap) for every tau that keeps the sum finite. Minimising over beta_t gives the
# per-step cost (c + a_t)^2 with c = 2 eta K / n. So eps_inf = alpha/(2 s^2) * min over paths 0 -> D of sum (c + a)^2,
# where a step goes A -> A' with a = g(A') - A >= 0 (the backward recursion read forward in k = T - t).
# lam = 1: A_tau = sum_j r^j a_j, r = 1/(1 + eta L), so sum a^2 >= D^2 / sum r^{2j} > D^2 (2 eta L + eta^2 L^2) for EVERY n:
# the bound has an n-free floor alpha D^2 (2 eta L + eta^2 L^2) / (2 s^2). lam < 1: Dijkstra on a grid of A.
import sys, json, numpy as np

def lam1(c, eL, D, Nmax=200000):
    r = 1 / (1 + eL); best = np.inf; bestN = None
    for N in np.unique(np.geomspace(1, Nmax, 400).astype(int)):
        w = r ** np.arange(1, N + 1)
        # KKT: a_j = max(0, mu w_j - c), choose mu so that sum w_j a_j = D (bisection)
        lo, hi = 0.0, (D + c * w.sum()) / (w * w).sum() * 4 + c / w.min()
        for _ in range(200):
            mu = (lo + hi) / 2; a = np.maximum(0, mu * w - c)
            if (w * a).sum() >= D: hi = mu
            else: lo = mu
        a = np.maximum(0, hi * w - c); cost = ((c + a) ** 2).sum()
        if cost < best: best, bestN = cost, int(N)
    return best, bestN

def dijkstra(c, eL, lam, D, M=1500):
    A = np.linspace(0, D, M); gA = A + eL * A ** lam
    dist = np.full(M, np.inf); dist[0] = 0; done = np.zeros(M, bool)
    for _ in range(M):
        i = np.argmin(np.where(done, np.inf, dist)); done[i] = True
        if i == M - 1: break
        a = gA - A[i]; ok = (a >= 0) & ~done
        nd = dist[i] + (c + np.where(ok, a, 0)) ** 2
        upd = ok & (nd < dist); dist[upd] = nd[upd]
    return dist[-1]

if __name__ == "__main__":
    eta, L, K, D = 0.01, 1.0, 1.0, 1.0       # eps_inf in units of alpha/(2 s^2)
    out = []
    for n in [10, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6]:
        c = 2 * eta * K / n
        v1, N1 = lam1(c, eta * L, D); vh = dijkstra(c, eta * L, 0.5, D)
        cvx = 2 * c * D        # convex analogue (no shrink): min_N N c^2 + D^2/N + 2cD -> 4 c D (Altschuler-Talwar scale)
        out.append(dict(n=n, lam1=v1, lam1_N=N1, lam_half=vh, convex_scale=4 * c * D))
        print("n %7d  lam=1: %.5e (N %6d)   lam=1/2: %.5e   convex scale 4cD: %.3e" % (n, v1, N1, vh, 4 * c * D), flush=True)
    print("lam=1 floor D^2(2 eta L + eta^2 L^2) = %.5e ; lam=1/2 continuum guess ~ eta L D^{3/2} * const" % (D * D * (2 * eta * L + (eta * L) ** 2)))
    json.dump(out, open("cl_floor.json", "w"), indent=1)
