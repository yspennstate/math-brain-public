"""Check of the constants in the window asymptotics: L_d = lim |u|^{d-1} I(u, v) and
theta_d = |S^{d-2}| L_d / ((d - 1) M) against the closed form 2^{d+1} pi^{(d-2)/2} Gamma(d/2) / ((d-1)^2 Gamma((d-1)/2)^2).
L_d is computed by direct quadrature of (1/(2d-2)) int_{R^{d-1}} max(|w - e|^2, |w|^2)^{1-d} dw in polar coordinates."""
import math
from scipy import integrate

def L_numeric(d):
    n = d - 1
    if n == 1:
        f = lambda w: max((w - 1) ** 2, w * w) ** (1 - d)
        val = integrate.quad(f, -math.inf, 0.5)[0] + integrate.quad(f, 0.5, math.inf)[0]
        return val / (2 * d - 2)
    # n >= 2: w = (t, rest), |rest| = q; integrate over t and q with the sphere factor of R^{n-1}
    sph = 2 * math.pi ** ((n - 1) / 2) / math.gamma((n - 1) / 2)
    f = lambda q, t: max((t - 1) ** 2 + q * q, t * t + q * q) ** (1 - d) * sph * q ** (n - 2)
    val = 0.0
    for a, b in [(-math.inf, 0.5), (0.5, math.inf)]:
        val += integrate.dblquad(f, a, b, 0, math.inf, epsabs=1e-11, epsrel=1e-9)[0]
    return val / (2 * d - 2)

for d in (2, 3, 4, 5):
    sph = 2 * math.pi ** ((d - 1) / 2) / math.gamma((d - 1) / 2)
    M = math.pi ** ((d - 1) / 2) * math.gamma((d - 1) / 2) / (2 * (d - 1) * math.gamma(d - 1))
    cd = 2 ** (2 - d) * math.pi ** (d / 2) / math.gamma(d / 2)
    L = L_numeric(d)
    theta = sph * L / ((d - 1) * M)
    closed = 2 ** (d + 1) * math.pi ** ((d - 2) / 2) * math.gamma(d / 2) / ((d - 1) ** 2 * math.gamma((d - 1) / 2) ** 2)
    print(f'd={d}: M={M:.6f} c_d/(2d-2)={cd / (2 * d - 2):.6f}  L_d={L:.6f}  theta_d={theta:.6f}  closed form {closed:.6f}')
