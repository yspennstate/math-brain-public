"""T390: closed-form asymptotics of the score-matching weight efficiency for 1/2 N(-m,1) + 1/2 N(m,1).

Weight parameter eta (w = e^eta/(e^eta + e^-eta)): p_eta(x) = phi(x) e^{-m^2/2} cosh(m x + eta)/cosh(eta).
Score s = -x + m tanh(m x + eta); g = d_eta s = m sech^2(m x) at eta = 0.
Hyvarinen per-sample loss l = s^2/2 + s'; d_eta l = s g + g' = -m sech^2(m x) (x + m tanh(m x)).
H = E[g^2], V = E[(d_eta l)^2], MLE Fisher I = E[tanh^2(m x)]; ARE = (1/I)/(V/H^2).
Prediction for large m: H ~ m e^{-m^2/2} phi(0) pi/2, V ~ m^3 e^{-m^2/2} phi(0) pi/8, so ARE ~ sqrt(2 pi) e^{-m^2/2}/m.

DSM at noise sigma with the noise integrated out: per-sample loss E_eps[l_sigma(x + sigma eps)] where l_sigma is the Hyvarinen loss of
the smoothed mixture (variance tau^2 = 1 + sigma^2). H is the smoothed model's; V = Var_x E_eps[...] <= the smoothed V (total variance).
"""
import math
import numpy as np

np.seterr(all="ignore")
phi0 = 1 / math.sqrt(2 * math.pi)


def moments(m, tau=1.0, grid=None):
    """H, V (no noise averaging) and I for the mixture of N(+-m, tau^2)."""
    L = m + 12 * tau
    x = np.linspace(-L, L, 400001) if grid is None else grid
    dx = x[1] - x[0]
    a = m / tau ** 2
    p = 0.5 * (np.exp(-(x - m) ** 2 / (2 * tau ** 2)) + np.exp(-(x + m) ** 2 / (2 * tau ** 2))) / (tau * math.sqrt(2 * math.pi))
    t = np.tanh(a * x); sech2 = 1 - t * t
    g = a * sech2                                  # d_eta of score
    dl = (-x / tau ** 2 + a * t) * g + (-2 * a * a * sech2 * t)
    H = float((g * g * p).sum() * dx); V = float((dl * dl * p).sum() * dx); I = float((t * t * p).sum() * dx)
    return H, V, I


print("(1) sigma = 0: exact ARE of the weight against sqrt(2 pi) e^{-m^2/2}/m")
print("m    ARE exact      asymptotic     ratio")
for m in [1, 2, 3, 4, 5, 6, 8]:
    H, V, I = moments(m)
    are = H * H / (V * I)
    asy = math.sqrt(2 * math.pi) * math.exp(-m * m / 2) / m
    print(f"{m}   {are:.4e}     {asy:.4e}     {are / asy:.4f}")

print("\n(2) DSM at noise sigma, noise integrated out (Gauss-Hermite, 80 nodes): ARE and the lower bound H_s^2/(V_s I)")
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(80); gh_w = gh_w / gh_w.sum()
print("m    sigma   ARE DSM     lower bound   m' = m/tau   sqrt(2pi)e^{-m'^2/2}/m'")
for m in [3.0, 5.0]:
    _, _, I = moments(m)
    for sigma in [0.0, 0.5 * m, m, 2 * m]:
        tau = math.sqrt(1 + sigma * sigma); a = m / tau ** 2
        L = m + 12; x = np.linspace(-L, L, 120001); dx = x[1] - x[0]
        p = 0.5 * (np.exp(-(x - m) ** 2 / 2) + np.exp(-(x + m) ** 2 / 2)) / math.sqrt(2 * math.pi)
        Ex = np.zeros_like(x); Eg = np.zeros_like(x)
        for e, wgt in zip(gh_x, gh_w):
            y = x + sigma * e
            t = np.tanh(a * y); sech2 = 1 - t * t; g = a * sech2
            Ex += wgt * ((-y / tau ** 2 + a * t) * g - 2 * a * a * sech2 * t)
            Eg += wgt * g * g
        H = float((Eg * p).sum() * dx); V = float((Ex * Ex * p).sum() * dx)
        Hs, Vs, _ = moments(m, tau)
        mp = m / tau
        print(f"{m:.0f}    {sigma:4.1f}    {H * H / (V * I):.4f}      {Hs * Hs / (Vs * I):.4f}        {mp:.3f}        "
              f"{math.sqrt(2 * math.pi) * math.exp(-mp * mp / 2) / mp:.4f}")
