"""Two tokens, no MLP blocks: P(zeta < infinity) from (3.2) in closed form.

s'(y) = (1 + lam y^2)^(-p) with p = 1/(4 gamma^2), lam = 2k^2/c = gamma^2/(2 tau0^2 (2 - gamma^2)).
With x = sqrt(lam) w0 and F(x) = int_0^x (1+u^2)^(-p) du = x 2F1(1/2, p; 3/2; -x^2),
F(inf) = (sqrt(pi)/2) Gamma(p - 1/2)/Gamma(p), finite iff gamma^2 < 1/2, so

    P = 2 Gamma(p) x 2F1(1/2, p; 3/2; -x^2) / (sqrt(pi) Gamma(p - 1/2)).

Limits: P -> erf(w0/(4 tau0)) as gamma^2 -> 0; P ~ 2 asinh(w0/(sqrt(6) tau0)) (1/2 - gamma^2) as gamma^2 -> 1/2.
Checked here against direct quadrature of (3.2), the form used by feller_closed.py.
"""
import numpy as np
from scipy.integrate import quad
from scipy.special import hyp2f1, gammaln, erf


def p_closed(g2, w0=1.0, tau0=1.0):
    p = 1.0 / (4 * g2)
    x = np.sqrt(g2 / (2 * tau0**2 * (2 - g2))) * w0
    return 2 * np.exp(gammaln(p) - gammaln(p - 0.5)) * x * hyp2f1(0.5, p, 1.5, -x * x) / np.sqrt(np.pi)


def p_quad(g2, w0=1.0, tau0=1.0):
    c = g2 * (2 - g2)
    k = g2 / (2 * tau0)
    s = lambda y: (1 + 2 * k * k * y * y / c) ** (-1 / (4 * g2))
    num = quad(s, 0, w0, limit=200)[0]
    return num / (num + quad(s, w0, np.inf, limit=400)[0])


if __name__ == "__main__":
    print(" gamma^2   closed      quadrature  |diff|")
    worst = 0.0
    for g2 in [0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.48]:
        a, b = p_closed(g2), p_quad(g2)
        worst = max(worst, abs(a - b))
        print(f" {g2:5.2f}    {a:.6f}    {b:.6f}    {abs(a-b):.1e}")
    print("worst |closed - quadrature| =", f"{worst:.1e}")
    print("gamma^2 -> 0:   P(1e-4) =", f"{p_closed(1e-4):.6f}", " erf(1/4) =", f"{erf(0.25):.6f}")
    for e in [1e-2, 1e-3, 1e-4]:
        print(f"gamma^2 = 1/2 - {e:g}: P/(1/2 - gamma^2) =", f"{p_closed(0.5 - e)/e:.6f}",
              " 2 asinh(1/sqrt 6) =", f"{2*np.arcsinh(1/np.sqrt(6)):.6f}")
