# Key lemma test: alpha * TC(x | f=1) <= C * I_mu(f), where TC = sum_i H(x_i|A) - H(x|A), alpha = mu(A) <= 1/2
# (if alpha > 1/2 use the complement, which has the same I and Var).  Float64 with log-weights; entropies computed
# from normalized conditional weights, so no cancellation.
import numpy as np, math, random, sys
def tc_ratio(fv, q):
    n = len(q); N = 1 << n
    X = ((np.arange(N)[:, None] >> np.arange(n)) & 1).astype(np.int8)
    lw = np.where(X == 1, np.log(q), np.log1p(-q)).sum(axis=1)
    fv = np.asarray(fv, bool)
    a1 = np.exp(lw[fv]).sum(); a0 = np.exp(lw[~fv]).sum()
    A = fv if a1 <= a0 else ~fv
    lwA = lw[A]; m = lwA.max(); wA = np.exp(lwA - m); alpha = wA.sum() * math.exp(m)
    pA = wA / wA.sum()
    H = -(pA * np.log(np.where(pA > 0, pA, 1))).sum()
    marg = (pA[:, None] * X[A]).sum(axis=0)
    Hm = sum(-(v * math.log(v) + (1 - v) * math.log(1 - v)) for v in marg if 0 < v < 1)
    TC = Hm - H
    sig2 = 4 * q * (1 - q); I = 0.0
    for i in range(n):
        m0 = X[:, i] == 0
        idx0 = np.nonzero(m0)[0]; idx1 = idx0 | (1 << i)
        piv = fv[idx0] != fv[idx1]
        rho = np.exp(lw[idx0][piv] - math.log1p(-q[i])).sum()
        I += sig2[i] * rho
    return alpha * TC / I, TC, alpha, I
def ltf(n, rng):
    mode = rng.random()
    if mode < 0.35: w = [1.0] * n
    elif mode < 0.7: w = [float(rng.randint(1, 6)) for _ in range(n)]
    else: w = [rng.expovariate(1.0) for _ in range(n)]
    th = rng.uniform(0.01, sum(w))
    return [1 if sum(w[i] for i in range(n) if x >> i & 1) >= th else 0 for x in range(1 << n)], w, th
if __name__ == '__main__':
    print('tribes (OR of N pairs), q = 1/N^2 (expect growth):')
    for N in [2, 3, 4, 5, 6, 7]:
        n = 2 * N
        f = [1 if any((x >> (2 * j)) & 1 and (x >> (2 * j + 1)) & 1 for j in range(N)) else 0 for x in range(1 << n)]
        r = tc_ratio(f, np.array([1.0 / N ** 2] * n)); print(N, 'ratio %.4f TC %.4f' % (r[0], r[1]))
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nlo, nhi = int(sys.argv[3]), int(sys.argv[4])
    best = (-1, None)
    for t in range(T):
        n = rng.randint(nlo, nhi)
        f, w, th = ltf(n, rng)
        if len(set(f)) < 2: continue
        q = []
        for _ in range(n):
            u = rng.random()
            q.append(10 ** -rng.uniform(0, 12) if u < 0.35 else (1 - 10 ** -rng.uniform(0, 12) if u < 0.6 else rng.uniform(0.01, 0.99)))
        q = np.clip(np.array(q), 1e-13, 1 - 1e-13)
        r = tc_ratio(f, q)
        if r[0] > best[0]:
            best = (r[0], n, [round(x, 3) for x in w], round(th, 3), [float('%.3g' % x) for x in q], r[1], r[2], r[3])
            print(t, 'best alpha*TC/I = %.4f' % r[0], best[1:], flush=True)
    print('DONE', best[0])
