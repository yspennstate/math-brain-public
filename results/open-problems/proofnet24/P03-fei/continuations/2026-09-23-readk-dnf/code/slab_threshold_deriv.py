# The damped ratio Psi(d)/Var(d) for d = 1[N < theta], N ~ Bin(m, q): the derivative of the heavy input of
# f = 1[m x_0 + N >= theta] (theta <= m).  Its coefficient on B, |B| = b >= 1, is sigma_B^2 D_b^2 with
# D_b = (b-1)-th backward difference of the Bin(m - b, q) pmf at theta - 1, divided by 2^b (the tail function's first
# difference is minus the pmf).  Level 1 alone gives (W_1/2) ln(4/(p(theta-1))^2) ~ (W_1/2) ln(8 pi v), so the ratio
# should grow like (1/pi) ln v at the median: per-coordinate damping cannot hold for weighted thresholds.
import mpmath as mp
mp.mp.dps = 80
def binpmf(n, q): return [mp.binomial(n, k) * q ** k * (1 - q) ** (n - k) for k in range(n + 1)]
def ratio(m, q, theta):
    q = mp.mpf(q); sig2 = 4 * q * (1 - q)
    pm = binpmf(m, q); rho = mp.fsum(pm[k] for k in range(0, theta)); var = rho * (1 - rho)
    psi = mp.mpf(0); pars = mp.mpf(0)
    for b in range(1, m + 1):
        p = binpmf(m - b, q)
        get = lambda k: p[k] if 0 <= k <= m - b else mp.mpf(0)
        diff = mp.fsum((-1) ** k * mp.binomial(b - 1, k) * get(theta - 1 - k) for k in range(b))
        D = diff / mp.mpf(2) ** b
        wgt = mp.binomial(m, b) * sig2 ** b * D ** 2
        pars += wgt
        if D != 0: psi += wgt * 2 / (b + 1) * mp.log(1 / abs(D))
    return psi / var, (pars - var) / var
for m in [8, 32, 128, 512]:
    r, e = ratio(m, '0.5', m // 2)
    print('m %4d  q 0.5  theta m/2  Psi/Var %.4f   (1/pi) ln(8 pi v) %.4f  Parseval err %.1e' % (m, float(r), float(mp.log(8 * mp.pi * m / 4) / mp.pi), float(e)), flush=True)
