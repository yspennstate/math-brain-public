"""In R^n: the cylinder B^k x R^{n-k} of Gaussian measure a has noise stability f_k(a) = P(|X|<=r, |Y|<=r) for
rho-correlated standard Gaussians in R^k with P(|X|<=r) = a (the R^{n-k} factor is free). Its complement has
2a - 1 + f_k(1 - a). So among cylinders in R^n the best is max over k <= n of these. Which k wins, for which (rho, a)?
f_1 is the interval; f_k by quadrature over |X| (chi law, k dof) with |Y| given X noncentral chi-square."""
import math
import numpy as np
from scipy.stats import ncx2, chi2
from scipy.special import gammaln

GL = np.polynomial.legendre.leggauss(600)

def f(k, a, rho):
    r2 = chi2.ppf(a, k); r = math.sqrt(r2); s2 = 1 - rho * rho
    x, w = GL; u = r * (x + 1) / 2; w = r * w / 2
    dens = np.exp((k - 1) * np.log(np.maximum(u, 1e-300)) - u * u / 2 - (k / 2 - 1) * math.log(2) - gammaln(k / 2))
    return float((w * dens * ncx2.cdf(r2 / s2, k, rho * rho * u * u / s2)).sum())

def cands(a, rho, K):
    out = {}
    for k in range(1, K + 1):
        out[f'B{k}'] = f(k, a, rho)
        out[f'B{k}c'] = 2 * a - 1 + f(k, 1 - a, rho)
    return out

if __name__ == '__main__':
    assert abs(f(2, 0.3, 1e-9) - 0.09) < 1e-9 and abs(f(5, 0.7, 1e-9) - 0.49) < 1e-9
    K = 6
    rhos = [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 0.95]
    As = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98]
    for n in [2, 3, 4, 6]:
        print(f'n = {n}: best cylinder B^k x R^(n-k) (Bk) or its complement (Bkc); rows rho, columns a')
        print('rho   ' + ' '.join(f'{a:>5}' for a in As))
        for rho in rhos:
            line = []
            for a in As:
                c = cands(a, rho, n); k = max(c, key=c.get)
                line.append(k)
            print(f'{rho:<5} ' + ' '.join(f'{x:>5}' for x in line))
        print()
    # margins for the middle-k winners
    print('cases where a k with 1 < k < n wins in n = 6, with the margin over the best k in {1, n}:')
    for rho in rhos:
        for a in As:
            c = cands(a, rho, 6); k = max(c, key=c.get)
            kk = int(k[1:].rstrip('c'))
            if 1 < kk < 6:
                ends = max(v for n_, v in c.items() if int(n_[1:].rstrip('c')) in (1, 6))
                print(f'  rho={rho} a={a} winner={k} {c[k]:.10f} margin={c[k] / ends - 1:+.2e}')
