# Referee check (agent C, 18 Oct): the T362 bias-side lower bound over EVERY step 0 < gL <= 1, not only gL n1 <= 1/2.
# Exact E X_K = A^K X0 + (1 - A^K) m, m = (g s/2) phi(r), A = r^n1 (dossier 15:15); E F - F* >= (mu/2) (E X_K)^2.
import math
def phi(r, n1):
    S = sum(r**k for k in range(n1))
    return 2 * sum((k + 1) * r**k for k in range(n1)) / ((n1 + 1) * S)
def run(n, n1, K, X0=1.0, L=1.0, s=1.0, ngrid=4000):
    mu, T = L * n1 / n, n * K
    Lam = math.log(X0 * mu * T / s)
    bound = s**2 * (Lam - math.log(Lam))**2 / (512 * mu * T**2)
    unit = s**2 * Lam**2 / (8 * mu * T**2)
    best, gbest, worst_ratio_far = 1e300, None, 1e300
    for j in range(1, ngrid + 1):
        g = (j / ngrid) / L          # 0 < gL <= 1, linear grid
        for g in (g, (1 / L) * 10 ** (-6 * (1 - j / ngrid))):   # plus a log grid down to gL = 1e-6
            r = 1 - g * L
            A = r ** n1
            m = g * s / 2 * phi(r, n1)
            EX = A ** K * X0 + (1 - A ** K) * m
            err = mu / 2 * EX * EX
            if err < best: best, gbest = err, g
            if g * L * n1 > 0.5: worst_ratio_far = min(worst_ratio_far, err / bound)
    return dict(n=n, n1=n1, K=K, need_K=round(n1 * (Lam - math.log(Lam)) / 2, 1), min_over_bound=best / bound,
                min_over_unit=best / unit, gmuT_over_Lam=gbest * mu * T / Lam, large_step_min_over_bound=worst_ratio_far)
for n, n1, K in ((100, 10, 10**3), (100, 10, 10**4), (100, 50, 10**3), (100, 50, 10**4), (1000, 100, 10**3), (1000, 100, 10**4),
                 (40, 3, 10**3), (100, 50, 200), (1000, 100, 300)):
    print(run(n, n1, K))
