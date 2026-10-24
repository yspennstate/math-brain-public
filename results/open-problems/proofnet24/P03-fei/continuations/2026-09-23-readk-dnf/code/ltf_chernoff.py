# For linear threshold events A = {w.y >= theta} under product measures: compare
#   alpha TC(mu_A)  <=  alpha ln(chi*/alpha)   (chi* = min_lambda E exp(lambda (S - theta)), the Chernoff bound)
# with I = sum_i sigma_i^2 mu(i pivotal).  Reports the worst ratios alpha TC / I and alpha ln(chi*/alpha) / I.
import numpy as np, random, sys, math
from scipy.optimize import minimize_scalar

def analyse(w, q, theta):
    n = len(w)
    X = ((np.arange(1 << n)[:, None] >> np.arange(n)) & 1).astype(float)
    p = np.prod(np.where(X == 1, q, 1 - q), axis=1)
    S = X @ w
    A = S >= theta - 1e-12
    alpha = p[A].sum()
    if alpha <= 0 or alpha >= 1: return None
    flip = False
    if alpha > 0.5:                       # use the smaller side: complement is {-w.y > -theta}
        flip = True
    if flip:
        A = ~A; alpha = 1 - alpha; Ssgn = -S; th = -theta
    else:
        Ssgn = S; th = theta
    # influences
    I = 0.0
    for i in range(n):
        Xi1 = X.copy(); Xi1[:, i] = 1; Xi0 = X.copy(); Xi0[:, i] = 0
        piv = ((Xi1 @ w) >= theta - 1e-12) != ((Xi0 @ w) >= theta - 1e-12)
        I += 4 * q[i] * (1 - q[i]) * p[piv].sum()
    # TC of mu_A
    pa = p[A] / alpha
    H = -(pa * np.log(pa)).sum()
    marg = (X[A] * pa[:, None]).sum(axis=0)
    Hm = sum(-(m * math.log(m) + (1 - m) * math.log(1 - m)) for m in marg if 0 < m < 1)
    tc = Hm - H
    # Chernoff for the event {Ssgn >= th} (on the chosen side)
    ww = -w if flip else w
    def logchi(lam):
        return np.sum(np.log(1 - q + q * np.exp(lam * ww))) - lam * th
    res = minimize_scalar(logchi, bounds=(0, 200), method='bounded')
    lc = min(res.fun, 0.0)
    return alpha * tc / I, alpha * (lc - math.log(alpha)) / I, alpha

rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
worst = {'tc': (0, None), 'chern': (0, None)}
for trial in range(T):
    n = rng.randint(2, nmax)
    kind = rng.random()
    if kind < 0.3:
        w = np.array([rng.randint(1, 3) for _ in range(n)], float)
    elif kind < 0.6:
        w = np.array([2.0 ** rng.randint(0, 6) for _ in range(n)])
    else:
        w = np.array([rng.expovariate(1.0) + 0.01 for _ in range(n)])
    q = np.array([min(max(10 ** -rng.uniform(0, 8) if rng.random() < 0.4 else rng.uniform(0.02, 0.98), 1e-9), 1 - 1e-9) for _ in range(n)])
    if rng.random() < 0.3: q = 1 - q
    theta = rng.uniform(0, w.sum())
    o = analyse(w, q, theta)
    if o is None: continue
    if o[0] > worst['tc'][0]: worst['tc'] = (o[0], (list(np.round(w, 3)), list(q), theta, o[2]))
    if o[1] > worst['chern'][0]: worst['chern'] = (o[1], (list(np.round(w, 3)), list(q), theta, o[2]))
    if trial % 500 == 0: print(trial, round(worst['tc'][0], 4), round(worst['chern'][0], 4), flush=True)
print('WORST alpha TC / I', worst['tc'])
print('WORST alpha ln(chi*/alpha) / I', worst['chern'])
