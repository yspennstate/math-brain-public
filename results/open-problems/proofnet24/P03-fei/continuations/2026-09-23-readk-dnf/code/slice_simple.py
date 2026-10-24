# Simple Gibbs bound for the damped slice quantity: S(d) = sum_k (U_k/(k+1)) ln(e_k(sigma^2)/U_k) >= Psi(d).
# Reports worst S/Var(d) and worst Psi/Var(d), split by rho <= 1/2 and rho > 1/2, plus Lambda/(1-rho) when rho > 1/2.
import mpmath as mp, random, sys
from isoper3 import biased_P
from slice_damped import rq
mp.mp.dps = 40
def elem(vals, k):
    e = [mp.mpf(1)] + [mp.mpf(0)] * k
    for v in vals:
        for j in range(k, 0, -1): e[j] += e[j - 1] * v
    return e[k]
def run(n, s, q):
    d = [1 if bin(x).count('1') == s else 0 for x in range(1 << n)]
    P = biased_P(d, q); sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    U = mp.fsum(P[1:]) / 4
    Uk = [mp.mpf(0)] * (n + 1); psi = mp.mpf(0)
    for B in range(1, 1 << n):
        c2 = P[B] / 4
        if c2 > 0:
            k = bin(B).count('1'); Uk[k] += c2
            psi += c2 / (k + 1) * mp.log(mp.fprod(sig2[i] for i in range(n) if B >> i & 1) / c2)
    S = mp.fsum(Uk[k] / (k + 1) * mp.log(elem(sig2, k) / Uk[k]) for k in range(1, n + 1) if Uk[k] > 0)
    rho = mp.fsum(mp.fprod(mp.mpf(q[i]) if x >> i & 1 else 1 - mp.mpf(q[i]) for i in range(n)) for x in range(1 << n) if d[x])
    return float(S / U), float(psi / U), float(rho), float(mp.fsum(sig2))
if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
    w = {}
    for trial in range(T):
        n = rng.randint(1, nmax); s = rng.randint(0, n); q = [rq(rng) for _ in range(n)]
        d = [1 if bin(x).count('1') == s else 0 for x in range(1 << n)]
        try:
            Sr, Pr, rho, Lam = run(n, s, q)
        except Exception as e:
            continue
        if rho <= 0 or rho >= 1 or rho * (1 - rho) < 1e-28: continue
        reg = 'lo' if rho <= 0.5 else 'hi'
        for key, val in (('S_' + reg, Sr), ('psi_' + reg, Pr)):
            if key not in w or val > w[key][0]: w[key] = (val, n, s, ['%.3g' % v for v in q], rho, Lam)
        if reg == 'hi':
            v = Lam / (1 - rho)
            if 'Lam_over_1mrho' not in w or v > w['Lam_over_1mrho'][0]: w['Lam_over_1mrho'] = (v, n, s, ['%.3g' % x for x in q], rho, Lam)
        if trial % 300 == 0: print(trial, {k: round(v[0], 3) for k, v in w.items()}, flush=True)
    for k, v in w.items(): print('WORST', k, v)
