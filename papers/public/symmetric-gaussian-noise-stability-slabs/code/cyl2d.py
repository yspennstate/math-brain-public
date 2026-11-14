"""In R^2: exact noise stability P(X in A, Y in A) of the four symmetric cylinder candidates of Gaussian measure a:
ball B(0,r), complement of a ball, strip |x1| <= t, complement of a strip. Which wins, on a (rho, a) grid?"""
import math, sys
import numpy as np
from scipy.stats import ncx2
from scipy.special import ndtr, erfinv

GL = np.polynomial.legendre.leggauss(400)

def interval(a, rho):                     # 1-D: P(|X|<=t, |Y|<=t), P(|Z|<=t) = a
    t = math.sqrt(2) * erfinv(a); s = math.sqrt(1 - rho * rho)
    x, w = GL; x = t * x; w = t * w
    phi = np.exp(-x ** 2 / 2) / math.sqrt(2 * math.pi)
    return float((w * phi * (ndtr((t - rho * x) / s) - ndtr((-t - rho * x) / s))).sum())

def ball(a, rho):                         # 2-D: P(|X|<=r, |Y|<=r), 1 - exp(-r^2/2) = a
    r = math.sqrt(-2 * math.log(1 - a)); s2 = 1 - rho * rho
    x, w = GL; u = r * (x + 1) / 2; w = r * w / 2
    return float((w * u * np.exp(-u ** 2 / 2) * ncx2.cdf(r * r / s2, 2, rho * rho * u * u / s2)).sum())

def cands(a, rho):
    return {'ball': ball(a, rho), 'ball_c': 2 * a - 1 + ball(1 - a, rho),
            'strip': interval(a, rho), 'strip_c': 2 * a - 1 + interval(1 - a, rho)}

if __name__ == '__main__':
    rhos = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]
    As = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.94, 0.95, 0.98]
    # sanity: rho -> 0 gives a^2, independence
    c = cands(0.3, 1e-9); assert all(abs(v - 0.09) < 1e-9 for v in c.values()), c
    print('winner table (rows rho, columns a); B ball, Bc ball complement, S strip, Sc strip complement')
    print('rho   ' + ' '.join(f'{a:>5}' for a in As))
    rows = []
    for rho in rhos:
        line = []
        for a in As:
            c = cands(a, rho)
            k = max(c, key=c.get); v = sorted(c.values())
            rows.append((rho, a, k, c[k], (v[-1] - v[-2]) / v[-1], c))
            line.append({'ball': 'B', 'ball_c': 'Bc', 'strip': 'S', 'strip_c': 'Sc'}[k])
        print(f'{rho:<5} ' + ' '.join(f'{x:>5}' for x in line))
    print()
    for rho, a, k, v, m, c in rows:
        print(f'rho={rho} a={a} win={k} {v:.10f} margin={m:.2e} ' + ' '.join(f'{n}={x:.10f}' for n, x in c.items()))
