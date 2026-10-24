# Damped slice inequality at large m, equal biases.  For d = 1[N = s], N ~ Bin(m, q), the biased Fourier
# coefficient on a set B with |B| = b is  d~(B)^2 = sigma_B^2 D_b^2  with  D_b = (backward difference of order b of the
# Bin(m - b, q) pmf at s) / 2^b,  sigma_B^2 = (4 q (1 - q))^b.  (Derivation: E[d prod_{i in B}(y_i - q_i)] equals
# prod_{i in B} q_i (1 - q_i) times the b-th backward difference of the pmf of the count outside B.)  Hence
#     Psi(d) = sum_{b >= 1} C(m, b) sigma^{2b} D_b^2 (2 / (b + 1)) ln(1 / |D_b|),   Var(d) = rho (1 - rho).
# The script checks Parseval (sum_b C(m,b) sigma^{2b} D_b^2 = Var) and prints Psi / Var as m grows.
import mpmath as mp, sys
mp.mp.dps = 60

def binpmf(n, q):
    # pmf of Bin(n, q) as a list, exact in mpmath
    return [mp.binomial(n, k) * q ** k * (1 - q) ** (n - k) for k in range(n + 1)]

def psi_ratio(m, q, s):
    q = mp.mpf(q)
    sig2 = 4 * q * (1 - q)
    pm = binpmf(m, q); rho = pm[s]; var = rho * (1 - rho)
    psi = mp.mpf(0); pars = mp.mpf(0)
    for b in range(1, m + 1):
        p = binpmf(m - b, q)
        get = lambda k: p[k] if 0 <= k <= m - b else mp.mpf(0)
        diff = mp.fsum((-1) ** (b - k) * mp.binomial(b, k) * get(s - k) for k in range(b + 1))
        D = diff / mp.mpf(2) ** b
        wgt = mp.binomial(m, b) * sig2 ** b * D ** 2
        pars += wgt
        if D != 0:
            psi += wgt * 2 / (b + 1) * mp.log(1 / abs(D))
    return psi / var, (pars - var) / var, rho

if __name__ == '__main__':
    for q in ['0.5', '0.1', '0.01']:
        for m in [4, 8, 16, 32, 64, 128, 256]:
            qq = mp.mpf(q)
            smean = int(round(m * float(qq)))
            for s in sorted(set([max(0, smean - 1), smean, min(m, smean + 1), min(m, smean + int(2 * (m * float(qq)) ** 0.5) + 1)])):
                r, perr, rho = psi_ratio(m, q, s)
                print('q %s m %4d s %4d  rho %.3e  Psi/Var %.4f  (Parseval err %.1e)' % (q, m, s, float(rho), float(r), float(perr)), flush=True)
