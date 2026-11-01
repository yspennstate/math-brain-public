# Exact checks (mpmath, 50 digits) for symmetric thresholds Thr_{t,n} under the i.i.d. measure mu_p, all nats.
#  level weights: W_k = C(n,k) (pq)^k (E_{c~Bin(n-k,p)} Delta^k G(c))^2,  G(c) = 1 - 2*[c >= t]
#  LHS+ = sum_{k>=1} W_k ln(C(n,k) sig^{2k} / W_k),  I = sum k W_k, V = sum_{k>=1} W_k, J = sum_{k>=2} k W_k
#  L1  G-bound:   4 n G <= I (1 + ln(1 + rho/alpha))            (G = alpha * D(Bern(p_hat) || Bern(p)))
#  L2  TC-lemma:  alpha * TC <= 0.736 I                          (TC = D(Law(K|A) || Bin(n, p_hat)))
#  L3  rank tail: sum_k k W_k ln+(Lam/k) <= 4.844 I              (Lam = n sig^2)
#  L4  credit:    V ln(1/V) <= I ln+(4 rho / V) + 5.637 I
#  T   theorem:   LHS+ <= 12.48 I;   and for 2 <= t <= n-1: rho <= 1/2, J >= I/2
import mpmath as mp, sys, random
mp.mp.dps = 50
def binpmf(m, p, j):
    if j < 0 or j > m: return mp.mpf(0)
    return mp.binomial(m, j) * p ** j * (1 - p) ** (m - j)
def check(n, t, p):
    p = mp.mpf(p); q = 1 - p; s2 = 4 * p * q; Lam = n * s2
    G = lambda c: 1 - 2 * (1 if c >= t else 0)
    W = []
    for k in range(n + 1):
        E = mp.fsum(binpmf(n - k, p, c) * mp.fsum((-1) ** (k - j) * mp.binomial(k, j) * G(c + j) for j in range(k + 1)) for c in range(n - k + 1))
        W.append(mp.binomial(n, k) * (p * q) ** k * E ** 2)
    V = mp.fsum(W[1:]); I = mp.fsum(k * W[k] for k in range(1, n + 1)); J = mp.fsum(k * W[k] for k in range(2, n + 1))
    lhs = mp.fsum(W[k] * mp.log(mp.binomial(n, k) * s2 ** k / W[k]) for k in range(1, n + 1) if W[k] > 0)
    up = mp.fsum(binpmf(n, p, c) for c in range(t, n + 1)); lo = mp.fsum(binpmf(n, p, c) for c in range(0, t))
    # smaller side A, as an up-set in the (possibly flipped) coordinates
    if up <= lo: alpha, pp, tt = up, p, t
    else: alpha, pp, tt = lo, q, n - t + 1
    rho = binpmf(n - 1, p, t - 1)
    out = {}
    # L1 / L2: exact conditional law of K on A = {K' >= tt} with K' ~ Bin(n, pp)
    lawK = {k: binpmf(n, pp, k) / alpha for k in range(tt, n + 1)}
    phat = mp.fsum(k * v for k, v in lawK.items()) / n
    Dm = phat * mp.log(phat / pp) + ((1 - phat) * mp.log((1 - phat) / (1 - pp)) if phat < 1 else 0)
    TC = mp.fsum(v * mp.log(v / binpmf(n, phat, k)) for k, v in lawK.items() if v > 0) if 0 < phat < 1 else mp.mpf(0)
    out['L1'] = float(4 * n * alpha * Dm / (I * (1 + mp.log(1 + rho / alpha))))
    out['L2'] = float(alpha * TC / I)
    out['chain'] = float(abs(alpha * mp.log(1 / alpha) - (n * alpha * Dm + alpha * TC)) / (alpha * mp.log(1 / alpha) + mp.mpf(10) ** -40))
    out['L3'] = float(mp.fsum(k * W[k] * max(0, mp.log(Lam / k)) for k in range(1, n + 1)) / I)
    V2 = 4 * up * lo
    out['Vrel'] = float(abs(V2 - V) / V2)
    out['L4'] = float((V2 * mp.log(1 / V2) - I * max(0, mp.log(4 * rho / V2))) / I)
    out['T'] = float(lhs / I)
    out['rho'] = float(rho); out['J/I'] = float(J / I)
    out['lhs/(I-V)'] = float(lhs / (I - V)) if I > V else None
    return out
if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2])
    worst = {}
    cases = []
    for n in range(1, 13):
        for t in range(1, n + 1):
            for e in [1, 2, 4, 8, 16, 30]:
                for p in [mp.mpf(10) ** -e, 1 - mp.mpf(10) ** -e]:
                    cases.append((n, t, p))
            for p in ['0.5', '0.3', '0.1', '0.7', '0.9']:
                cases.append((n, t, mp.mpf(p)))
    for _ in range(T):
        n = rng.randint(13, 40); t = rng.randint(1, n)
        u = rng.random()
        p = mp.mpf(10) ** (-rng.uniform(0, 20)) if u < 0.4 else (1 - mp.mpf(10) ** (-rng.uniform(0, 20)) if u < 0.7 else mp.mpf(rng.uniform(0.01, 0.99)))
        cases.append((n, t, p))
    for (n, t, p) in cases:
        o = check(n, t, p)
        for kk, v in o.items():
            if v is None: continue
            if kk in ('rho', 'J/I'):
                if 2 <= t <= n - 1:
                    key = kk + '_mid'
                    if key not in worst or (v > worst[key][0] if kk == 'rho' else v < worst[key][0]): worst[key] = (v, n, t, float(p))
                continue
            if kk not in worst or v > worst[kk][0]: worst[kk] = (v, n, t, float(p))
    for kk, v in sorted(worst.items()):
        print(kk, v)
